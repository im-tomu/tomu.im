#!/usr/bin/env python3

import csv
import json
import os.path
import pprint
import urllib.request


def replicate(l):
    l = list(l)
    for i in range(1,len(l)):
        if not l[i]:
            l[i] = l[i-1]
    return l


def convert(l):
    o = []
    for v in l:
        if v.endswith(' MHz'):
            v = v[:-4]
        if v.endswith(' kbytes'):
            v = v[:-7]
        v = v.replace(',','')

        if v == 'No':
            v = 'No' #False
        elif v == 'Yes':
            v = 'Yes' #True
        else:
            try:
                v = float(v)
            except ValueError:
                pass
        o.append(v)
    return o


def replace_many(s, chars, r):
    for c in chars:
        s = s.replace(c, r)
    return s


def get_header(l):
    if ''.join(str(x) for x in l[1:]) == '':
        return l[0], []
    return l[0], l[1:]


fn = 'google-sheet-specs.csv'
if not os.path.exists(fn):
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ0Q0UsybzAMzOaggp6ruzJmRF_6L4GlOxd5wZ1YcuY3jIXkPh6YAUBHusOgEOkmYsZOESZ3g51_TjT/pub?output=csv'
    with open(fn, 'wb') as f:
        f.write(urllib.request.urlopen(url).read())

response = open(fn, 'r')
data = [x for x in csv.reader(response)]
names = data.pop(0)
assert names[0] in ('Name', '')
names = replicate(names)

variants = data.pop(0)
assert variants[0] in ('Variant', '')
variants = replicate(variants)

_, parts = get_header(list(zip(names, variants)))
parts_name = ['{}-{}'.format(n.lower(), v.lower().replace(' ', '-')).replace('-?','') for n, v in parts]

row_data = []
row_data.append((('','name'), names[1:]))
row_data.append((('','variant'), variants[1:]))

section = ''
for line in data:
    header, rd = get_header(line)
    if not rd:
        section = header
        continue
    rd = replicate(rd)
    rd = convert(rd)
    row_data.append(([section, header], rd))

print('-'*50)
print(parts_name)
pprint.pprint(row_data)
print('-'*50)

output_data = {}
for pn in parts_name:
    output_data[pn] = {}

for (s, n), d in row_data:
    if s:
        n = '%s_%s' % (s, n)
    n = replace_many(n.lower(), ' -/', '_')
    for pn, v in zip(parts_name, d):
        output_data[pn][n] = v

del output_data['?omu']
pprint.pprint(output_data)
with open('specs.json', 'w') as f:
    json.dump(output_data, f, sort_keys=True, indent=2)
