path = 'usagov.txt'

result = open(path).readline()

import json
records = [json.loads(line) for line in open(path,encoding="utf8")]
print(records[0])
print(records[0]['tz'])

time_zone = [record['tz'] for record in records if 'tz' in record and record['tz'] != '']
print(time_zone[:5])

from collections import defaultdict

def get_counts2(sequese):
    counts = defaultdict(int)
    for x in sequese:
        counts[x] += 1
    return counts

counts = get_counts2(time_zone)

print(counts['America/New_York'])

print(len(time_zone))

def top_counts(count_dict, n=5):
    value_key_pairs = [(count, tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

print(top_counts(counts))

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
frame = DataFrame(records)
print(frame['tz'][:10])

clean_tz = frame['tz'].fillna('Missing')
print(clean_tz[:10])
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
plt = tz_counts[:10].plot(kind='barh',rot=0)

results = Series(x.split()[0] for x in frame.a.dropna())
print(results[:5])
print(results.value_counts()[:5])

cframe = frame[frame.a.notnull()]
operation_system = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')
print(operation_system[:5])