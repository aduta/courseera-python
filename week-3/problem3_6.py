# -*- coding: utf-8 -*-

from sys import argv

inf = open(argv[1])
outf = open(argv[2], 'w')

for line in inf:
  chars = len(line.strip('\n'))
  outf.write(str(chars) + '\n')

inf.close()
outf.close()

