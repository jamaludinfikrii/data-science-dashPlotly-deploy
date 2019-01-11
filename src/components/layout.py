# import Tab Ui
from src.components.tab1.render.renderTab1 import renderTab1
from src.components.tab2.render.renderTab2 import renderTab2
from src.components.tab3.render.renderTab3 import renderTab3
from src.components.tab4.render.renderTab4 import renderTab4
from src.components.tab5.render.renderTab5 import renderTab5

def layout(html,dcc,dfPokemon,go):
    return html.Div(children=[
                    html.H1(children='Dashboard Pokemon',className='titleDashboard'),
                    dcc.Tabs(id="tabs", value='tab-1', children=[
                        dcc.Tab(label='Pokemon Dataset', value='tab-1',children=[
                            renderTab1(dfPokemon,html)
                        ]),
                        dcc.Tab(label='Scatter Plot', value='tab-2',children=[
                            renderTab2(dfPokemon,html,dcc,go)
                        ]),
                        dcc.Tab(label='Categorical Plot', value='tab-3',children=[
                            renderTab3(html,dcc)
                        ]),
                        dcc.Tab(label='Pie Chart', value='tab-4',children=[
                            renderTab4(dfPokemon,html,dcc)
                        ]),
                        dcc.Tab(label='Histogram', value='tab-5',children=[
                            renderTab5(dfPokemon,html,dcc)
                            ,
                        ])
                    ], style={
                        'fontFamily': 'system-ui'
                    }, content_style={
                        'fontFamily': 'Arial',
                        'borderBottom': '1px solid #d6d6d6',
                        'borderLeft': '1px solid #d6d6d6',
                        'borderRight': '1px solid #d6d6d6',
                        'padding': '44px'
                    })
                ], style={
                    'maxWidth': '1200px',
                    'margin': '0 auto'
                })