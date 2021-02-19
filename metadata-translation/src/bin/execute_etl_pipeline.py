import os, sys, click
from git_root import git_root
sys.path.append(os.path.abspath(git_root('schema'))) # add path nmdc schema files and modules

from lib.nmdc_etl_class import NMDC_ETL
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
from git_root import git_root

def get_json(file_path, replace_single_quote=False):
    ## load json
    with open(file_path, 'r') as in_file:
        if replace_single_quote: # json
            text = in_file.read()
            json_list = json.loads(text.replace("'", '"'))
        else:
            json_list =  json.load(in_file)
    return json_list


def save_json(json_data, file_path):
    ## save json with changed data types
    with open(file_path, 'w') as out_file:
        json.dump(json_data, out_file, indent=2)
    return json_data


def make_merged_data_source(spec_file='lib/nmdc_data_source.yaml', save_path='../data/nmdc_merged_data.tsv'):
    """Create a new data source containing the merged data sources"""

    mdf = dop.make_dataframe_from_spec_file (spec_file) # build merged data frame (mdf)
    mdf.to_csv(save_path, sep='\t', index=False) # save merged data
    print ('merged data frame length: ', len(mdf))

    return mdf


def make_test_datasets():
    gold_study = get_json("output/nmdc_etl/gold_study.json")
    gold_biosample = get_json("output/nmdc_etl/gold_biosample.json")
    gold_project = get_json("output/nmdc_etl/gold_omics_processing.json")
    emsl_project = get_json("output/nmdc_etl/emsl_omics_processing.json")
    emsl_data_object = get_json("output/nmdc_etl/emsl_data_objects.json")
    # jgi_data_object = get_json("output/nmdc_etl/jgi_fastq_data_objects.json")
    
    mg_assembly_activities = get_json('../data/aim-2-workflows/metagenome_assembly_activities.json')
    mg_assembly_data_objects = get_json('../data/aim-2-workflows/metagenome_assembly_data_objects.json')
    readQC_activities = get_json('../data/aim-2-workflows/readQC_activities.json')
    readQC_data_objects = get_json('../data/aim-2-workflows/readQC_data_objects.json')

    ## make study_test subset
    study_test = jq.compile('.[0:3] | .[]').input(gold_study).all()
    save_json({ "study_set": study_test}, 'output/study_test.json')
    
    ## make biosample test
    biosample_test =  jq.compile('.[0:3] | .[]').input(gold_biosample).all()
    save_json({ "biosample_set": biosample_test}, 'output/biosample_test.json')
    
    ## make gold omics processing test
    gold_project_test =  jq.compile('.[0:3] | .[]').input(gold_project).all()
    save_json({ "omics_processing_set": gold_project_test}, 'output/gold_project_test.json')
    
    ## make emsl omics processing test
    emsl_project_test =  jq.compile('.[0:3] | .[]').input(emsl_project).all()
    save_json({ "omics_processing_set": emsl_project_test}, 'output/emsl_project_test.json')
    
    ## make emsl data objects test
    emsl_data_object_test =  jq.compile('.[0:3] | .[]').input(emsl_data_object).all()
    save_json({ "data_object_set": emsl_data_object_test}, 'output/emsl_data_object_test.json')

    ## make metagenome activities test
    mg_assembly_activities_test = jq.compile('.[0:3] | .[]').input(mg_assembly_activities).all()
    save_json({ "metagenome_assembly_set": mg_assembly_activities_test}, 'output/mg_assembly_activities_test.json')
    
    ## make metagenome data objects test
    mg_assembly_data_objects_test = jq.compile('.[0:3] | .[]').input(mg_assembly_data_objects).all()
    save_json({ "data_object_set": mg_assembly_data_objects_test}, 'output/mg_assembly_data_objects_test.json')
    
    ## make read QC activities test
    readQC_activities_test = jq.compile('.[0:3] | .[]').input(readQC_activities).all()
    save_json({ "read_QC_analysis_activity_set": readQC_activities_test}, 'output/readQC_activities_test.json')
    
    ## make metagenome data objects test
    readQC_data_objects_test = jq.compile('.[0:3] | .[]').input(readQC_data_objects).all()
    save_json({ "data_object_set": readQC_data_objects_test}, 'output/readQC_data_objects_test.json')
    
    
def make_nmdc_database():
    gold_study = get_json("output/nmdc_etl/gold_study.json")
    gold_biosample = get_json("output/nmdc_etl/gold_biosample.json")
    gold_project = get_json("output/nmdc_etl/gold_omics_processing.json")
    emsl_project = get_json("output/nmdc_etl/emsl_omics_processing.json")
    emsl_data_object = get_json("output/nmdc_etl/emsl_data_objects.json")
    jgi_data_object = get_json("output/nmdc_etl/jgi_fastq_data_objects.json")


    ## load aim 2 json files ## removed for GSP 02/2021
    # mg_annotation_activities = get_json('../data/aim-2-workflows/metagenome_annotation_activities.json')
    # mg_annotation_data_objects = get_json('../data/aim-2-workflows/metagenome_annotation_data_objects.json')

    mg_assembly_activities = get_json('../data/aim-2-workflows/metagenome_assembly_activities.json')
    mg_assembly_data_objects = get_json('../data/aim-2-workflows/metagenome_assembly_data_objects.json')

    readQC_activities = get_json('../data/aim-2-workflows/readQC_activities.json')
    readQC_data_objects = get_json('../data/aim-2-workflows/readQC_data_objects.json')

    ## metaproteomic files ## removed for GSP 02/2021
    # hess_mp_analysis_activities = get_json('../data/aim-2-workflows/Hess_metaproteomic_analysis_activities.json')
    # hess_mp_data_objects = get_json('../data/aim-2-workflows/Hess_emsl_analysis_data_objects.json')
    # stegen_mp_analysis_activities = get_json('../data/aim-2-workflows/Stegen_metaproteomic_analysis_activities.json')
    # stegen_mp_data_objects = get_json('../data/aim-2-workflows/Stegen_emsl_analysis_data_objects.json')

    database = \
    {
        "study_set": [*gold_study], 
        "omics_processing_set": [*gold_project, *emsl_project], 
        "biosample_set": [*gold_biosample], 
        "data_object_set": [*jgi_data_object, *emsl_data_object, *mg_assembly_data_objects,*readQC_data_objects], 
        "metagenome_assembly_set": [*mg_assembly_activities],
        "read_QC_analysis_activity_set": [*readQC_activities]
    }

    save_json(database, "output/nmdc_database.json" )


def make_nmdc_example_database():
    ## load json files
    biosample_json = get_json('output/nmdc_etl/gold_biosample.json')
    projects_json = get_json('output/nmdc_etl/gold_omics_processing.json')
    study_json = get_json('output/nmdc_etl/gold_study.json')
    data_objects_json = get_json('output/nmdc_etl/jgi_fastq_data_objects.json')

    ## get a list of distinct omics processing study ids, and choose the first 3 studies
    study_ids =  set(jq.compile('.[] | .part_of[]').input(projects_json).all()) # all returns a list
    study_ids = list(study_ids)[0:3]
    # study_ids = 

    ## build a test set of studies from the study ids
    study_test = \
        jq.compile('.[] | select( .id == (' + ', '.join('"{0}"'.format(id) for id in study_ids) + '))')\
          .input(study_json).all() # all() returns a list
       
    ## build a test set of projects from the study ids
    ## note: the jq query only selects first omics found for a given study id
    projects_test = []
    for id in study_ids:
        j = jq.compile(f'[.[] | select( .part_of[]? |  . == "{id}")][0]').input(projects_json).all()
        projects_test.append(*j)

    ## get list of unique biossample ids from omics processing and build biosample test set
    biosample_ids = jq.compile('.[] | .has_input[]?').input(projects_test).all() # all() returns a list
    biosample_test = \
        jq.compile('.[] | select( .id == (' + ', '.join('"{0}"'.format(id) for id in biosample_ids) + '))')\
          .input(biosample_json).all() # all() returns a list
           
    ## get a list of data object ids and build data objects test set
    data_objects_ids = jq.compile('.[] | .has_output[]?').input(projects_test).all() # all() returns a list
    data_objects_test = \
        jq.compile('.[] | select( .id == (' + ', '.join('"{0}"'.format(id) for id in data_objects_ids) + '))')\
          .input(data_objects_json).all() # all() returns a list
    
    ## compile into database object
    database = \
    {
      "study_set": [*study_test], 
      "omics_processing_set": [*projects_test], 
      "biosample_set": [*biosample_test], 
      "data_object_set": [*data_objects_test]
    }

    save_json(database, 'output/nmdc_example_database.json')


def execute_etl(data_file='../data/nmdc_merged_data.tsv.zip',
                etl_modules=['gold_study', 
                            'gold_omics_processing', 
                            'gold_biosample', 
                            'emsl_omics_processing',
                            'emsl_data_object', 
                            'jgi_data_object'],
                sssom_map_file=git_root('schema/mappings/gold-to-mixs.sssom.tsv'),
                spec_file='lib/nmdc_data_source.yaml'):

    nmdc_etl = NMDC_ETL(merged_data_file=data_file, data_source_spec_file=spec_file, sssom_file=sssom_map_file)
    
    if 'gold_study' in etl_modules:
        nmdc_etl.transform_study()
        # nmdc_etl.transform_study(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_study(file_path='output/nmdc_etl/gold_study.json')
    
    if 'gold_omics_processing' in etl_modules:
        nmdc_etl.transform_omics_proccessing()
        # nmdc_etl.transform_omics_proccessing(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_omics_proccessing(file_path='output/nmdc_etl/gold_omics_processing.json')

    if 'gold_biosample' in etl_modules:
        nmdc_etl.transform_biosample()
        # nmdc_etl.transform_biosample(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_biosample('output/nmdc_etl/gold_biosample.json')
        
        # align_nmdc_datatypes.align_gold_biosample() ########### currently broken

    if 'emsl_omics_processing' in etl_modules:
        nmdc_etl.transform_emsl_omics_processing()
        # nmdc_etl.transform_emsl_omics_processing(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_emsl_omics_processing('output/nmdc_etl/emsl_omics_processing.json')
        
    if 'emsl_data_object' in etl_modules:
        nmdc_etl.transform_emsl_data_object()
        # nmdc_etl.transform_emsl_data_object(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_emsl_data_object('output/nmdc_etl/emsl_data_objects.json')
        
    if 'jgi_data_object' in etl_modules:
        nmdc_etl.transform_jgi_data_object()
        # nmdc_etl.transform_jgi_data_object(test_rows=1, print_df=True, print_dict=True)
        nmdc_etl.save_jgi_data_object('output/nmdc_etl/jgi_fastq_data_objects.json')


################################# CLI interface ##########################################
@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--datafile', '-df', 
              help='the path to data that input into the ETL pipeline', 
              default=git_root('metadata-translation/src/data/nmdc_merged_data.tsv.zip'))
@click.option('--etlmodules', '-em',
              help='string of comma separated modules (e.g., "gold_study, gold_biosample") to transform',
              default="gold_study, gold_omics_processing, gold_biosample, emsl_omics_processing,emsl_data_object, jgi_data_object")
@click.option('--sssomfile', '-ssom', 
              help="path to the sssom file to use for mapping",
              default=git_root('schema/mappings/gold-to-mixs.sssom.tsv'))    
@click.option('--specfile', '-sf',
              help='the data source specification yaml file used to define the data sources',
              default=git_root('metadata-translation/src/bin/lib/nmdc_data_source.yaml'))
@click.option('--etl/--no-etl', is_flag=True, default=True,
              help='specifies whether to exectute the ETL pipeline and build the NMDC datbase; default true')
@click.option('--exdb/--no-exdb', is_flag=True, default=True,
              help='specifies whether to build the example NMDC database; default true')
@click.option('--testdata/--no-testdata', is_flag=True, default=True,
              help='specifies whether to build test datasets; default true')
@click.option('--mergedb/--no-mergedb', is_flag=True, default=False,
              help='specifies whether to build a new merged data source used for input into the ETL pipeline; default false')
@click.option('--only-mergedb', is_flag=True, default=False,
              help='specifies whether to ONLY build a new merged data source used for input into the ETL pipeline and NOT build the NMDC database, example dataase, and test datasets; default false')
def main(datafile, etlmodules, sssomfile, specfile, etl, exdb, testdata, mergedb, only_mergedb):
    if mergedb or only_mergedb:
        click.echo('building new merged database for input into ETL pipeline.')
        make_merged_data_source()
        click.echo('finished merged database')
        
    if etl and not only_mergedb:
        etl_modules = [m.strip() for m in etlmodules.split(",")]
        click.echo(f'executing etl for modules: {etl_modules}')
        execute_etl(datafile, etl_modules, sssomfile, specfile)
        click.echo('building NMDC database')
        make_nmdc_database()
        click.echo('finished NMDC database')
    
    if exdb and not only_mergedb:
        click.echo('building example NMDC database')
        make_nmdc_example_database()
        click.echo('finished example NMDC database')
    
    if testdata and not only_mergedb:
        click.echo('building NMDC test datasets')
        make_test_datasets()
        click.echo('finished NMDC test datasets')
        
    
if __name__ == '__main__':
    main() # CLI interface
    
    # make_merged_data_source() # consolidates all nmdc data into a single tsv
    
    # ----- testing etl pipeline ------ # 
    # main(etl_modules=['gold_biosample']) # test gold biosample etl
    # main(etl_modules=['gold_omics_processing']) # test gold project etl
    # main(etl_modules=['jgi_data_object']) # test jgi data object etl
    # main(etl_modules=['emsl_omics_processing']) # test emsl omics processing etl
    # main(etl_modules=['emsl_data_object']) # test emsl data object etl
    
    # ------ testing specific etl modules --------#
    # data_file='../data/nmdc_merged_data.tsv.zip'
    # sssom_map_file=git_root('schema/mappings/gold-to-mixs.sssom.tsv')
    # spec_file='lib/nmdc_data_source.yaml'
    # nmdc_etl = NMDC_ETL(merged_data_file=data_file, data_source_spec_file=spec_file, sssom_file=sssom_map_file)

    ## test GOLD biosample etl
    # nmdc_etl.transform_biosample(test_rows=5)
    # nmdc_etl.save_biosample('output/nmdc_etl/test.json')
    
    ## test emsl omic processing etl
    # nmdc_etl.transform_emsl_omics_processing()
    # nmdc_etl.save_emsl_omics_processing('output/nmdc_etl/test.json')
    # print(nmdc_etl.emsl.head())
    
    ## test GOLD study etl
    # nmdc_etl.transform_study()
    # nmdc_etl.save_study('output/nmdc_etl/test.json')
    # print(list(nmdc_etl.study.columns))
    # print(nmdc_etl.study.head())
    