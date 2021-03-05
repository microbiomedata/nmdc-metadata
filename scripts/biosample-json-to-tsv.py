import click
import json
import pandas as pd

@click.command()
@click.argument('jsonfile')
def convert(jsonfile):
    """convert nmdc schema json to flat tsv"""
    obj = json.load(open(jsonfile))
    biosamples = obj['biosample_set']
    items = []
    for s in biosamples:
        item = {
            'id': s['id'],
            'name': s['name']
        }
        for k,v in s.items():
            if 'has_raw_value' in v:
                item[k] = v['has_raw_value']
        items.append(item)
    df = pd.DataFrame(items)
    print(df.to_csv(sep='\t', index=False))

if __name__ == '__main__':
    convert()
