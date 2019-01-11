import numpy as np

esti_func = {
    'Count': len,
    'Sum': sum,
    'Average': np.mean,
    'Standard Deviation': np.std
}

def updateGraphPie(cat,esti,col,dfPokemon,go):
    listLabel = list(dfPokemon[cat].unique())
    listLabel.sort()
    return {
        'data': [
            go.Pie(
                labels=listLabel,
                values=[esti_func[esti](dfPokemon[dfPokemon[cat] == item][col]) for item in listLabel],
                textinfo='value',
                hoverinfo='label+percent',
                marker=dict(
                    # colors=color_set[hue], 
                    line=dict(color='black', width=2)
                ),
                sort=False
            )
        ],
        'layout': go.Layout(
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1}
        )
    }