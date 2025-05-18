import array
arr1=array.array('i')
print(arr1)
print(type(arr1))

arr2=array.array('i',[1,2,3,4])
print(arr2)

import numpy as np
n_arr1=np.array([],dtype=int)
print(type(n_arr1))
n_arr=np.array([1,3,5,7])
print(n_arr)
print(type(n_arr))