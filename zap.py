path = 'usagov.txt'

result = open(path).readline()
print(result)

import json
records = [json.loads(line) for line in open(path,encoding="utf8")]
print(records[0])
print(records[0]['tz'])

time_zone = [record['tz'] for record in records if 'tz' in record and record['tz'] != '']
print(time_zone[:5])
