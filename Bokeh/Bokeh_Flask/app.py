from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    # Create Bokeh plot
    x = np.linspace(0, 4 * np.pi, 100)
    y = np.sin(x)
    plot = figure(title="Sine Wave Plot", plot_height=300, plot_width=600)
    plot.line(x, y)

    # Embed Bokeh plot into HTML
    script, div = components(plot)
    return render_template('index.html', script=script, div=div)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)
