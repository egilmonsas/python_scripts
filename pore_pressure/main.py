
import jinja2
import pandas as pd
import numpy as np
from bokeh.embed import components
from bokeh.plotting import figure
import html_template

TITLE="Poretrykksammenstilling";




#Generate dummy data
N=10000
x=np.linspace(0,1000,N)
y=np.sin(x)+0.2*np.cos(0.2*x)

p = figure(
    plot_height=250, 
    sizing_mode="stretch_width",
    x_axis_type="datetime",
    output_backend="webgl"
    )
p.line(x,y, color='navy', alpha=0.5)

script, div = components(p)
with open('plot.html', 'w') as f:
    f.write(html_template.poretrykkdash.render(doc_title=TITLE,script=script, div=div))
