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

'''
Dictionary-based representations of vectors: Setter and getter
Setter:
'''
def setitem(v, d, val): v.f[d] = val

'''
Second argument should be member of v.D.
Third argument should be an element of the field.
Example:
>>> setitem(v, ’B’, 2.)
'''


'''
Quiz: Write a procedure getitem(v, d) with the following spec:
input: an instance v of Vec, and an element d of the set v.D
output: the value of entry d of v
'''

def getitem(v, d) : return v.f[d] if d in v.f else 0

'''
Quiz: Write a procedure list2vec(L) with the following spec:
input: a list L of field elements
output: an instance v of Vec with domain {0, 1, 2, . . . , len(L)-1} such that
v[i] = L[i] for each integer i in the domain
'''
def list2vec(L) :
    return Vec(set{range(len(L))} , { k:x for k,x in emumerate(L)} )
    # return Vec(set{range(len(L))} , { k:L[k] for k in range(len(L))} )
