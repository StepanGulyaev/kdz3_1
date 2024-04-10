class Task1:

    def __init__(self):
        self.p_sections = []
        self.q_sections = []
        self.p_turning_point = None
        self.q_turning_point = None
        self.nash_balance_points = []

    def __get_nash_coef_CD(self, matrix : list):
        return matrix[0][0] - matrix[0][1] - matrix[1][0] + matrix[1][1]

    def __get_nash_coef_alpha(self, matrix : list):
        return matrix[1][1] - matrix[0][1]

    def __get_nash_coef_beta(self, matrix : list):
        return matrix[1][1] - matrix[1][0]

    def __print_formula(self, CD : int, alphabeta : int, variable1 : str, variable2 : str):
        print(f'( {variable1} - 1 )( {CD}{variable2} - ({alphabeta}) ) >= 0')
        print(f'{variable1}( {CD}{variable2} - ({alphabeta}) ) >= 0')

    def is_growing(self, pq_sections : list):
        values = list(pq_sections[1].values())
        if values[0][1] == values[1][0]: return True
        else: False

    def __get_pq_sections(self, CD: int, alphabeta: int, variable1: str, variable2: str):
        pq = [[variable1, variable2]]
        pq_value = round(alphabeta / CD, 3)

        if CD >= 0:
            segments = {0: [0, pq_value], 1: [pq_value, 1]}
        else:
            segments = {0: [pq_value, 1], 1: [0, pq_value]}
        pq.append(segments)
        return pq

    def __print_pq_sections(self,pq_sections : list):
        keys = list(pq_sections[1].keys())
        values = list(pq_sections[1].values())
        pq_value = list(set(values[0]).intersection(values[1]))[0]
        for i in range(2):
            print(f'{pq_sections[0][0]} = {keys[i]}, '
                  f'{pq_sections[0][1]} ∈ {values[i]}')
        print(f'{pq_sections[0][0]} ∈ (0,1), '
              f'{pq_sections[0][1]} = {pq_value}')


    def get_turning_point(self, pq_sections : list):
        values = list(pq_sections[1].values())
        return list(set(values[0]).intersection(values[1]))[0]

    def getNashPoint(self, A : list, B : list):
        C = self.__get_nash_coef_CD(A)
        alpha = self.__get_nash_coef_alpha(A)

        D = self.__get_nash_coef_CD(B)
        beta = self.__get_nash_coef_beta(B)

        print()
        print("Для матрицы А:")
        self.__print_formula(C, alpha, "p", "q")
        print()
        print("Для матрицы B:")
        self.__print_formula(D, beta, "q", "p")
        print()

        self.q_sections = self.__get_pq_sections(C, alpha, "p", "q")
        self.p_sections = self.__get_pq_sections(D, beta, "q", "p")

        print("Промежутки для p: ")
        self.__print_pq_sections(self.q_sections)
        print()
        print("Промежутки для q: ")
        self.__print_pq_sections(self.p_sections)
        print()

        self.p_turning_point = self.get_turning_point(self.p_sections)
        self.q_turning_point = self.get_turning_point(self.q_sections)

        if self.is_growing(self.q_sections) and self.is_growing(self.p_sections):
            self.nash_balance_points.append((0, 0))
            self.nash_balance_points.append((1, 1))

        self.nash_balance_points.append((self.p_turning_point, self.q_turning_point))

        if (not self.is_growing(self.q_sections)) and (not self.is_growing(self.p_sections)):
            self.nash_balance_points.append((0, 1))
            self.nash_balance_points.append((1, 0))

        print("Точки равновесия по Нэшу:")
        print(",".join(map(str,self.nash_balance_points)))