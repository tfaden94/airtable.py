import airtable

with open('/Users/tyler.faden/Git/Local/ghost/ghost_airtable/config/config.json', 'r')

at = airtable.Airtable('BASE_ID', 'API_KEY')
at.get('TABLE_NAME')