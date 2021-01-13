---
parent: Classes
title: nmdc:Biosample
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: Biosample


A material sample. It may be environmental (encompassing many organisms) or isolate or tissue.   An environmental sample containing genetic material from multiple individuals is commonly referred to as a biosample.

URI: [nmdc:Biosample](https://microbiomedata/meta/Biosample)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TimestampValue],[TextValue],[QuantityValue],[NamedThing],[GeolocationValue],[Database],[ControlledTermValue],[BiosampleProcessing],[QuantityValue]%3Cmisc_param%200..1-++[Biosample%7Cid:string;name:string%20%3F;alternate_identifiers:string%20%2A;description(i):string%20%3F],[TextValue]%3Cal_sat_meth%200..1-++[Biosample],[QuantityValue]%3Cal_sat%200..1-++[Biosample],[TextValue]%3Cheavy_metals_meth%200..1-++[Biosample],[QuantityValue]%3Cheavy_metals%200..1-++[Biosample],[TextValue]%3Csalinity_meth%200..1-++[Biosample],[TextValue]%3Clink_addit_analys%200..1-++[Biosample],[TextValue]%3Cmicrobial_biomass_meth%200..1-++[Biosample],[QuantityValue]%3Cmicrobial_biomass%200..1-++[Biosample],[TextValue]%3Ctot_nitro_content_meth%200..1-++[Biosample],[QuantityValue]%3Ctot_nitro_content%200..1-++[Biosample],[TextValue]%3Ctot_org_c_meth%200..1-++[Biosample],[TextValue]%3Cph_meth%200..1-++[Biosample],[TextValue]%3Ctexture_meth%200..1-++[Biosample],[QuantityValue]%3Ctexture%200..1-++[Biosample],[TextValue]%3Cdrainage_class%200..1-++[Biosample],[TextValue]%3Cprofile_position%200..1-++[Biosample],[QuantityValue]%3Cslope_aspect%200..1-++[Biosample],[QuantityValue]%3Cslope_gradient%200..1-++[Biosample],[TextValue]%3Csoil_type_meth%200..1-++[Biosample],[TextValue]%3Csoil_type%200..1-++[Biosample],[TextValue]%3Clocal_class_meth%200..1-++[Biosample],[TextValue]%3Clocal_class%200..1-++[Biosample],[TextValue]%3Cfao_class%200..1-++[Biosample],[TextValue]%3Clink_class_info%200..1-++[Biosample],[QuantityValue]%3Cannual_precpt%200..1-++[Biosample],[QuantityValue]%3Cseason_precpt%200..1-++[Biosample],[QuantityValue]%3Cannual_temp%200..1-++[Biosample],[QuantityValue]%3Cseason_temp%200..1-++[Biosample],[TextValue]%3Clink_climate_info%200..1-++[Biosample],[TextValue]%3Cstore_cond%200..1-++[Biosample],[TextValue]%3Cpool_dna_extracts%200..1-++[Biosample],[QuantityValue]%3Csamp_vol_we_dna_ext%200..1-++[Biosample],[TextValue]%3Cwater_content_soil_meth%200..1-++[Biosample],[QuantityValue]%3Cwater_content%200..1-++[Biosample],[QuantityValue]%3Csieving%200..1-++[Biosample],[TextValue]%3Chorizon_meth%200..1-++[Biosample],[TextValue]%3Chorizon%200..1-++[Biosample],[TimestampValue]%3Cextreme_event%200..1-++[Biosample],[TimestampValue]%3Cflooding%200..1-++[Biosample],[TimestampValue]%3Cfire%200..1-++[Biosample],[TextValue]%3Ctillage%200..1-++[Biosample],[QuantityValue]%3Cagrochem_addition%200..1-++[Biosample],[TextValue]%3Ccrop_rotation%200..1-++[Biosample],[TextValue]%3Cprevious_land_use_meth%200..1-++[Biosample],[TextValue]%3Cprevious_land_use%200..1-++[Biosample],[TextValue]%3Ccur_vegetation_meth%200..1-++[Biosample],[TextValue]%3Ccur_vegetation%200..1-++[Biosample],[TextValue]%3Ccur_land_use%200..1-++[Biosample],[QuantityValue]%3Cchlorophyll%200..1-++[Biosample],[QuantityValue]%3Cnitrate%200..1-++[Biosample],[QuantityValue]%3Cdiss_oxygen%200..1-++[Biosample],[QuantityValue]%3Csalinity%200..1-++[Biosample],[QuantityValue]%3Celev%200..1-++[Biosample],[QuantityValue]%3Calt%200..1-++[Biosample],[QuantityValue]%3Ctot_org_carb%200..1-++[Biosample],[QuantityValue]%3Cdepth%200..1-++[Biosample],[AttributeValue]%3Cspecific_ecosystem%200..1-++[Biosample],[AttributeValue]%3Cecosystem_subtype%200..1-++[Biosample],[AttributeValue]%3Cecosystem_type%200..1-++[Biosample],[AttributeValue]%3Cecosystem_category%200..1-++[Biosample],[AttributeValue]%3Cecosystem%200..1-++[Biosample],[ControlledTermValue]%3Cenv_medium%201..1-++[Biosample],[ControlledTermValue]%3Cenv_local_scale%201..1-++[Biosample],[ControlledTermValue]%3Cenv_broad_scale%201..1-++[Biosample],[TimestampValue]%3Ccollection_date%200..1-++[Biosample],[TextValue]%3Cgeo_loc_name%200..1-++[Biosample],[GeolocationValue]%3Clat_lon%201..1-++[Biosample],[TextValue]%3Cenv_package%200..1-++[Biosample],[BiosampleProcessing]-%20has%20input%200..%2A%3E[Biosample],[Database]++-%20biosample%20set%200..%2A%3E[Biosample],[NamedThing]%5E-[Biosample],[AttributeValue])

---


## Identifier prefixes

 * GOLD

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[BiosampleProcessing](BiosampleProcessing.md)** *[biosample processing➞has input](biosample_processing_has_input.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**
 *  **[Database](Database.md)** *[biosample set](biosample_set.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**

## Attributes


### Own

 * [agrochem_addition](agrochem_addition.md)  <sub>OPT</sub>
    * Description: "Addition of fertilizers, pesticides, etc. - amount and time of applications"
    * range: [QuantityValue](QuantityValue.md)
 * [al_sat](al_sat.md)  <sub>OPT</sub>
    * Description: Aluminum saturation (esp. For tropical soils)
    * range: [QuantityValue](QuantityValue.md)
 * [al_sat_meth](al_sat_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining Al saturation
    * range: [TextValue](TextValue.md)
 * [alt](alt.md)  <sub>OPT</sub>
    * Description: "Altitude is a term used to identify heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earthbs surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air"
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (environment)
 * [annual_precpt](annual_precpt.md)  <sub>OPT</sub>
    * Description: "The average of all annual precipitation values known, or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps. "
    * range: [QuantityValue](QuantityValue.md)
 * [annual_temp](annual_temp.md)  <sub>OPT</sub>
    * Description: Mean annual temperature
    * range: [QuantityValue](QuantityValue.md)
 * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * Description: The same biosample may have distinct identifiers in different databases (e.g. GOLD and EMSL)
    * range: [String](types/String.md)
 * [biosample➞depth](biosample_depth.md)  <sub>OPT</sub>
    * range: [QuantityValue](QuantityValue.md)
 * [biosample➞env_broad_scale](biosample_env_broad_scale.md)  <sub>REQ</sub>
    * Description: formerly known as 'biome'
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_local_scale](biosample_env_local_scale.md)  <sub>REQ</sub>
    * Description: formerly known as 'feature'
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_medium](biosample_env_medium.md)  <sub>REQ</sub>
    * Description: formerly known as 'material'
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞id](biosample_id.md)  <sub>REQ</sub>
    * Description: The primary identifier for the biosample. Example: GOLD:Gb0205609
    * range: [String](types/String.md)
 * [biosample➞lat_lon](biosample_lat_lon.md)  <sub>REQ</sub>
    * Description: This is currently a required field but it's not clear if this should be required for human hosts
    * range: [GeolocationValue](GeolocationValue.md)
 * [biosample➞name](biosample_name.md)  <sub>OPT</sub>
    * Description: A human readable name or description of the biosample
    * range: [String](types/String.md)
 * [chlorophyll](chlorophyll.md)  <sub>OPT</sub>
    * Description: Concentration of chlorophyll
    * range: [QuantityValue](QuantityValue.md)
 * [collection_date](collection_date.md)  <sub>OPT</sub>
    * Description: "The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant"
    * range: [TimestampValue](TimestampValue.md)
    * in subsets: (environment)
 * [crop_rotation](crop_rotation.md)  <sub>OPT</sub>
    * Description: "Whether or not crop is rotated, and if yes, rotation schedule"
    * range: [TextValue](TextValue.md)
 * [cur_land_use](cur_land_use.md)  <sub>OPT</sub>
    * Description: Present state of sample site
    * range: [TextValue](TextValue.md)
 * [cur_vegetation](cur_vegetation.md)  <sub>OPT</sub>
    * Description: "Vegetation classification from one or more standard classification systems, or agricultural crop"
    * range: [TextValue](TextValue.md)
 * [cur_vegetation_meth](cur_vegetation_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in vegetation classification 
    * range: [TextValue](TextValue.md)
 * [diss_oxygen](diss_oxygen.md)  <sub>OPT</sub>
    * Description: Concentration of dissolved oxygen
    * range: [QuantityValue](QuantityValue.md)
 * [drainage_class](drainage_class.md)  <sub>OPT</sub>
    * Description: Drainage classification from a standard system such as the USDA system
    * range: [TextValue](TextValue.md)
 * [elev](elev.md)  <sub>OPT</sub>
    * Description: "Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit"
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (environment)
 * [env_package](env_package.md)  <sub>OPT</sub>
    * Description: "MIxS extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported"
    * range: [TextValue](TextValue.md)
    * in subsets: (mixs extension)
 * [extreme_event](extreme_event.md)  <sub>OPT</sub>
    * Description: Unusual physical events that may have affected microbial populations
    * range: [TimestampValue](TimestampValue.md)
 * [fao_class](fao_class.md)  <sub>OPT</sub>
    * Description: Soil classification from the FAO World Reference Database for Soil Resources. The list can be found at http://www.fao.org/nr/land/sols/soil/wrb-soil-maps/reference-groups
    * range: [TextValue](TextValue.md)
 * [fire](fire.md)  <sub>OPT</sub>
    * Description: Historical and/or physical evidence of fire
    * range: [TimestampValue](TimestampValue.md)
 * [flooding](flooding.md)  <sub>OPT</sub>
    * Description: Historical and/or physical evidence of flooding
    * range: [TimestampValue](TimestampValue.md)
 * [geo_loc_name](geo_loc_name.md)  <sub>OPT</sub>
    * Description: "The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (v 1.512) (http://purl.bioontology.org/ontology/GAZ)"
    * range: [TextValue](TextValue.md)
    * in subsets: (environment)
 * [geo_loc_name](geo_loc_name.md)  <sub>OPT</sub>
    * Description: "The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (v 1.512) (http://purl.bioontology.org/ontology/GAZ)"
    * range: [TextValue](TextValue.md)
    * in subsets: (environment)
 * [heavy_metals](heavy_metals.md)  <sub>OPT</sub>
    * Description: Heavy metals present and concentrationsany drug used by subject and the frequency of usage; can include multiple heavy metals and concentrations
    * range: [QuantityValue](QuantityValue.md)
 * [heavy_metals_meth](heavy_metals_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining heavy metals
    * range: [TextValue](TextValue.md)
 * [horizon](horizon.md)  <sub>OPT</sub>
    * Description: Specific layer in the land area which measures parallel to the soil surface and possesses physical characteristics which differ from the layers above and beneath
    * range: [TextValue](TextValue.md)
 * [horizon_meth](horizon_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining the horizon
    * range: [TextValue](TextValue.md)
 * [link_addit_analys](link_addit_analys.md)  <sub>OPT</sub>
    * Description: Link to additional analysis results performed on the sample
    * range: [TextValue](TextValue.md)
 * [link_class_info](link_class_info.md)  <sub>OPT</sub>
    * Description: Link to digitized soil maps or other soil classification information
    * range: [TextValue](TextValue.md)
 * [link_climate_info](link_climate_info.md)  <sub>OPT</sub>
    * Description: Link to climate resource
    * range: [TextValue](TextValue.md)
 * [local_class](local_class.md)  <sub>OPT</sub>
    * Description: Soil classification based on local soil classification system
    * range: [TextValue](TextValue.md)
 * [local_class_meth](local_class_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining the local soil classification 
    * range: [TextValue](TextValue.md)
 * [microbial_biomass](microbial_biomass.md)  <sub>OPT</sub>
    * Description: "The part of the organic matter in the soil that constitutes living microorganisms smaller than 5-10 micrometer. If you keep this, you would need to have correction factors used for conversion to the final units"
    * range: [QuantityValue](QuantityValue.md)
 * [microbial_biomass_meth](microbial_biomass_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining microbial biomass
    * range: [TextValue](TextValue.md)
 * [misc_param](misc_param.md)  <sub>OPT</sub>
    * Description: "Any other measurement performed or parameter collected, that is not listed here"
    * range: [QuantityValue](QuantityValue.md)
 * [nitrate](nitrate.md)  <sub>OPT</sub>
    * Description: Concentration of nitrate in the sample
    * range: [QuantityValue](QuantityValue.md)
 * [ph_meth](ph_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining ph
    * range: [TextValue](TextValue.md)
 * [pool_dna_extracts](pool_dna_extracts.md)  <sub>OPT</sub>
    * Description: "Indicate whether multiple DNA extractions were mixed. If the answer yes, the number of extracts that were pooled should be given"
    * range: [TextValue](TextValue.md)
 * [previous_land_use](previous_land_use.md)  <sub>OPT</sub>
    * Description: Previous land use and dates
    * range: [TextValue](TextValue.md)
 * [previous_land_use_meth](previous_land_use_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining previous land use and dates
    * range: [TextValue](TextValue.md)
 * [profile_position](profile_position.md)  <sub>OPT</sub>
    * Description: Cross-sectional position in the hillslope where sample was collected.sample area position in relation to surrounding areas
    * range: [TextValue](TextValue.md)
 * [salinity](salinity.md)  <sub>OPT</sub>
    * Description: "Salinity is the total concentration of all dissolved salts in a water sample. While salinity can be measured by a complete chemical analysis, this method is difficult and time consuming. More often, it is instead derived from the conductivity measurement. This is known as practical salinity. These derivations compare the specific conductance of the sample to a salinity standard such as seawater"
    * range: [QuantityValue](QuantityValue.md)
 * [salinity_meth](salinity_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining salinity
    * range: [TextValue](TextValue.md)
 * [samp_vol_we_dna_ext](samp_vol_we_dna_ext.md)  <sub>OPT</sub>
    * Description: "Volume (ml), weight (g) of processed sample, or surface area swabbed from sample for DNA extraction"
    * range: [QuantityValue](QuantityValue.md)
 * [season_precpt](season_precpt.md)  <sub>OPT</sub>
    * Description: "The average of all seasonal precipitation values known, or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps. "
    * range: [QuantityValue](QuantityValue.md)
 * [season_temp](season_temp.md)  <sub>OPT</sub>
    * Description: Mean seasonal temperature
    * range: [QuantityValue](QuantityValue.md)
 * [sieving](sieving.md)  <sub>OPT</sub>
    * Description: Collection design of pooled samples and/or sieve size and amount of sample sieved 
    * range: [QuantityValue](QuantityValue.md)
 * [slope_aspect](slope_aspect.md)  <sub>OPT</sub>
    * Description: "The direction a slope faces. While looking down a slope use a compass to record the direction you are facing (direction or degrees); e.g., nw or 315 degrees. This measure provides an indication of sun and wind exposure that will influence soil temperature and evapotranspiration."
    * range: [QuantityValue](QuantityValue.md)
 * [slope_gradient](slope_gradient.md)  <sub>OPT</sub>
    * Description: Commonly called 'slope'. The angle between ground surface and a horizontal line (in percent). This is the direction that overland water would flow. This measure is usually taken with a hand level meter or clinometer
    * range: [QuantityValue](QuantityValue.md)
 * [soil_type](soil_type.md)  <sub>OPT</sub>
    * Description: Soil series name or other lower-level classification
    * range: [TextValue](TextValue.md)
 * [soil_type_meth](soil_type_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining soil series name or other lower-level classification
    * range: [TextValue](TextValue.md)
 * [store_cond](store_cond.md)  <sub>OPT</sub>
    * Description: Explain how and for how long the soil sample was stored before DNA extraction
    * range: [TextValue](TextValue.md)
 * [texture](texture.md)  <sub>OPT</sub>
    * Description: "The relative proportion of different grain sizes of mineral particles in a soil, as described using a standard system; express as % sand (50 um to 2 mm), silt (2 um to 50 um), and clay (<2 um) with textural name (e.g., silty clay loam) optional."
    * range: [QuantityValue](QuantityValue.md)
 * [texture_meth](texture_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining soil texture
    * range: [TextValue](TextValue.md)
 * [tillage](tillage.md)  <sub>OPT</sub>
    * Description: Note method(s) used for tilling
    * range: [TextValue](TextValue.md)
 * [tot_nitro_content](tot_nitro_content.md)  <sub>OPT</sub>
    * Description: Total nitrogen content of the sample
    * range: [QuantityValue](QuantityValue.md)
 * [tot_nitro_content_meth](tot_nitro_content_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining the total nitrogen
    * range: [TextValue](TextValue.md)
 * [tot_org_c_meth](tot_org_c_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining total organic carbon
    * range: [TextValue](TextValue.md)
 * [tot_org_carb](tot_org_carb.md)  <sub>OPT</sub>
    * Description: "Definition for soil: total organic carbon content of the soil, definition otherwise: total organic carbon content"
    * range: [QuantityValue](QuantityValue.md)
 * [tot_org_carb](tot_org_carb.md)  <sub>OPT</sub>
    * Description: "Definition for soil: total organic carbon content of the soil, definition otherwise: total organic carbon content"
    * range: [QuantityValue](QuantityValue.md)
 * [water_content](water_content.md)  <sub>OPT</sub>
    * Description: Water content measurement
    * range: [QuantityValue](QuantityValue.md)
 * [water_content_soil_meth](water_content_soil_meth.md)  <sub>OPT</sub>
    * Description: Reference or method used in determining the water content of soil
    * range: [TextValue](TextValue.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)

### Inherited from study:

 * [ecosystem](ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_category](ecosystem_category.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_type](ecosystem_type.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_subtype](ecosystem_subtype.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [specific_ecosystem](specific_ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [principal investigator](principal_investigator.md)  <sub>OPT</sub>
    * Description: represents the PI
    * range: [PersonValue](PersonValue.md)
 * [doi](doi.md)  <sub>OPT</sub>
    * range: [AttributeValue](AttributeValue.md)
 * [study➞id](study_id.md)  <sub>REQ</sub>
    * Description: The primary identifier for the study.
    * range: [String](types/String.md)
 * [study➞name](study_name.md)  <sub>OPT</sub>
    * Description: A human readable name or description of the study.
    * range: [String](types/String.md)
 * [study➞alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * Description: The same study may have distinct identifiers in different databases (e.g. GOLD and EMSL)
    * range: [String](types/String.md)

### Domain for slot:

 * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * Description: The same biosample may have distinct identifiers in different databases (e.g. GOLD and EMSL)
    * range: [String](types/String.md)
 * [biosample➞depth](biosample_depth.md)  <sub>OPT</sub>
    * range: [QuantityValue](QuantityValue.md)
 * [biosample➞env_broad_scale](biosample_env_broad_scale.md)  <sub>REQ</sub>
    * Description: formerly known as 'biome'
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_local_scale](biosample_env_local_scale.md)  <sub>REQ</sub>
    * Description: formerly known as 'feature'
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_medium](biosample_env_medium.md)  <sub>REQ</sub>
    * Description: formerly known as 'material'
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞id](biosample_id.md)  <sub>REQ</sub>
    * Description: The primary identifier for the biosample. Example: GOLD:Gb0205609
    * range: [String](types/String.md)
 * [biosample➞lat_lon](biosample_lat_lon.md)  <sub>REQ</sub>
    * Description: This is currently a required field but it's not clear if this should be required for human hosts
    * range: [GeolocationValue](GeolocationValue.md)
 * [biosample➞name](biosample_name.md)  <sub>OPT</sub>
    * Description: A human readable name or description of the biosample
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sample |
|  | | material sample |
|  | | specimen |
|  | | biospecimen |
| **In Subsets:** | | sample subset |
| **Exact Mappings:** | | OBI:0000747 |
|  | | NCIT:C43412 |

