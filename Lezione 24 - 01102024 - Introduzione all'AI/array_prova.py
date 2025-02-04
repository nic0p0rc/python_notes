import numpy as np

a = np.arange(10).reshape(1,2,5)
print(a)

b = np.arange(10, 20).reshape(1,2,5)
print(b)

c = np.concatenate((a,b), axis=0)
print()
#print("array c:",c)

c = np.concatenate((a,b), axis=1)
print()
#print("array c:",c)

c = np.concatenate((a,b), axis=2)
print()
#print("array c:",c)

print(a+b)
print(a*b)


