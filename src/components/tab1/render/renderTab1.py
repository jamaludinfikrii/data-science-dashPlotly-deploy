
def generate_table(dataframe,html,max_rows=10,) :
    return html.Table(
         # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(str(dataframe[col][i])) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

def renderTab1(df ,html) :
    return html.Div([
                html.H1('Data Pokemon', className='h1'),
                generate_table(df , html)
            ])