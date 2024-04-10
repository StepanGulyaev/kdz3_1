import random
import numpy as np
from point import Point
from prettytable import PrettyTable
class Task2:

    def __init__(self,num_of_random_pq_points, A : list, B : list):
        self.A = A
        self.B = B
        self.num_of_random_pq_points = num_of_random_pq_points
        self.pq_points = []
        self.fpq_points = []
        self.pareto_points = []

    def gen_random_pq_points(self):
        for i in range(self.num_of_random_pq_points):
            point = Point(random.random(), random.random(), i)
            self.pq_points.append(point)

    def __calculate_fpq(self, p : float, matrix : list, q : float):
        p = np.array([p, 1 - p])
        q = np.array([q, 1 - q]).transpose()
        np_matrix = np.array(matrix)
        fpq = (p.dot(np_matrix)).dot(q)
        return fpq

    def get_fpq_points(self):
        for point in self.pq_points:
            fpqA = self.__calculate_fpq(point.x, self.A, point.y)
            fpqB = self.__calculate_fpq(point.x, self.B, point.y)
            fpq_point = Point(fpqA,fpqB,point.name)
            self.fpq_points.append(fpq_point)

    def get_pareto_points(self):
        for point in self.fpq_points:
            for point1 in self.fpq_points:
                if (point.x >= point1.x and point.y >= point1.y) and not \
                    (point.x == point1.x and point.y == point1.y):
                    point1.is_excluded = True

        for point in self.fpq_points:
            if not point.is_excluded:
                point.is_pareto = True
                self.pareto_points.append(point)

    def show_pareto(self):
        pareto_table = PrettyTable()
        pareto_table.field_names = ["№", "fa(p,q)", "fb(p,q)"]
        for point in self.pareto_points:
            pareto_table.add_row([point.name + 1, point.x, point.y])
        print(pareto_table)






