#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

def n_str( str_line, index ):
    num = str(str_line[index])
    return num[:-1]

f = open('/home/jastinog/Python/vk.res', 'r')

lines = f.readlines()
print(lines[0])

# mailName = sys.argv[1]
# if mailName == 'igor@evne.com.ua':
#     print(n_str(lines, 0))
# elif mailName == 'admin@evne.com.ua':
#     print(n_str(lines, 1))
# elif mailName == 'inflatable.syphax@gmail.com':
#     print(n_str(lines, 2))
# elif mailName == 'mcwinlin@mail.ru':
#     print(n_str(lines, 3))

f.close()