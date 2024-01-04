# app.py
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
import numpy as np

# Create initial data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(x=x, y=y))

# Create a plot
plot = figure(title="Real-time Sin Plot", plot_height=300, plot_width=600)
line = plot.line('x', 'y', source=source)

# Define the callback function to update the plot
def update():
    new_y = np.sin(x + curdoc().session_context.request.arguments.get('shift', [0])[0].decode("utf-8").astype(float))
    source.data = dict(x=x, y=new_y)

# Add periodic callback to update the plot every 200 milliseconds
curdoc().add_periodic_callback(update, 200)

# Run the application
curdoc().title = "Real-time Sin Plot"
curdoc().add_root(plot)
