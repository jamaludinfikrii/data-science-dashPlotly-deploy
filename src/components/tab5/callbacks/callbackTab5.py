from plotly import tools

subplots_hist = {
    'All' : [1,1],
    'Generation' : [3,2],
    'Legendary' : [1,2]
}

def updateFigHist(col,cat,dfPokemon,go):
    jmlrow,jmlcol = subplots_hist[cat][0],subplots_hist[cat][1]
    subtitles = ['All']
    if(cat != 'All') :
        subtitles = []
        for item in dfPokemon[cat].unique() :
            subtitles.append(str(item))

    fig = tools.make_subplots(rows=jmlrow, 
                            cols=jmlcol,
                            subplot_titles=subtitles)
    r,c = 1,1;
    if(cat == 'All'):
        fig.append_trace(
             go.Histogram(
                    x=dfPokemon[
                        (dfPokemon[col] > (dfPokemon[col].mean() - 2 * dfPokemon[col].std()))
                        & (dfPokemon[col] < (dfPokemon[col].mean() + 2 * dfPokemon[col].std()))
                    ][col],
                    marker=dict(
                        color="green"
                    ),
                    name="Normal " + col,
                    opacity=0.7
                ),1,1
        )
        fig.append_trace(
             go.Histogram(
                x=dfPokemon[
                    (dfPokemon[col] < (dfPokemon[col].mean() - 2 * dfPokemon[col].std()))
                    | (dfPokemon[col] > (dfPokemon[col].mean() + 2 * dfPokemon[col].std()))
                ][col],
                marker=dict(
                    color="red"
                ),
                name="Outlier " + col,
                opacity=0.7
            ),1,1
        )
        fig['layout']['xaxis'+str(1)].update(title=col.capitalize())
        fig['layout']['yaxis'+str(1)].update(title='Total Pokemon')
    else :
        for item,index in zip(dfPokemon[cat].unique(), range(1, dfPokemon[cat].nunique()+1)) :
            fig.append_trace(
                go.Histogram(
                        x=dfPokemon[
                            (dfPokemon[cat] == item)
                            & (dfPokemon[col] > (dfPokemon[col].mean() - 2 * dfPokemon[col].std()))
                            & (dfPokemon[col] < (dfPokemon[col].mean() + 2 * dfPokemon[col].std()))
                        ][col],
                        marker=dict(
                            color="green"
                        ),
                        name="Normal " + str(item) + " " + col,
                        opacity=0.7
                    ),r,c
            )
            fig.append_trace(
                go.Histogram(
                    x=dfPokemon[
                        (dfPokemon[cat] == item)
                        & ((dfPokemon[col] < (dfPokemon[col].mean() - 2 * dfPokemon[col].std()))
                        | (dfPokemon[col] > (dfPokemon[col].mean() + 2 * dfPokemon[col].std())))
                    ][col],
                    marker=dict(
                        color="red"
                    ),
                    name="Outlier " + str(item) + " " + col,
                    opacity=0.7
                ),r,c
            )
            fig['layout']['xaxis'+str(index)].update(title=col.capitalize())
            fig['layout']['yaxis'+str(index)].update(title='Total Pokemon')
            c += 1;
            # sLegend = False;
            if(c > jmlcol) :
                c = 1;
                r += 1;
    if(cat == 'Generation') :
        fig['layout'].update(height=700, width=1000,
                            title='Histogram ' + col.capitalize())
    else :
        fig['layout'].update(height=450, width=1000,
                            title='Histogram ' + col.capitalize())
    return fig