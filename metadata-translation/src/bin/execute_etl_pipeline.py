import os, sys
sys.path.append(os.path.abspath('../../../schema')) # add path nmdc schema files and modules

import yaml
import json
from yaml import CLoader as Loader, CDumper as Dumper
from collections import namedtuple
from pprint import pprint
import pandas as pds
import jsonasobj
import nmdc
import lib.data_operations as dop
import align_nmdc_datatypes
import jq


def get_json(file_path):
    ## load json
    with open(file_path, 'r') as in_file:
        json_list =  json.load(in_file)
    return json_list


def save_json(json_list, file_path):
    ## save json with changed data types
    with open(file_path, 'w') as out_file:
        json.dump(json_list, out_file, indent=2)
    return json_list


def make_merged_data_source(spec_file='lib/nmdc_data_source.yaml', save_path='../data/nmdc_merged_data.tsv'):
    """Create a new data source containing the merged data sources"""

    mdf = dop.make_dataframe_from_spec_file (spec_file) # build merged data frame (mdf)
    mdf.to_csv(save_path, sep='\t', index=False) # save merged data
    print ('merged data frame length: ', len(mdf))

    return mdf


def make_json_etl(dataframe, nmdc_class, spec_class_name, spec_file='lib/nmdc_data_source.yaml', attribute_map_file=''):
    with open(spec_file, 'r') as input_file: # load data specificaiton info
        spec = yaml.load(input_file, Loader=Loader)
    
    ## specify attributes and constructor args
    attributes = spec['classes'][spec_class_name]['attributes']
    constructor = spec['classes'][spec_class_name]['constructor']

    attr_map = {}
    if len(attribute_map_file) > 0:
        ## create map betweeen gold fields and mixs terms
        mapping_df = dop.make_dataframe(attribute_map_file)
        attr_map = dop.make_gold_to_mixs_map(attributes, mapping_df, 'biosample')

    ## build json
    data_dictdf = dataframe.to_dict(orient="records") # transorm dataframe to dictionary
    data_json_list = dop.make_json_string_list \
        (data_dictdf, nmdc_class, constructor_map=constructor, attribute_fields=attributes, attribute_map=attr_map)
    
    ## return json
    return data_json_list


def make_nmdc_database():
    gold_study = get_json("output/nmdc_etl/gold_study.json")
    gold_biosample = get_json("output/nmdc_etl/gold_biosample.json")
    gold_project = get_json("output/nmdc_etl/gold_omics_processing.json")
    emsl_project = get_json("output/nmdc_etl/emsl_omics_processing.json")
    emsl_data_object = get_json("output/nmdc_etl/emsl_data_objects.json")
    jgi_data_object = get_json("output/nmdc_etl/jgi_fastq_data_objects.json")

    database = \
    {
        "study_set": [*gold_study], 
        "omics_processing_set": [*gold_project, *emsl_project], 
        "biosample_set": [*gold_biosample], 
        "data_object_set": [*jgi_data_object, *emsl_data_object]
    }

    save_json(database, "output/nmdc_database.json" )


def make_nmdc_example_database():
    ## load biosample json and get list of biosamples
    biosample_json = get_json('output/nmdc_etl/gold_biosample.json')
    biosample_test = json.loads(jq.compile('.[0:5]').input(biosample_json).text())
    biosample_list = jq.compile('.[0:5]| .[] | .id').input(biosample_json).text().replace('\n', ', ')

    ## load projects (omics processing)
    projects_json = get_json('output/nmdc_etl/gold_omics_processing.json')

    ## get list of associated projects from biosample
    # projects_list = jq.compile('.[] | .has_input[]').input(biosample_test).text().replace('\n', ', ')

    # projects_test = jq.compile('.[] | select(.id == (' + projects_list + '))').input(projects_json).text()
    projects_test = jq.compile('.[] | select(.has_input[]? == (' + biosample_list + '))').input(projects_json).text()
    projects_test = json.loads('[' + projects_test.replace('\n', ',') + ']') # put into correct json

    ## get list of studies
    study_list = jq.compile('.[] | .part_of[]').input(projects_test).text().replace('\n', ', ')
    study_list = ','.join(set(study_list.replace(' ', '').split(','))) # get unique list of study ids

    ## load study json
    study_json = get_json('output/nmdc_etl/gold_study.json')
    study_test = jq.compile('.[] | select(.id == (' + study_list + '))').input(study_json).text()
    study_test = json.loads('[' + study_test.replace('\n', ',') + ']') # put into correct json

    ## get outputs of projects
    data_objects_list = jq.compile('.[] | .has_output[]').input(projects_test).text().replace('\n', ', ')

    ## load data objects
    data_objects_json = get_json('output/nmdc_etl/jgi_fastq_data_objects.json')
    data_objects_test = jq.compile('.[] | select(.id == (' + data_objects_list + '))').input(data_objects_json).text().replace('\n', ', ')
    data_objects_test = json.loads('[' + data_objects_test.replace('\n', ',') + ']') # put into correct json

    ## compile into database object
    database = \
    {
      "study_set": [*study_test], 
      "omics_processing_set": [*projects_test], 
      "biosample_set": [*biosample_test], 
      "data_object_set": [*data_objects_test]
    }

    save_json(database, 'output/nmdc-03.json')

    
def main(data_file='../data/nmdc_merged_data.tsv.zip',
         etl_modules=['gold_study', 
                      'gold_omics_processing', 
                      'gold_biosample', 
                      'emsl_omics_processing',
                      'emsl_data_object', 
                      'jgi_data_object']):

    # build merbed data frame (mdf) from saved file
    mdf = pds.read_csv(data_file, sep='\t', dtype=str)
    
    ## Extract tables from merged dataset
    study_table = dop.extract_table(mdf, 'study_table')
    contact_table = dop.extract_table(mdf, 'contact_table')
    proposals_table = dop.extract_table(mdf, 'proposals_table')
    project_table = dop.extract_table(mdf, 'project_table')
    jgi_emsl_table = dop.extract_table(mdf, 'ficus_jgi_emsl')
    emsl_table = dop.extract_table(mdf, 'ficus_emsl')
    emsl_biosample_table = dop.extract_table(mdf, 'ficus_emsl_biosample')
    fastq_table = dop.extract_table(mdf, 'ficus_fastq_table')
    project_biosample_table = dop.extract_table(mdf, 'project_biosample_table')
    biosample_table = dop.extract_table(mdf, 'biosample_table')

    ## build dataframes from tables
    study = dop.make_study_dataframe(study_table, contact_table, proposals_table) # gold studies
    emsl = dop.make_emsl_dataframe(emsl_table, jgi_emsl_table, study_table, emsl_biosample_table) # emsl projects / data objects
    # data_objects = dop.make_data_objects_dataframe(faa_table, fna_table, fastq_table, project_table) # jgi data objects
    fastq = dop.make_jgi_fastq_dataframe(fastq_table, project_table)
    biosample = dop.make_biosample_dataframe(biosample_table, project_biosample_table, project_table) # gold biosamples
    project = dop.make_project_dataframe(project_table, study_table, contact_table, fastq, project_biosample_table, biosample) # gold projects

    if 'gold_study' in etl_modules:
        gold_study_json = make_json_etl(study, nmdc.Study, 'gold_study')
        dop.save_json_string_list("output/nmdc_etl/gold_study.json", gold_study_json)
    
    if 'gold_omics_processing' in etl_modules:
        gold_json_op = make_json_etl(project, nmdc.OmicsProcessing, 'gold_omics_processing')
        dop.save_json_string_list("output/nmdc_etl/gold_omics_processing.json", gold_json_op)

    if 'gold_biosample' in etl_modules:
        gold_biosample_json = make_json_etl(dataframe=biosample, 
                                            nmdc_class=nmdc.Biosample, 
                                            spec_class_name='gold_biosample', 
                                            attribute_map_file='../data/GOLD-to-mixs-map.tsv')
        dop.save_json_string_list("output/nmdc_etl/gold_biosample.json", gold_biosample_json)
        align_nmdc_datatypes.align_gold_biosample() # currently broken

    if 'emsl_omics_processing' in etl_modules:
        emsl_json_op = make_json_etl(emsl, nmdc.OmicsProcessing, 'emsl_omics_processing')
        dop.save_json_string_list("output/nmdc_etl/emsl_omics_processing.json", emsl_json_op)
    
    if 'emsl_data_object' in etl_modules:
        emsl_json_do = make_json_etl(emsl, nmdc.DataObject, 'emsl_data_object')
        dop.save_json_string_list("output/nmdc_etl/emsl_data_objects.json", emsl_json_do)
        align_nmdc_datatypes.align_emsl_data_object()
        
    if 'jgi_data_object' in etl_modules:
        jgi_json_do = make_json_etl(fastq, nmdc.DataObject, 'jgi_data_object')
        dop.save_json_string_list("output/nmdc_etl/jgi_fastq_data_objects.json", jgi_json_do)
        align_nmdc_datatypes.align_jgi_data_object()


if __name__ == '__main__':
    # make_merged_data_source() # consolidates all nmdc data into a single tsv
    # main(etl_modules=['gold_biosample']) # test gold biosample etl
    # main(etl_modules=['gold_omics_processing']) # test gold project etl
    # main(etl_modules=['jgi_data_object']) # test jgi data object etl
    # main(etl_modules=['emsl_data_object']) # test emsl data object etl
    main() # run etl on all files
    make_nmdc_database() # combines output into database json format
    make_nmdc_example_database() # make example data