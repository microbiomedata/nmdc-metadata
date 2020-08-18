import os
import sys
import yaml
import requests
import wget

from biolinkml.generators.yumlgen import YumlGenerator

YAML_SPEC = sys.argv[1]
OUTPUT = sys.argv[2]

model = yaml.load(open(YAML_SPEC), Loader=yaml.FullLoader)
yuml = YumlGenerator(model).serialize()
yuml = yuml.replace(' ', '%20')
yuml = yuml.replace('<', '%3C')
yuml = yuml.replace('^', '%5E')
yuml = yuml.replace('>', '%3E')
yuml = yuml.replace('|', '%7C')
yuml = yuml.replace('*', '%2A')
yuml = yuml.replace('&#124;', '%7C')

# Using HTTP POST for large YUML
base_url = "https://yuml.me"
handler = "diagram/nofunky/class/"
dsl_text = f"dsl_text={yuml.replace('http://yuml.me/diagram/nofunky;dir:TB/class/', '')}"
post_url = f"{base_url}/{handler}"
response = requests.post(post_url, data=dsl_text)

# yuml.me returns with a token for the rendered file, which we then download
token = response.text
get_url = f"{base_url}/{token.replace('svg', 'png')}"

if os.path.exists(OUTPUT):
    os.remove(OUTPUT)

file = wget.download(get_url, OUTPUT)
print(f"\nUML diagram written to {file}")
