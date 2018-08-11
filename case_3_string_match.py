#!/usr/bin/python

import re

match = re.match('/(.*)/(.*)', '/usr/home/lumberjack')
print(match.groups())
