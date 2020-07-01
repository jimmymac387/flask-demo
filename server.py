from io import StringIO
from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components
import numpy as np

app = Flask(__name__)


@app.route('/hello')
def index():
    return render_template('hello.html', message='hello')


# @app.route('/bokeh')
# Moved to static directory instead of decorator
# Don't want to write things to a static file
# Only use static for offline files

# Generate on the fly
@app.route('/plot')
def plot():
    p = figure(plot_width=300, plot_height=200)
    x = np.random.uniform(-1, 1, 100)
    y = np.random.uniform(-1, 1, 100)
    s = np.random.uniform(1, 10, 100)
    p.scatter(x, y, s)
    # sio = StringIO()
    script, div = components(p)
    return render_template(
        'plot.html',
        script=script,
        div=div
    )
    # save(p, sio)
    # return sio.getvalue()


if __name__ == '__main__':
    app.run(port=8000, debug=True)
