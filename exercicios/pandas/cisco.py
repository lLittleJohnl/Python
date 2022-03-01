dct = {'one':'two', 'three':'one', 'two':'three'}
v = dct["three"]
for k in range(len(dct)):
    v = dct[v]
print(v)