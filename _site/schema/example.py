import jsonasobj
from nmdc import *

s = Biosample(id='GOLD:001', name='test sample')
kvs = {
    'depth': '2cm',
    'biome': 'ocean',
    'material': 'seawater'
}

for k,v in kvs.items():
    c = Characteristic(id=k)
    ann = Annotation(has_characteristic=c, has_raw_value=v)
    s.annotations.append(ann)

json = jsonasobj.as_json(s)
print(json)
