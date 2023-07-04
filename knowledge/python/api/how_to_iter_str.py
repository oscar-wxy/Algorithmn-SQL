a = "sdf"

for c in a:
    print(c)
"""
output:
s
d
f
"""

for i in enumerate(a):
    print(i)
"""
output:
(0, 's')
(1, 'd')
(2, 'f')
"""

for i in iter(a):
    print(i)
"""
s
d
f
"""