from os.path import dirname, join

import pandas as pd
import numpy as np

from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, HoverTool, HBox, VBoxForm
from bokeh.models.widgets import Slider, Select, TextInput
from bokeh.io import curdoc

# create Input controls
min_year = Slider(title="Min Year", start=2000, end=2016, value=2000, step=1)
max_year = Slider(title="Max Year", start=2000, end=2016, value=2016, step=1)
last_name = TextInput(title="Last Name", value="")

# change times to timestamp
def timeToTimeStamp(times):
    new_time=[]

    for i in range(len(times)):
        if len(times[i].split(':'))==2:
            time_string='00:'+times[i]
        else:
            time_string=times[i]

        if (type(pd.to_datetime(time_string))!=pd.tslib.Timestamp):
            time_stamp=pd.to_datetime('00:40:00')
        else:
            time_stamp=pd.to_datetime(time_string)
            new_time.append(time_stamp)
    
    return new_time

def select_runners():
    selected=runners[
            (runners.YEAR >= min_year.value) &
            (runners.YEAR <= max_year.value)].copy()
    #selected['color']='blue'
    selected['alpha']=0.5

    last_name_val=last_name.value.strip()
    print last_name_val
    
    selected["color"] = np.where(selected["LASTNAME"] == last_name_val, "red", "green")
    selected["alpha"] = np.where(selected["LASTNAME"] == last_name_val, 0.95, 0.4)
    selected["size"] = np.where(selected["LASTNAME"] == last_name_val, 20, 8)

    '''
    if (last_name_val != ""):
        
        selected[selected.LASTNAME==last_name_val]['color']='red'
        selected[selected.LASTNAME==last_name_val]['alpha']=0.85
    '''
    return selected

def update(attrname, old, new):
    df=select_runners()

    source.data=dict(x=df['AGE'], y=df['TIMESTAMP'],color=df['color'],alpha=df['alpha'],size=df['size'],last_name=df['LASTNAME'], first_name=df['FIRSTNAME'],time=df['TIME'],year=df['YEAR'])

runners=pd.read_csv('./output/alltime.csv')

runners['TIMESTAMP']=timeToTimeStamp(runners.TIME)

source = ColumnDataSource(data=dict(x=[], y=[]))

p = Figure(plot_width=1400, plot_height=800, y_axis_type='datetime')
#s1=p.scatter('AGE', 'TIMESTAMP', source =source, size=15, alpha=0.5)
p.circle(x="x", y="y", source=source, size="size",color="color",fill_alpha="alpha")

hover = HoverTool()
hover.tooltips = [('First Name', '@first_name'), ('Last Name', '@last_name'), ('Time', '@time'), ('Year', '@year'), ('Age', '@x')]
p.add_tools(hover)

controls=[min_year, max_year, last_name]

for c in controls:
    c.on_change('value', update)

inputs=HBox(VBoxForm(*controls), width=300)

update(None, None, None)

curdoc().add_root(HBox(inputs, p, width=1100))
















