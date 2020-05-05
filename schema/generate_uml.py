import sys
import yaml
import requests
from biolinkml.generators.yumlgen import YumlGenerator

YAML_SPEC = sys.argv[1]
OUTPUT = sys.argv[2]

model = yaml.load(open(YAML_SPEC), Loader=yaml.FullLoader)
yuml = YumlGenerator(model).serialize()
yuml = yuml.replace('&#124;', '|')
if not yuml.endswith('.png'):
    # append the desired format
    yuml += '.png'
myfile = requests.get(yuml)
open(OUTPUT, 'wb').write(myfile.content)
