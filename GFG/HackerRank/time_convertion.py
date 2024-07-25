"""
 convert it to military (24-hour) time.
"""

import re

s = "12:05:45AM"  # 00:05:45
s1 = "07:05:45AM"

if re.search("AM", s):
    print(s)
else:
    ss = s.replace("PM", "")
    print(ss)
    sl = ss.split(":")
    con = int(sl[0]) + 12
    if con >= 24:
        con = 00
    print(str(con) + ":" + sl[1] + ":" + sl[2])

# else:
#     re_s = re.search("(\d+:\d+:\d+)", s)
#     ss = re_s.group()
#     sl = ss.split(":")
#     # print(type(ss))
#     print(sl[0])
#     se = int(sl[0]) + 12
#     # print(type(sl), type(ss[1]))
#     print(str(se) + ":" + sl[1] + ":" + sl[2])
