import numpy as np

matrix1 = np.array([[4, 2, 0],
            [1, 3, 2],
            [-1, 3, 10]])

matrix2 = np.array([matrix1[1], matrix1[0], matrix1[2]])
print(matrix2)

matrix3 = np.array([matrix2[0], matrix2[1]+matrix2[0] * (-4), matrix2[2] + matrix2[0]])
print(matrix3)


