def renderTab3(html,dcc):
    return html.Div([
                html.H1('Categorical Plot Pokemon', className='h1'),
                html.Div(children=[
                    html.Div([
                        dcc.Dropdown(
                            id='jenisPlot',
                            options=[{'label': i.capitalize(), 'value': i} for i in ['bar','box','violin']],
                            value='bar'
                        )
                    ],className='col-6')
                ],className='row'),
                dcc.Graph(
                    id='categoricalPlot'
                )
            ])