import csv
import sys

import nilsimsa

import cnilsimsa

if sys.argv[1] == 'py':
    comp = nilsimsa.compare_hexdigests
elif sys.argv[1] == 'c':
    comp = cnilsimsa.compare_hexdigests
else:
    print 'py or c?'
    sys.exit(1)

with open('tests/hashes.csv') as hashes_file:
    hashes_csv = list(csv.reader(hashes_file))

for _ in range(100):
    for digest1, digest2 in hashes_csv:
        comp(digest1, digest2)
