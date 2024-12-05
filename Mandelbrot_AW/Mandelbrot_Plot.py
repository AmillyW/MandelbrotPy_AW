import matplotlib.pyplot as plt
from Mandelbrot_Generate import MandelbrotSet


class example_name(MandelbrotSet):
    def __init__(self, colormap, option):
        """
        Initialize the 'colormap' attribute and call the parent class of example_name, MandelbrotSet.
        """
        super().__init__()
        self.option = option
        self.colormap = colormap
        self.image = None
        self.X, self.Y, self.image = self.array_generate()


class Mandelbrot_Plot:
    def __init__(self, example_instance):
        """
        Initialize the 'colormap' attribute and call the parent class of example_name, MandelbrotSet.
        """
        if not isinstance(example_instance, example_name):
            raise TypeError("Expected an instance of the 'example_name' class.")
        self.example_instance = example_instance

    def plot_on_axis(self, ax):
        if self.example_instance.image is None:
            raise ValueError(
                "Mandelbrot set not generated. Call array_generate() firse."
            )
        axes = ax.pcolormesh(
            self.example_instance.X,
            self.example_instance.Y,
            self.example_instance.image,
            cmap=self.example_instance.colormap,
            shading="auto",
        )
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel("Re(c)")
        ax.set_ylabel("Im(c)")
        ax.set_title(f"Mandelbrot Set ({example_name.colormap} colormap)")
        return axes

    def figure_plot(self, show_width, show_height):
        """
        Create a plot for the Mandelbrot set with the specified colormap and size.
        """
        # Create a figure and axis object
        fig, axis = plt.subplots(figsize=(show_width, show_height))

        # Plot the Mandelbrot set on the axis object
        example_name_result = self.plot_on_axis(axis)

        # Determine the label for the colorbar based on the option
        if example_name.option == "continuous":
            label_option = "Smoothed Number of Iterations"
        elif example_name.option == "discrete":
            label_option = "Number of Iterations"
        else:
            raise TypeError(
                "Invalid map option. Please choose either 'continuous' or 'discrete'."
            )

        # Add a colorbar to the plot
        fig.colorbar(example_name_result, ax=axis, label=label_option)
        plt.show()
