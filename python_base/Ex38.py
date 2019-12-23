import numpy

A = numpy.array([[3, 2], [3, 4], [9, 6]])
B = numpy.array([[3, 1, 2], [3, 6, 4]])
C = numpy.dot(A, B)
print("A:\n", A)
print("B:\n", B)
print("A×B:\n", C)
