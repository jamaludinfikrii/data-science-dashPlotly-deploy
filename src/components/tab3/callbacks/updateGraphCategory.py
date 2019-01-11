def updateGraphCategory(jenisPlot,getPlot,go):
        return {
        'data': getPlot(jenisPlot),
        'layout': go.Layout(
                    xaxis={'title': 'Generation'},
                    yaxis={'title': 'Total Stat'},
                    margin=dict(l=40,b=40,t=10,r=10),
                    # legend=dict(x=0,y=1), 
                    hovermode='closest',
                    boxmode='group',violinmode='group'
                )
    }