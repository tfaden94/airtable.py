import airtable
import json

with open('/Users/tyler.faden/Git/Local/ghost/airtable/config/config.json', 'r') as file:
    creds = json.load(file)

api_key = creds['API_KEY']
dp = creds['BASE']['deal_pipeline']

at = airtable.Airtable(dp, api_key)
#
at.get('TABLE_NAME')