from task1 import *
from graphics import *

A = [[5,3],
     [3,8]]

B = [[5,15],
     [20,5]]


def print_matrix(matrix : list):
     for row in matrix:
          print(' '.join(map(str, row)))

if __name__ == '__main__':
     graphics1 = Graphics(30, 12, 20, (-0.1, 0.05))

     print("Матрица игрока А:",end="\n\n")
     print_matrix(A)
     print()

     print("Матрица игрока B:",end="\n\n")
     print_matrix(B)
     print()

     print("1. Найти равновесное по Нэшу решение графо-аналитическим методом")
     task1 = Task1()
     task1.getNashPoint(A, B)
     graphics1.draw_nash_point(task1)

     print("2. Построить множество Парето-оптимальных решений")
     graphics2 = Graphics(30, 12, 20, (-1.3, 0.5))
     graphics2.draw_pareto(A,B)

     plt.show()


