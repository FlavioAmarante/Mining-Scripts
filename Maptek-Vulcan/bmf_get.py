# Busca variáveis modelo de blocos
def bmf_get(model_lst,lst_vars):

    from maptek import vulcan as vl
    import pandas as pd
    
    df  = pd.DataFrame()
    
    for i in model_lst:
        # Avaliação modelo de blocos 
        bm = vl.block_model(i)
        vars_bm = list(bm.field_list())
        bmf = pd.DataFrame()
        
        for j in lst_vars:
            if j in vars_bm:
                bmf[j] = bm.get_data(j)
            else:
                print('Variavel',j,'não existe no modelo :',i)
        bm.close()
        
        bmf['model'] = i
        
        df = pd.concat([df, bmf], axis=0)
        
    return df
