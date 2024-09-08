import os
import json
from dotenv import load_dotenv

load_dotenv()

from pyairtable import Api

def create_table():
    api = Api(os.environ['AIRTABLE_TOKEN'])
    x = os.environ['AIRTABLE_X']
    y = os.environ['AIRTABLE_Y']
    table = api.table(x, y)
    print()
    # Write the formatted JSON to a file
    with open('output.json', 'w') as file:
        file.write(json.dumps(table.all(),indent=4))
    
