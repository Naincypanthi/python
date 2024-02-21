import numpy as np
#one dimensional array
list1=[20,30,40,50,60,70]
array1=np.array(list1)
array1.ndim
print(array1[0])            #indexing
print(array1[-1])

                               #menstion datatype (dtye="U32") character
print(array1)
print(type(list1))



#two dimensional array
list2=[[1,8,9],[9,4,5],[6,2,3]]
array2=np.array(list2)
print(array2)
print(type(list2))
array2.ndim
print(array2[0,2])
print(array2[1,1])
print(array2[:,1])
print(array2[:,0])


#range
array3=np.arange(11,17).reshape((2,3))
print(array3)



array4=np.zeros((4,3 ))
print(array4)

array5=np.ones((3,3))
print(array5)



