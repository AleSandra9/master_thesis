import matplotlib.pyplot as plt
from matplotlib import cycler
import matplotlib as mpl

from typing import Tuple, List, NoReturn


class DefaultStyle:

    """
    Class the sets the defaults plotting style used in the course
    """

    def __init__(self, plot_size: Tuple[float, float] = (12, 6), font_size: float = 15.0):

        """
        Spills plot style into memory upon instantiation

        Parameters
        ----------
        plot_size:
        The size of the figure as (height, width)
        font_size:
        The size of the font on the plot as as float
        """

        self.colors = list(default_colors.values())
        self.figsize = plot_size
        self.font_size = font_size
        self.legend = True
        self._font = 'Arial'
        self._face_color = 'white'
        self._edge_color = 'white'
        self._grid_color = '#dddddd'
        self._tick_color = '.15'
        self._line_style = '--'
        self._line_width = 2.0
        self._tick_dir = 'out'
        self.save_format = 'pdf'
        self._spill()

    def _spill(self) -> NoReturn:

        """
        Spills rcParams into global memory

        Returns
        -------
        None
        """
        colors = cycler(color=self.colors)
        plt.rc('axes', facecolor=self._face_color, axisbelow=True, grid=True, prop_cycle=colors, autolimit_mode='data',
               xmargin=0, ymargin=0)
        plt.rc('grid', color=self._grid_color, linestyle=self._line_style)
        plt.rc('xtick', direction=self._tick_dir, color=self._tick_color)
        plt.rc('ytick', direction=self._tick_dir, color=self._tick_color)
        plt.rc('patch', edgecolor=self._edge_color)
        plt.rc('lines', linewidth=self._line_width)
        plt.rc('font', family='Arial', size=self.font_size)
        plt.rc('legend', loc='best', fontsize=self.font_size, fancybox=True, shadow=False)
        plt.rc('savefig', format=self.save_format)


"""
Default colors
"""

color_map = plt.cm.get_cmap('tab20c')

default_colors = dict()
default_colors['purple'] = '#AC72F0'
default_colors['green'] = '#00CF83'
default_colors['orange'] = '#F5863B'
default_colors['blue'] = '#1F77FA'
default_colors['dark_blue'] = '#014D7A'
default_colors['light_blue'] = '#5CC6FF'
default_colors['gray'] = '#ebf4f6'


default_colors['red'] = '#EB1933'
default_colors['dark_purple'] = '#7B00FF'
default_colors['pink'] = '#EB47C3'
default_colors['cyan'] = '#0ADDEB'
default_colors['yellow'] = '#F5C000'
default_colors['dark_green'] = '#00B390'
default_colors['dark_orange'] = '#F53D02'
default_colors['dark_red'] = '#B90109'


