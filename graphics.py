import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

class Graphics:

    def __init__(self, line_frequency, dotsize, fontsize, annotate_shift):
        self.__line_frequency = line_frequency
        self.__dotsize = dotsize
        self.__fontsize = fontsize
        self.__annotate_shift = annotate_shift
    def __draw_grid(self, graph : plt.gca, x_range : tuple , y_range : tuple,
                    x_axis_name : str, y_axis_name : str):
        major_ticks = np.arange(*x_range)
        minor_ticks = np.arange(*y_range)
        graph.set_xticks(major_ticks)
        graph.set_xticks(minor_ticks, minor=True)
        graph.set_yticks(major_ticks)
        graph.set_yticks(minor_ticks, minor=True)
        graph.tick_params(axis='both', which='major', labelsize=10)
        graph.tick_params(axis='both', which='minor', labelsize=10)
        graph.grid(which='both')
        plt.xlabel(f'{x_axis_name}')
        plt.ylabel(f'{y_axis_name}')

    def __draw_axis(self, graph: plt.gca(), x_range : tuple, y_range : tuple):
        graph.set_xlim(*x_range)
        graph.set_ylim(*y_range)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

    def __draw_line(self, graph : plt.gca(), start_point : tuple, end_point : tuple,
                    style: str, width : int, color : str):
        x = np.linspace(start_point[0], end_point[0], self.__line_frequency)
        y = np.linspace(start_point[1], end_point[1], self.__line_frequency)
        graph.plot(x, y, linestyle=style, linewidth=width, color=color)

    def draw_nash_point(self, task1):
        nash_graph = plt.gca()
        nash_graph.set_aspect(1)
        self.__draw_grid(nash_graph, (-0.2, 1.2, 0.2), (-0.2, 1.2, 0.2),task1.q_sections[0][0],task1.p_sections[0][0])
        self.__draw_axis(nash_graph, (-0.2, 1.2), (-0.2, 1.2))

        #borders
        self.__draw_line(nash_graph, (0, 1), (1, 1), 'dashed', 2, 'black')
        self.__draw_line(nash_graph, (1, 0), (1, 1), 'dashed', 2, 'black')

        #GetValues
        q_keys = list(task1.q_sections[1].keys())
        q_values = list(task1.q_sections[1].values())

        p_keys = list(task1.p_sections[1].keys())
        p_values = list(task1.p_sections[1].values())

        #Q sections
        start_point = (q_keys[0], q_values[0][0])
        end_point = (q_keys[0], q_values[0][1])
        self.__draw_line(nash_graph, start_point, end_point, '-', 2, 'red')

        if task1.is_growing(task1.q_sections):
            start_point = (q_keys[0], q_values[0][1])
            end_point = (q_keys[1], q_values[1][0])
        else:
            start_point = (q_keys[0], q_values[0][0])
            end_point = (q_keys[1], q_values[1][1])

        self.__draw_line(nash_graph, start_point, end_point, '-', 2, 'red')

        start_point = (q_keys[1], q_values[1][0])
        end_point = (q_keys[1], q_values[1][1])
        self.__draw_line(nash_graph, start_point, end_point, '-', 2, 'red')

        #P sections
        start_point = (p_values[0][0], p_keys[0])
        end_point = (p_values[0][1], p_keys[0])
        self.__draw_line(nash_graph, start_point, end_point, '-', 2, 'blue')

        if task1.is_growing(task1.p_sections):
            start_point = (p_values[0][1], p_keys[0])
            end_point = (p_values[1][0], p_keys[1])
        else:
            start_point = (p_values[0][0], p_keys[0])
            end_point = (p_values[1][1], p_keys[1])

        self.__draw_line(nash_graph, start_point, end_point, '-', 2, 'blue')

        start_point = (p_values[1][0], p_keys[1])
        end_point = (p_values[1][1], p_keys[1])
        self.__draw_line(nash_graph, start_point, end_point, '-', 2, 'blue')

        #Nash points

        if task1.is_growing(task1.q_sections) and task1.is_growing(task1.p_sections):
            nash_graph.plot(0, 0, 'k.', markersize=self.__dotsize)
            nash_graph.annotate("M", xy=(0 + self.__annotate_shift[0] , 0 + self.__annotate_shift[1]),
                                fontsize=self.__fontsize)
            nash_graph.plot(1, 1, 'k.', markersize=self.__dotsize)
            nash_graph.annotate("O", xy=(1 + self.__annotate_shift[0], 1 + self.__annotate_shift[1]),
                                fontsize=self.__fontsize)

        elif (not task1.is_growing(task1.q_sections)) and (not task1.is_growing(task1.p_sections)):
            nash_graph.plot(0, 1, 'k.', markersize=self.__dotsize)
            nash_graph.annotate("M", xy=(0 + self.__annotate_shift[0] , 1 + self.__annotate_shift[1]),
                                fontsize=self.__fontsize)
            nash_graph.plot(1, 0, 'k.', markersize=self.__dotsize)
            nash_graph.annotate("O", xy=(1 + self.__annotate_shift[0], 0 + self.__annotate_shift[1]),
                                fontsize=self.__fontsize)

        nash_graph.plot(task1.p_turning_point, task1.q_turning_point, 'k.', markersize=self.__dotsize)
        nash_graph.annotate("N", xy=(task1.p_turning_point + self.__annotate_shift[0],
                                     task1.q_turning_point + self.__annotate_shift[1]),
                            fontsize=self.__fontsize)





