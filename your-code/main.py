#1. Import the NUMPY package under the name np.
import numpy as np



#2. Print the NUMPY version and the configuration.
print(np.version.version)

"""
1.20.1
"""
#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random((2,3,5))



#4. Print a.
print(a)

#array([[[0.32516645, 0.25739206, 0.13371283, 0.8217491 , 0.34506912],
#        [0.88221921, 0.01113987, 0.01675822, 0.4374189 , 0.22344315],
#        [0.94142291, 0.61732752, 0.80126355, 0.26467524, 0.16051862]],

#       [[0.17901407, 0.03302833, 0.01623576, 0.26030806, 0.44340774],
#        [0.57211398, 0.23553058, 0.37648599, 0.5308043 , 0.03784586],
#        [0.28114436, 0.98570996, 0.19864552, 0.33261179, 0.53832672]]])

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))


#6. Print b.
print(b)

#array([[[1., 1., 1.],
#        [1., 1., 1.]],
#
#       [[1., 1., 1.],
#        [1., 1., 1.]],
#
#       [[1., 1., 1.],
#        [1., 1., 1.]],
#
#       [[1., 1., 1.],
#        [1., 1., 1.]],
#
#       [[1., 1., 1.],
#        [1., 1., 1.]]])

#7. Do a and b have the same size? How do you prove that in Python code?
"""Tienen el mismo tamano"""

a.size == b.size
True

#8. Are you able to add a and b? Why or why not?

"""No se pueden sumar porque no tienen la misma dimensión"""
a.shape == b.shape
False

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = np.reshape(b, (2,3,5))

#array([[[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]],
#
#       [[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]]])


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = a+c
"""Porque ya son de las mismas dimensiones"""
#array([[[1.32516645, 1.25739206, 1.13371283, 1.8217491 , 1.34506912],
#        [1.88221921, 1.01113987, 1.01675822, 1.4374189 , 1.22344315],
#        [1.94142291, 1.61732752, 1.80126355, 1.26467524, 1.16051862]],
#
#       [[1.17901407, 1.03302833, 1.01623576, 1.26030806, 1.44340774],
#        [1.57211398, 1.23553058, 1.37648599, 1.5308043 , 1.03784586],
#        [1.28114436, 1.98570996, 1.19864552, 1.33261179, 1.53832672]]])

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(d)
"""Los valores de 'a' son floats y los valores de 'd' es la suma de 'c', que eran numeros integrales, y 'a'"""

"""[[[0.32516645 0.25739206 0.13371283 0.8217491  0.34506912]
  [0.88221921 0.01113987 0.01675822 0.4374189  0.22344315]
  [0.94142291 0.61732752 0.80126355 0.26467524 0.16051862]]

 [[0.17901407 0.03302833 0.01623576 0.26030806 0.44340774]
  [0.57211398 0.23553058 0.37648599 0.5308043  0.03784586]
  [0.28114436 0.98570996 0.19864552 0.33261179 0.53832672]]]
[[[1.32516645 1.25739206 1.13371283 1.8217491  1.34506912]
  [1.88221921 1.01113987 1.01675822 1.4374189  1.22344315]
  [1.94142291 1.61732752 1.80126355 1.26467524 1.16051862]]

 [[1.17901407 1.03302833 1.01623576 1.26030806 1.44340774]
  [1.57211398 1.23553058 1.37648599 1.5308043  1.03784586]
  [1.28114436 1.98570996 1.19864552 1.33261179 1.53832672]]]"""


#12. Multiply a and c. Assign the result to e.
"""e = a*c
array([[[0.32516645, 0.25739206, 0.13371283, 0.8217491 , 0.34506912],
        [0.88221921, 0.01113987, 0.01675822, 0.4374189 , 0.22344315],
        [0.94142291, 0.61732752, 0.80126355, 0.26467524, 0.16051862]],

       [[0.17901407, 0.03302833, 0.01623576, 0.26030806, 0.44340774],
        [0.57211398, 0.23553058, 0.37648599, 0.5308043 , 0.03784586],
        [0.28114436, 0.98570996, 0.19864552, 0.33261179, 0.53832672]]])"""

#13. Does e equal to a? Why or why not?
"""Si es equivalente 'a' a 'e' porque solo se multipica por valores de '1'"""
"""a == e
array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])"""


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
"""d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print("El valor maximo de 'd' es: ", d_max)
print("El valor minimo de 'd' es: ", d_min)
print("El promedio de 'd' es: ", d_mean)

El valor maximo de 'd' es:  1.985709958963862
El valor minimo de 'd' es:  1.0111398728175631
El promedio de 'd' es:  1.3753496597641226"""

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
"""f = np.empty((2,3,5))"""



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
"""f = np.where(d == d_min, 0,
            np.where((d > d_min) & (d < d_mean), 25,
                    np.where(d == d_mean, 50,
                            np.where((d > d_mean) & (d < d_max), 75, 100)
                            )
                    )
            ) """



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
"""array([[[1.32516645, 1.25739206, 1.13371283, 1.8217491 , 1.34506912],
        [1.88221921, 1.01113987, 1.01675822, 1.4374189 , 1.22344315],
        [1.94142291, 1.61732752, 1.80126355, 1.26467524, 1.16051862]],

       [[1.17901407, 1.03302833, 1.01623576, 1.26030806, 1.44340774],
        [1.57211398, 1.23553058, 1.37648599, 1.5308043 , 1.03784586],
        [1.28114436, 1.98570996, 1.19864552, 1.33261179, 1.53832672]]])"""

"""array([[[ 25,  25,  25,  75,  25],
        [ 75,   0,  25,  75,  25],
        [ 75,  75,  75,  25,  25]],

       [[ 25,  25,  25,  25,  75],
        [ 75,  25,  75,  75,  25],
        [ 25, 100,  25,  25,  75]]])"""

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
"""
h = np.empty((2,3,5), dtype="O")
for ind, sub_arr in enumerate(d):

    for ind_sub, sub_sub_arr in enumerate(sub_arr):

        for ind_sub_sub, element in enumerate(sub_sub_arr):

            if element == d_min:
                h[ind][ind_sub][ind_sub_sub] = 'A'
            elif element > d_min and element < d_mean:
                h[ind][ind_sub][ind_sub_sub] = 'B'
            elif element == d_mean:
                h[ind][ind_sub][ind_sub_sub] = 'C'
            elif element > d_mean and element < d_max:
                h[ind][ind_sub][ind_sub_sub] = 'D'
            else:
                h[ind][ind_sub][ind_sub_sub] = 'E'"""


"""array([[['B', 'B', 'B', 'D', 'B'],
        ['D', 'A', 'B', 'D', 'B'],
        ['D', 'D', 'D', 'B', 'B']],

       [['B', 'B', 'B', 'B', 'D'],
        ['D', 'B', 'D', 'D', 'B'],
        ['B', 'E', 'B', 'B', 'D']]], dtype=object)"""
