
from jinja2 import Environment, PackageLoader, select_autoescape
import pandas as pd
import numpy as np
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from piezometer import PiezometerMetaData, PiezometerDataHandler


env = Environment(
    loader=PackageLoader('main', 'templates'),
    autoescape=select_autoescape(['html'])
)

PIEZOMETERS = [
    PiezometerMetaData("sample.pvt","Test",12.2)
]

data_handler = PiezometerDataHandler(piezomer_meta_data=PIEZOMETERS)
data=data_handler.load_piezometer_data()

source = ColumnDataSource.from_df(next(data)[1])


p = figure(
    plot_height=250, 
    sizing_mode="stretch_width",
    x_axis_type="datetime",
    output_backend="webgl",
    tools=['hover']
    )
p.line('Date_Time',"GWL", source=source, color='navy', alpha=0.5)

script, div = components(p)
with open('plot.html', 'w') as f:
    f.write(env.get_template("piezometer_rapport").render(doc_title="gangster",script=script, div=div)
        )
