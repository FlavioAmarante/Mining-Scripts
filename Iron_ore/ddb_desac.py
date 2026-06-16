# Desacumula banco de dados Faixas. 
def ddb_desac(df, var_break,brk):
    
    import pandas as pd
    import numpy as np

    df = df.rename(columns=str.lower)
    
    mask = (df[var_break] == brk)
    
    # Zera as variáveis
    df.loc[mask,'fe1'] = np.nan
    df.loc[mask,'si1'] = np.nan
    df.loc[mask,'p1'] = np.nan
    df.loc[mask,'al1'] = np.nan
    df.loc[mask,'mn1'] = np.nan
    df.loc[mask,'pf1'] = np.nan
    df.loc[mask,'ti1'] = np.nan
    df.loc[mask,'mg1'] = np.nan
    df.loc[mask,'ca1'] = np.nan

    df.loc[mask,'fe2'] = np.nan
    df.loc[mask,'si2'] = np.nan
    df.loc[mask,'p2'] = np.nan
    df.loc[mask,'al2'] = np.nan
    df.loc[mask,'mn2'] = np.nan
    df.loc[mask,'pf2'] = np.nan
    df.loc[mask,'ti2'] = np.nan
    df.loc[mask,'mg2'] = np.nan
    df.loc[mask,'ca2'] = np.nan

    df.loc[mask,'fe3'] = np.nan
    df.loc[mask,'si3'] = np.nan
    df.loc[mask,'p3'] = np.nan
    df.loc[mask,'al3'] = np.nan
    df.loc[mask,'mn3'] = np.nan
    df.loc[mask,'pf3'] = np.nan
    df.loc[mask,'ti3'] = np.nan
    df.loc[mask,'mg3'] = np.nan
    df.loc[mask,'ca3'] = np.nan

    df.loc[mask,'fe4'] = np.nan
    df.loc[mask,'si4'] = np.nan
    df.loc[mask,'p4'] = np.nan
    df.loc[mask,'al4'] = np.nan
    df.loc[mask,'mn4'] = np.nan
    df.loc[mask,'pf4'] = np.nan
    df.loc[mask,'ti4'] = np.nan
    df.loc[mask,'mg4'] = np.nan
    df.loc[mask,'ca4'] = np.nan

    # Desacumula
    
    df.loc[mask & (df['g1'] > 0), 'fe1'] = (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'afe1'])) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )
    df.loc[mask & (df['g1'] > 0), 'si1'] = (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'asi1'])) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )
    df.loc[mask & (df['g1'] > 0), 'p1'] =  (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'ap1'] )) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )
    df.loc[mask & (df['g1'] > 0), 'al1'] = (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'aal1'])) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )
    df.loc[mask & (df['g1'] > 0), 'mn1'] = (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'amn1'])) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )
    df.loc[mask & (df['g1'] > 0), 'pf1'] = (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'apf1'])) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )
    df.loc[mask & (df['g1'] > 0), 'ti1'] = (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'ati1'])) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )
    df.loc[mask & (df['g1'] > 0), 'mg1'] = (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'amg1'])) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )
    df.loc[mask & (df['g1'] > 0), 'ca1'] = (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'aca1'])) / (np.nan_to_num(df.loc[mask & (df['g1'] > 0), 'g1']) )

    df.loc[mask & (df['g2'] > 0), 'fe2'] = (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'afe2'])) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )
    df.loc[mask & (df['g2'] > 0), 'si2'] = (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'asi2'])) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )
    df.loc[mask & (df['g2'] > 0), 'p2'] =  (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'ap2'] )) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )
    df.loc[mask & (df['g2'] > 0), 'al2'] = (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'aal2'])) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )
    df.loc[mask & (df['g2'] > 0), 'mn2'] = (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'amn2'])) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )
    df.loc[mask & (df['g2'] > 0), 'pf2'] = (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'apf2'])) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )
    df.loc[mask & (df['g2'] > 0), 'ti2'] = (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'ati2'])) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )
    df.loc[mask & (df['g2'] > 0), 'mg2'] = (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'amg2'])) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )
    df.loc[mask & (df['g2'] > 0), 'ca2'] = (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'aca2'])) / (np.nan_to_num(df.loc[mask & (df['g2'] > 0), 'g2']) )

    df.loc[mask & (df['g3'] > 0), 'fe3'] = (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'afe3'])) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )
    df.loc[mask & (df['g3'] > 0), 'si3'] = (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'asi3'])) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )
    df.loc[mask & (df['g3'] > 0), 'p3'] =  (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'ap3'] )) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )
    df.loc[mask & (df['g3'] > 0), 'al3'] = (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'aal3'])) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )
    df.loc[mask & (df['g3'] > 0), 'mn3'] = (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'amn3'])) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )
    df.loc[mask & (df['g3'] > 0), 'pf3'] = (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'apf3'])) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )
    df.loc[mask & (df['g3'] > 0), 'ti3'] = (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'ati3'])) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )
    df.loc[mask & (df['g3'] > 0), 'mg3'] = (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'amg3'])) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )
    df.loc[mask & (df['g3'] > 0), 'ca3'] = (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'aca3'])) / (np.nan_to_num(df.loc[mask & (df['g3'] > 0), 'g3']) )

    df.loc[mask & (df['g4'] > 0), 'fe4'] = (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'afe4'])) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df.loc[mask & (df['g4'] > 0), 'si4'] = (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'asi4'])) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df.loc[mask & (df['g4'] > 0), 'p4'] =  (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'ap4'] )) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df.loc[mask & (df['g4'] > 0), 'al4'] = (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'aal4'])) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df.loc[mask & (df['g4'] > 0), 'mn4'] = (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'amn4'])) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df.loc[mask & (df['g4'] > 0), 'pf4'] = (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'apf4'])) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df.loc[mask & (df['g4'] > 0), 'ti4'] = (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'ati4'])) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df.loc[mask & (df['g4'] > 0), 'mg4'] = (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'amg4'])) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df.loc[mask & (df['g4'] > 0), 'ca4'] = (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'aca4'])) / (np.nan_to_num(df.loc[mask & (df['g4'] > 0), 'g4']))
    df = df.rename(columns=str.upper)
    
    return df
