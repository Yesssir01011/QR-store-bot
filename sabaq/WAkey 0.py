#2)
import math
# cosπ
cosin = math.cos(math.pi)
print("cosπ мәні:",cosin)
#3)
from datetime import datetime
ddt = datetime.now().time()
print(ddt)
#4
from random import randint as rnd
from random import choice as chc
a = 5
b = 20
Li = [rnd(a,b) for i in range(5)]
print(Li)
print(chc(Li))




