
color_set = ['#000000','#FCE63D']
def renderTab2(df,html,dcc,go):
    return  html.Div([
            html.H1('Scatter Plot Pokemon', className='h1'),
            dcc.Graph(
                id='scatterPlot',
                figure={
                    'data': [
                        go.Scatter(
                            x=df[df['Legendary'] == col]['Attack'],
                            y=df[df['Legendary'] == col]['Defense'],
                            mode='markers',
                            marker=dict(color=color_set[i], size=10, line=dict(width=0.5, color='white')),
                            name=str(col)
                        ) for col, i in zip(df['Legendary'].unique(), range(2))
                    ],
                    'layout': go.Layout(
                        xaxis= dict(title='Attack'),
                        yaxis={'title': 'Defense'},
                        margin={ 'l': 40, 'b': 40, 't': 10, 'r': 10 },
                        hovermode='closest'
                    )
                }
            )
        ])