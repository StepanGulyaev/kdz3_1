
class task1:
    def __get_nash_coef_CD(self, matrix : list):
        return matrix[0][0] - matrix[0][1] - matrix[1][0] + matrix[1][1]

    def __get_nash_coef_alpha(self, matrix : list):
        return matrix[1][1] - matrix[0][1]

    def __get_nash_coef_beta(self, matrix : list):
        return matrix[1][1] - matrix[1][0]

    def __print_formula(self, CD : int, alphabeta : int, variable1 : str, variable2 : str):
        print(f'( {variable1} - 1 )( {CD}{variable2} - ({alphabeta}) ) >= 0')
        print(f'{variable1}( {CD}{variable2} - ({alphabeta}) ) >= 0')

    def __get_pq_sections(self, CD : int, alphabeta : int, variable1 : str, variable2 : str):
        pq = []
        variable = round(alphabeta / CD, 3)

        for i in range(2):
            if CD >= 0:
                if (i - 1) * ((variable + 0.001) * CD - alphabeta) >= 0: symbol = ">="
                else: symbol = "<="
            else:
                if (i - 1) * ((variable - 0.001) * CD - alphabeta) >= 0: symbol = "<="
                else: symbol = ">="
            dict = {f'{variable1} = {i}' : [variable2, symbol, variable]}
            pq.append(dict)
        dict = {f'0 < {variable1} < 1' : [ variable2,"=", variable]}
        pq.append(dict)
        return pq

    def __print_pq_sections(self,pq_sections : list):
        for i in range(len(pq_sections)):
            print(f'{" ".join(map(str,list(pq_sections[i].keys())))}, {" ".join(map(str,list(pq_sections[i].values())[0]))}')


    def getNashPoint(self, A : list, B : list):
        C = self.__get_nash_coef_CD(A)
        alpha = self.__get_nash_coef_alpha(A)

        D = self.__get_nash_coef_CD(B)
        beta = self.__get_nash_coef_beta(B)

        print()
        print("Для матрицы А:")
        self.__print_formula(C,alpha,"p","q")
        print()
        print("Для матрицы B:")
        self.__print_formula(D,beta, "q", "p")
        print()

        q_sectinos = self.__get_pq_sections(C,alpha,"p","q")
        p_sections = self.__get_pq_sections(D,beta, "q","p")

        print("Промежутки для p: ")
        self.__print_pq_sections(q_sectinos)
        print()
        print("Промежутки для q: ")
        self.__print_pq_sections(p_sections)
        print()



