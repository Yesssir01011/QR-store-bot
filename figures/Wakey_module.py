
def taq_sany(a):
    b = 0
    for i in a:
        if i % 2 == 1:
            b += 1
    f = b
    return f

def jup_qos(b):
    l = 0
    for i in b:
        if i % 2 != 1:
            l += i
    r = l
    return r

from random import randint as rnd
def kezdeisoq_massiv(a):
    if a == 0:
        b = [rnd(5,100) for i in range(10)]
        return b

def arif_orta(a):
    b = sum(a)
    c = len(a)
    return b/c

def indecs(a):
    return len(a)//2

def ind_san(massiv):
    while sum(1 for x in massiv if x > arif_orta(massiv)):
        for i in massiv:
            if i > arif_orta(massiv):
                f = massiv.index(i)
                return f

