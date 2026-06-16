# Grafico boxplot por litologia
def boxplot_lito(df,var,lito_var,lito_lst, prefixo,pasta): 

    import plotly.graph_objects as go
    import numpy as np
    from plotly.subplots import make_subplots
    import pandas as pd
    
    
    # Litologias
    lito_col = df[lito_var].unique()
    lito_col
    
    # Busca cores das litologias para o banco de dados
    for i in lito_col:
   
        if i.upper() in litocolor:
            df.loc[(df[lito_var]==i) ,'color'] = litocolor[i.upper()]    
            
        else:
            df.loc[(df[lito_var]==i),'color'] = '#FFEEBB'
     
    fig = go.Figure()

    fig = make_subplots(
        column_widths=[0.05, 0.95],
        rows=2, cols=2,
        shared_xaxes=False,
        vertical_spacing=0.04,
        horizontal_spacing=0.01,
        specs=[[{"type": "bar"},{"type": "bar"}],
               [{"type": "table"},{"type": "table"}]])

    st_sum = pd.DataFrame()

    for i in lito_lst:
        mask = (df[lito_var]==i) 
        l_cor = list(df[mask]['color'].unique())
        fig.add_trace(go.Box(y=df[mask][var],name=i,marker_color=l_cor[0]), row=1, col=2)
        st_sum[i] = round(df[mask][var].describe(include='all'),2)

    st_data = [st_sum.values[:, i].tolist() for i in range(st_sum.values.shape[1])]

    # Criar a tabela
    fig.add_trace(go.Table(header=dict(values=st_data,
                    line_color='#FFFFFF',
                    fill_color='#FFFFFF',
                    align=['center','center'],
                    font=dict(color='black', size=12)),
                    domain=dict(x=[0,1]),
                    #cells=dict(values=st_data)
    ),row=2, col=2)

    idx=[]

    idx.append(st_sum.index)

    fig.add_trace(go.Table(header=dict(values=idx,
                    line_color='#FFFFFF',
                    fill_color='#FFFFFF',
                    align=['center','center'],
                    font=dict(color='black', size=12)),
    ),row=2, col=1)


    fig.update_layout(height=900,width=950, margin=dict(t=50, b=0, l=25, r=25),template="plotly_white",
                      title=dict(text='Boxplot variavel: {}'.format(var), x=0.5))
    return fig.show()
    #fig.show()
    fig.write_html('{}/{}_boxplot.html'.format(pasta,prefixo))
