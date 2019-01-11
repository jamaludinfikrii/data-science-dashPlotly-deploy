import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
from dash.dependencies import Input, Output
from categoryplot import dfPokemon, getPlot

# import Layout
from src.components.layout import layout

# import Callback
from src.components.tab3.callbacks.updateGraphCategory import updateGraphCategory
from src.components.tab4.callbacks.callbackTab4 import updateGraphPie
from src.components.tab5.callbacks.callbackTab5 import updateFigHist


disabledEsti = {
    'Count': True,
    'Sum': False,
    'Average': False,
    'Standard Deviation': False
}


app = dash.Dash(__name__)

server = app.server


# mean = dfPokemon['HP'].mean()
# std = dfPokemon['HP'].std()
# batasMax = mean + (2*std)
# batasMin = mean - (2*std)


app.title = 'Dashboard Pokemon'

app.layout = layout(html,dcc,dfPokemon,go)

@app.callback(
    Output(component_id='categoricalPlot', component_property='figure'),
    [Input(component_id='jenisPlot', component_property='value')]
)
def update_graph_categorical(jenisPlot):
    return updateGraphCategory(jenisPlot,getPlot,go)

@app.callback(
    Output(component_id='pieChart', component_property='figure'),
    [Input(component_id='catFilterPie', component_property='value'),
    Input(component_id='estiFilterPie', component_property='value'),
    Input(component_id='colFilterPie', component_property='value')]
)
def update_graph_pie(cat,esti,col):
    return updateGraphPie(cat,esti,col,dfPokemon,go)
 
    
@app.callback(
    Output('colFilterPie', 'disabled'),
    [Input('estiFilterPie','value')]
)
def update_ddl_col(esti) :
    return disabledEsti[esti]

@app.callback(
    Output('histogramPlot', 'figure'),
    [Input('colFilterHist','value'),
    Input('catFilterHist','value')]
)
def update_fig_hist(col,cat) :
    return updateFigHist(col,cat,dfPokemon,go)

if __name__ == '__main__':
    app.run_server(debug=True,port=2000)