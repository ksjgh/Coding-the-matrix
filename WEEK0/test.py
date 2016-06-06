def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [ p+i for i in range(n) ]

# print( row(10,4))
# print([ row(i,15) for i in range(20)])
print([ [ p+n for n in range(15)] for p in range(20)])
