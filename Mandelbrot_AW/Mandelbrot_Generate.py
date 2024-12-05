import numpy as np
from .Mandelbrot_Continuous import MDB_MapRule_Continuous
from .Mandelbrot_Discrete import MDB_MapRule_Discrete


class MandelbrotSet:
    def __init__(self, max_iter, width, height, x_min, x_max, y_min, y_max, option):
        # Store the attributes needed to generate the Mandelbrot set
        """
        The Mandelbrot in your interesting attributes.
        Arguments:
        ----------
        max_iter: int
            The maximum number of iterations to perform for each point in the Mandelbrot set, relating to the display effect and the fineness of the plot.
        width: int
            The width of the plot in pixels.
        height: int
            The height of the plot in pixels.
        x_min: float
            The minimum value of the x-axis.
        x_max: float
            The maximum value of the x-axis.
        y_min: float
            The minimum value of the y-axis.
        y_max: float
            The maximum value of the y-axis.
        option: str
            The map option to use. Either "continuous" or "discrete".
        These arguments are basic attributes of the plot, relating to the display size and range of the plot.
        """
        self.max_iter = max_iter
        self.width = width
        self.height = height
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.image = None
        self.option = option

    def map(self, c, option):
        """
        The map from the initial 2D array to the Mandelbrot set:
        ----------
        Two options are available: "continuous" and "discrete".
        """
        match option:
            case "continuous":
                return MDB_MapRule_Continuous(c, self.max_iter)
            case "discrete":
                return MDB_MapRule_Discrete(c, self.max_iter)
            case _:
                raise TypeError(
                    "Invalid map option. Please choose either 'continuous' or 'discrete'."
                )

    def array_generate(self):
        """
        Assigning values to the initial 2D array.
        """
        real = np.linspace(self.x_min, self.x_max, self.width)
        imag = np.linspace(self.y_min, self.y_max, self.height)
        mandelbrot_set = np.zeros((self.height, self.width))
        for i in range(self.height):
            for j in range(self.width):
                c = complex(real[j], imag[i])
                mandelbrot_set[i, j] = self.map(c)
        return real, imag, mandelbrot_set
