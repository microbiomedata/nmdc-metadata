"""
PYTHONPATH=. pipenv run python examples/nmdc-example.py
"""

from schema.nmdc import Biosample, GeolocationValue, ControlledTermValue, QuantityValue, Activity, OntologyClass


a = Activity(activity_id='A1')
s = Biosample(id='S1',
              lat_lon=GeolocationValue(has_raw_value='1.0 1.0'),
              env_broad_scale=ControlledTermValue(has_raw_value="tropical moist broadleaf forest biome [ENVO:01000228]",
                                                  was_generated_by=a.activity_id),
              env_local_scale=ControlledTermValue(
                  has_raw_value="understory [ENVO:01000335]",
                  term=OntologyClass(id="ENVO:01000335",
                                     name="understory")
              ),
              env_medium=ControlledTermValue(has_raw_value="plant matter [ENVO:01001121]"),
              depth=QuantityValue("5 cm")
                                       
)
print(s)
