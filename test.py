from Mandelbrot_AW import MandelbrotSet, example_name, Mandelbrot_Plot

# Create an instance of the example_name class
mandelbrot = example_name(
    width=800,
    height=800,
    x_min=-2.0,
    x_max=1.0,
    y_min=-1.5,
    y_max=1.5,
    colormap="viridis",
    option="continuous",
)

# Create a Mandelbrot_Plot instance and plot
plotter = Mandelbrot_Plot(mandelbrot)
plotter.figure_plot(show_width=10, show_height=10)
