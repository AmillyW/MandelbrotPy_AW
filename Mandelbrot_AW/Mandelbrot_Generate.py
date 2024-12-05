class Mandelbrot_Attributes:
    def __init__(self, width, height, x_min, x_max, y_min, y_max):
        # Store the attributes needed to generate the Mandelbrot set
        """
        The Mandelbrot in your interesting attributes.
        ----------
        These arguments are basic attributes of the plot, relating to the display size and range of the plot.
        """
        self.width = width
        self.height = height
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.image = None

    def iteration(self, max_iter):
        """
        Arguments:
        ----------
        max_iter: int
            The maximum number of iterations to perform for each point in the Mandelbrot set, relating to the display effect and the fineness of the plot.
        """
        self.max_iter = max_iter
