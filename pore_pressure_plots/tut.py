
import pandas as pd
from bokeh.plotting import figure
from bokeh.sampledata.stocks import AAPL
import jinja2
from bokeh.embed import components
import templates

df = pd.DataFrame(AAPL)
df['date'] = pd.to_datetime(df['date'])
p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")
p.line([0, 1, 2], [15, 3, 1], color='navy', alpha=0.5)

script, div = components(p)
with open('plot.html', 'w') as f:
    f.write(templates.poretrykkdash.render(script=script, div=div)
            )
