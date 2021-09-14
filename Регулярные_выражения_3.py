"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:
zabcz
zzxzz
"""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    ans=re.search(r'z...z', line)
    if ans is not None:
        print(line)
