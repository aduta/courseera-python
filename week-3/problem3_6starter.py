# -problem3_6.py *- coding: utf-8 -*-

import sys

inf = open(sys.argv[1])
outf = open(sys.argv[2], 'w')

for line in inf:
  chars = len(line.strip('\n'))
  outf.write(str(chars) + '\n')

inf.close()
outf.close()

