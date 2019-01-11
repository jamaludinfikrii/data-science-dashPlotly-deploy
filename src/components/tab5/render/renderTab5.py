def renderTab5(dfPokemon,html,dcc):
    return html.Div([
                html.H1('Histogram Pokemon', className='h1'),
                html.Div([
                    html.Div([
                        html.P('Column :'),
                        dcc.Dropdown(
                            id='colFilterHist',
                            options=[{'label': i, 'value': i} for i in dfPokemon.columns[4:11]],
                            value=dfPokemon.columns[4]
                        )
                    ],className='col-4'),
                     html.Div([
                        html.P('Category :'),
                        dcc.Dropdown(
                            id='catFilterHist',
                            options=[{'label': i, 'value': i} for i in ['All' , 'Generation' , 'Legendary']],
                            value='All'
                        )
                    ],className='col-4')
                ],className='row'),
                dcc.Graph(
                    id='histogramPlot',
                    figure={
                        
                    }
                )
            ])