## add ./lib directory to sys.path so that local modules can be found
import os, sys; sys.path.append(os.path.abspath("./lib"))
# print(sys.path)

## system level modules
import pandas as pds
import jsonasobj
import json
import zipfile


def make_dataframe(file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True,
                   replace_spaces=True, file_type="tsv", delimiter="\t", sheet_name=0, file_archive_name=""):
    """
    Builds a pandas dataframe from the designated file.
    
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        subset_cols: Specifies a specific of subset of columns to be included in the dataframe.
        exclude_cols: Specifies a specific of subset of columns to be excluded from the dataframe.
        nrows: Specifies the number of rows to be returned in the dataframe (useful for testing).
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
        file_type: Speicfies the type of file. Current acceptable file types are tsv, csv, and excel. Note that when using excel, you may need to specify a sheet name.
        delimiter: Specifies the delimiter character used between fields.
        sheet_name: If the files is an Excel spreadsheet, this parameter specifies a particular sheet.
        archive_name: If the file_name is contained in an zip or file, this is the name of archive file.
    Returns:
        Pandas dataframe
    """
    ## normalize paramaters for use with pandas
    if len(subset_cols) < 1: subset_cols = None
    if len(exclude_cols) < 1: exclude_cols = None

    ## check if file is contained in an archive
    file_archive = None
    if len(file_archive_name) > 1:
        file_archive = zipfile.ZipFile(file_archive_name, "r")

    ## load data from file
    if "tsv" == file_type.lower() or "csv" == file_type.lower():
        if None != file_archive:
            df = pds.read_csv(file_archive.open(file_name), sep=delimiter, nrows=nrows)
        else:
            df = pds.read_csv(file_name, sep=delimiter, nrows=nrows)
    elif "excel" == file_type.lower():
        if None != file_archive:
            df = pds.read_excel(file_archive.open(file_name), sheet_name=sheet_name, nrows=nrows)
        else:
            df = pds.read_excel(file_name, sheet_name=sheet_name, nrows=nrows)

    ## clean column names
    df = clean_dataframe_column_names(df, lowercase_col_names, replace_spaces)

    ## create subset of columns
    ## note: since column names are case sensitive, this needs to happen after cleaning column names
    if subset_cols:
        df = df[subset_cols]

    ## return dataframe
    return df


def clean_dataframe_column_names(df, lowercase_col_names=True, replace_spaces=True):
    """
    Changes the column names of a dataframe into a standard format. The default settings change the column names to:
      - lower case
      - replaces spaces with underscores
    Args:
        df: The dataframe whose columns will be cleaned.
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
    Returns:
      Pandas dataframe
    """

        ## clean column names
    if lowercase_col_names:
        df.columns = [c.strip().lower() for c in df.columns]

    if replace_spaces:
        df.columns = [c.replace(" ", "_") for c in df.columns]

    return df



def make_dataframe_dictionary(file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True,
                              replace_spaces=True, file_type="tsv", delimiter="\t", sheet_name=0, file_archive_name=""):
    """
    Builds a dictionary based on the structure of the pandas dataframe generated from the designated file.
    The dictionary is oriented for records.
    E.g.:
      [
        {
          'col1': 1, 
          'col2': 0.5
        }, 
        {
          'col1': 2, 
          'col2': 0.75
        }
      ]

    Essentially, this function is a shortcut for calling make_dataframe() and then transforming the result into a dictionary. 
    E.g.:
      df = make_dataframe(file_name)
      dictdf = dictdf = df.to_dict(orient="records")
    
    
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        subset_cols: Specifies a specific of subset of columns to be included in the dataframe.
        exclude_cols: Specifies a specific of subset of columns to be excluded from the dataframe.
        nrows: Specifies the number of rows to be returned in the dataframe (useful for testing).
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
        file_type: Speicfies the type of file. Current acceptable file types are tsv, csv, and excel. Note that when using excel, you may need to specify a sheet name.
        delimiter: Specifies the delimiter character used between fields.
        sheet_name: If the files is an Excel spreadsheet, this parameter specifies a particular sheet.
        archive_name: If the file_name is contained in an zip or file, this is the name of archive file.
    Returns:
        Dictionary built from a Pandas dataframe.
    """
    df = make_dataframe(file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True, \
                        replace_spaces=True, file_type="tsv", delimiter=delimiter, sheet_name=sheet_name, file_archive_name=file_archive_name)
    return df.to_dict(orient="records")



def convert_dict_list_to_json_list(dict_list):
    """
    Takes a list of dictionaries, converts each dictionary into json, and returns a list the json strings.
    Args:
      dict_list: A list in which each item is a dictionary.
    Returns:
      A list in which each item is a json string.
    """
    json_list = [] # list to hold json 

    ## iterate over dict list
    for d in dict_list:
        json_list.append(json.dumps(d))
        
    ## return final list
    return json_list


def save_json_string_list(file_name, json_list):
    """
    Saves a list of json strings to a file.
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        json_list: The list of json strings to be saved to file.
    Returns:
        Nothing.
    """
    ## merge json list into a single string
    json_str = "[\n" + ", ".join(json_list) + "\n]"

    with open(file_name, "w") as f:
        f.write(json_str)


def load_dict_from_json_file(file_name):
    """
    Creates and returns from a json file.
    Args:
      file_name: The name of the file containing the json formated data.
    Returns:
      A dict object containing the JSON dta.
    """
    with open(file_name, "r") as json_file:
        return json.load(json_file)
    
