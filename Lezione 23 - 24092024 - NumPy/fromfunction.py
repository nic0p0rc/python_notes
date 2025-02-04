import numpy as np

def myfunc(i):
    print(type(i))
    print('i=',i)
    return (i>=5)*(1**2)+(1<5)*(1)

def myfunc1(i,j):
    print('i=',i)
    print('j=',j)
    return (i>=3)*(1**j)+(1<3)*(1)

def main():
    myarray = np.fromfunction(myfunc, (16,), dtype=np.int32)
    print(f'myarray = {myarray}')
    myarray1 = np.fromfunction(myfunc1, (5,5))
    print(f'myarray1 0 {myarray1}')

if __name__ == "__main__":
    main()