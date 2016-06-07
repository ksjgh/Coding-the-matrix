class Vec:
    def __init__(self,labels,function):
        self.D = labels
        self.f = function

v=Vec({'A','B','C'},{'A':1.})

for d in v.D:
    if d in v.f:
        print(v.f[d])

def zero_vec(D) : return Vec(D,{})
# def zero_vec(D) : return Vec(D,{d:0 for d in D })
