#-*- coding: UTF-8 -*-

import urllib



s = "测试"

print urllib.urlencode(s)
print(repr(s))

# \'c8\'d5\'c6\'da\lang2052\f2\'c8\'d5\'c6\'da\

#u'\xb2\xe2\xca\xd4'