#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from datetime import datetime

from temp_sensor import TMP117
from multimeter import *

short_sensor = TMP117(0x48)
long_sensor = TMP117(0x49)

bench_2001 = K2001(16)
bench_7081 = S7081(2)

with open('5700A-10V.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Time','Short Temp Sensor', 'Long Temp Sensor', 'K2001', 'S7081'])
    while True:
        writer.writerow([datetime.now(), short_sensor.read(), long_sensor.read(), bench_2001.read(), bench_7081.read()])