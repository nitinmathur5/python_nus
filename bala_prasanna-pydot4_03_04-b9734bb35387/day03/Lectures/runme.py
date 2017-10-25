import json
response = {'name': 'stackup', 'url': 'www.stackup.sg'}
print json.dumps(response, indent=4, separators=(',', ': '))