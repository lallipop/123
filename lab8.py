import lab9
from lab9 import Matrix
 
A = Matrix(3, 3)
B = Matrix(3, 3)
C = A + B
D = A - B
E = A * 2
F = A * B
print('Матрица А = ')
A.outMat()
print('Матрица В = ')
B.outMat()
print('C = A + B: ')
if C != 1:
    C.outMat()
else:
    print('Матрицы разных размеров!')
print('D = A - B: ')
if D != 1:
    D.outMat()
else:
    print('Матрицы разных размеров!')
print('E = A * 2: ')
E.outMat()
print('F = A * B: ')
if F != 1:
    F.outMat()
else:
    print('Матрицы разных размеров!')
print('Определитель матрицы А: ')
A.determinant()
print('Матрица А транспонированная: ')
A.transporate()
A.outMat()
input("\n\nНажмите Enter чтобы выйти ...")