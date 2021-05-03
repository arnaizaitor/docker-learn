import json
from pprint import *


with open('./sample_data.json') as json_file:
    data = json.load(json_file)

    pprint(data)