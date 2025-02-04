import numpy as np

mioarr = np.arange(2,30,2)
print(mioarr)

mioarr2 = np.arange(1,31)
print(mioarr2)
print(mioarr2.ndim)

mioarr3 = np.zeros((1,31))
print(mioarr3)

mioarr4 = np.ones((2,3,5), dtype=np.int32) #2 matrici 3colonne 5 numeri
print(mioarr4)
print(mioarr4.ndim)
print(mioarr4.nbytes)
print(mioarr4.itemsize)
print(mioarr4.dtype)
print(mioarr4.size)
print(mioarr4.data)
print(mioarr4.shape)

mioarr5 = np.linspace(1,10, 9)
print(mioarr5)
print(mioarr5.nbytes)