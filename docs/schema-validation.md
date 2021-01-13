# Validating json objects against the NMDC schema

This document assumes knowledge of
[JSON](https://www.json.org/json-en.html). It also assumes rudimentary
familiarity with [JSON-Schema](https://json-schema.org/) but don't
worry if you are not an expert on this.

We can conceive of validation of a piece of JSON at two levels

 1. The JSON should be syntactically correct JSON
 2. The JSON should conform to the NMDC schema

## Syntactically correct JSON

It is crucial that the JSON is syntactically valid, otherwise it can't even be schema-validated.

There are a varoety of ways to check for this. We recommend using jsonschema to validate this, see below.

NOTE: all NMDC JSON-producing tools, libraries, or scripts SHOULD use a standard json library. If you are using a robust standard json library, your output is practically guaranteed to be syntactically valid JSON.

It is strongly recommended that you do NOT generate JSON by methods such as directly manipulating json strings or printing directly. This is guaranteed to be fragile/non-robust. Even if your code works now, it is certain it will fail later and produce incorrect JSON.

For Python, there is only one choice:

https://docs.python.org/3/library/json.html

If you are not using this, you should

## Schema validation

The JSON-Schema for NMDC is maintained in this github repo, under [../schema/nmdc.schema.json](schema/nmdc.schema.json)

Note that the JSON-Schema is generated from a higher level YAML
representation, using a modeling framework called linkML. See the
README for details. For understanding the schema, you may be better
looking at the auto-generated docs. However, for computational
conformance, the JSON-Schema is what is should be used.

There are a variety of json schema validators, these will give the same results. There are web playgrounds for this. But for simplicity we recommend the Python [jsonschema package](https://pypi.org/project/jsonschema/)

To install:

```bash
pip install jsonschema
```

Assume you have a file MYFILE that is json intended to conform

```bash
jsonschema -i /PATH/TO/MYFILE.json schema/nmdc.schema.json
```

If the json is valid, there will be no output and the script will pass. If there are problems these will be reported.

You can try this with some ready-made examples in this repo:

```bash
jsonschema -i examples/nmdc-01.json schema/nmdc.schema.json
```

You can also use the jsonschema library to validate directly from within your python.

# What to do if your JSON does not validate

There are 3 possibilities:

 1. Your json is good, and the schema needs to be extended or modified to account
 2. you need to modify the json to conform
 3. some other odd bug somewhere

For 1, you can go right ahead and make PR on the schema yaml. However,
if you are not confortable doing this then you can get help from one
of the schema developers. We recommend filing a new ticket explaining the issue.

For 2, this is upon you to fix this. If you need help explaining part of the schema then 

# NMDC Producer SOP

It is expected that different providers of JSON within the NMDC take
responsibility for validating their JSON. Aim1 can help with any
problems.

Currently not all providers of information to NMDC provide JSON - for
example, GOLD is provided as database dumps, and an ETL process
transforms this into JSON. In future we would like to move towards a
situation where all information is provided as JSON.
