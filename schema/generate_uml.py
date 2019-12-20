import yaml
import requests
from biolinkml.generators.yumlgen import YumlGenerator

YAML_SPEC = 'nmdc.yaml'
OUTPUT = 'nmdc_schema_uml.png'

model = yaml.load(open(YAML_SPEC), Loader=yaml.FullLoader)
yuml = YumlGenerator(model).serialize()
yuml = yuml.replace('&#', '|')
myfile = requests.get(yuml)
open(OUTPUT, 'wb').write(myfile.content)
