def renderTab4(dfPokemon,html,dcc):
    return html.Div([
                html.H1('Pie Chart Pokemon', className='h1'),
                html.Div(children=[
                    html.Div([
                        html.P('Category :'),
                        dcc.Dropdown(
                            id='catFilterPie',
                            options=[{'label': i.capitalize(), 'value': i} for i in ['Generation','Legendary']],
                            value='Generation'
                        )
                    ],className='col-4'),
                    html.Div([
                        html.P('Estimator :'),
                        dcc.Dropdown(
                            id='estiFilterPie',
                            options=[{'label': i, 'value': i} for i in ['Count','Sum','Average','Standard Deviation']],
                            value='Count'
                        )
                    ],className='col-4'),
                    html.Div([
                        html.P('Column :'),
                        dcc.Dropdown(
                            id='colFilterPie',
                            options=[{'label': i, 'value': i} for i in dfPokemon.describe().drop(['#','Generation'],axis=1).columns],
                            value='Total'
                        )
                    ],className='col-4')
                ],className='row'),
                dcc.Graph(
                    id='pieChart'
                )
            ])