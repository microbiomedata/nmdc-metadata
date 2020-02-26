import sys
import json
import jsonschema
import argparse

parser = argparse.ArgumentParser(description='Validate a data JSON against a given schema')
parser.add_argument('--data', type=str, help='Data JSON', required=True)
parser.add_argument('--schema', type=str, help='JSONSchema for validation', required=True)
parser.add_argument('--class_type', type=str, help='Class from JSONSchema that is being checked against', required=True)
args = parser.parse_args()
print(args)

data_file = args.data
schema_file = args.schema
class_type = args.class_type

json_data = json.load(open(data_file))
schema = json.load(open(schema_file))

for x in json_data:
	jsonschema.validate(x, schema=schema['properties'][class_type])
