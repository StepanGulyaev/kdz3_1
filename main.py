from task1 import *

#A = [[5,3],
     #[3,8]]

#B = [[5,15],
     #[20,5]]

A = [[6,3],
     [3,9]]

B = [[5,15],
     [20,5]]

def print_matrix(matrix : list):
     for row in matrix:
          print(' '.join(map(str, row)))

if __name__ == '__main__':
     print("Матрица игрока А:",end="\n\n")
     print_matrix(A)
     print()

     print("Матрица игрока B:",end="\n\n")
     print_matrix(B)
     print()
     
     print("1. Найти равновесное по Нэшу решение графо-аналитическим методом")
     task1 = task1()
     task1.getNashPoint(A, B)
