import numpy as np
def taq_sandar(a):
    c = 0
    for i in a:
        if i % 2 == 1:
            c = i
        return np.array(c)
