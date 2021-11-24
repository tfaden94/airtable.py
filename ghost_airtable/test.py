import airtable
import json

with open('/Users/tyler.faden/Git/Local/ghost/ghost_airtable/config/config.json', 'r') as file:
    creds = json.load(file)


api_key = creds['API_KEY']
base = creds['BASE']
dp = base['Deal Pipeline']

at = airtable.Airtable(dp, api_key)

test = at.get('SALES DEALS (SELLER SIDE)')
for i in test['records']:
    print(i)