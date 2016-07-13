#!/usr/bin/env python

import re
import os

__HERE = os.path.dirname(os.path.abspath(__file__))

SAMPLES = {}

for year, energy in ((11, 7), (12, 8), (14, 13), (15, 13)):
    SAMPLES[year] = {}
    with open(os.path.join(__HERE, '%dTeV.txt' % energy)) as f:
        for line in f:
            line = line.strip()
            if line:
                if (line[0]).isdigit():
                    line = line.split()
                    sampleid = int(line[0])
                    nevt = -9999
                    if energy == 13:
                        xsec, kfact, effic = float(line[2]), float(line[3]), float(line[4])
                    else:
                        xsec, kfact, effic = map(float, line[2].split('*'))
                    if sampleid not in SAMPLES[year]:
                        SAMPLES[year][sampleid] = {}
                    else:
                        raise ValueError("duplicate sample {0} in {1}".format(line, f.name))
                    SAMPLES[year][sampleid]['lephad'] = {'xsec': xsec, 'effic': effic, 'kfact': kfact, 'nevt': nevt}
#                    print year, sampleid, xsec, kfact, effic

def xsec_kfact_effic(year, id):
    year %= 1000
    info = SAMPLES[year][id]['lephad']
    return info['xsec'], info['kfact'], info['effic']

def nevts(year, id):
    year %= 1000
    info = SAMPLES[year][id]['lephad']
    return info['nevt']
