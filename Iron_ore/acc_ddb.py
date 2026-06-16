# Acumulacao banco de dados
def ddb_acc(df1,varbreak,brk):
    
    import pandas as pd
    import numpy as np
    
    var_break = varbreak.lower()
    
    df = df1.copy()
    df = df.rename(columns=str.lower)
    mask = (df[var_break] == brk) & (df['g1'] > 0) 
    
    # ZERA VARIAVEIS ACUMULADAS
    
    df.loc[mask,'afe1'] = np.nan
    df.loc[mask,'asi1'] = np.nan
    df.loc[mask,'ap1'] = np.nan
    df.loc[mask,'aal1'] = np.nan
    df.loc[mask,'amn1'] = np.nan
    df.loc[mask,'apf1'] = np.nan
    df.loc[mask,'ati1'] = np.nan
    df.loc[mask,'amg1'] = np.nan
    df.loc[mask,'aca1'] = np.nan

    df.loc[mask,'afe2'] = np.nan
    df.loc[mask,'asi2'] = np.nan
    df.loc[mask,'ap2'] = np.nan
    df.loc[mask,'aal2'] = np.nan
    df.loc[mask,'amn2'] = np.nan
    df.loc[mask,'apf2'] = np.nan
    df.loc[mask,'ati2'] = np.nan
    df.loc[mask,'amg2'] = np.nan
    df.loc[mask,'aca2'] = np.nan

    df.loc[mask,'afe3'] = np.nan
    df.loc[mask,'asi3'] = np.nan
    df.loc[mask,'ap3'] = np.nan
    df.loc[mask,'aal3'] = np.nan
    df.loc[mask,'amn3'] = np.nan
    df.loc[mask,'apf3'] = np.nan
    df.loc[mask,'ati3'] = np.nan
    df.loc[mask,'amg3'] = np.nan
    df.loc[mask,'aca3'] = np.nan

    df.loc[mask,'afe4'] = np.nan
    df.loc[mask,'asi4'] = np.nan
    df.loc[mask,'ap4'] = np.nan
    df.loc[mask,'aal4'] = np.nan
    df.loc[mask,'amn4'] = np.nan
    df.loc[mask,'apf4'] = np.nan
    df.loc[mask,'ati4'] = np.nan
    df.loc[mask,'amg4'] = np.nan
    df.loc[mask,'aca4'] = np.nan

    # ACUMULACAO
    
    df.loc[mask, 'afe1'] = (np.nan_to_num(df.loc[mask, 'fe1'] * df.loc[mask, 'g1'])  )
    df.loc[mask, 'asi1'] = (np.nan_to_num(df.loc[mask, 'si1'] * df.loc[mask, 'g1'])  )
    df.loc[mask, 'ap1'] = (np.nan_to_num(df.loc[mask, 'p1'] * df.loc[mask, 'g1'])    )
    df.loc[mask, 'aal1'] = (np.nan_to_num(df.loc[mask, 'al1'] * df.loc[mask, 'g1'])  )
    df.loc[mask, 'amn1'] = (np.nan_to_num(df.loc[mask, 'mn1'] * df.loc[mask, 'g1'])  )
    df.loc[mask, 'apf1'] = (np.nan_to_num(df.loc[mask, 'pf1'] * df.loc[mask, 'g1'])  )
    df.loc[mask, 'ati1'] = (np.nan_to_num(df.loc[mask, 'ti1'] * df.loc[mask, 'g1'])  )
    df.loc[mask, 'amg1'] = (np.nan_to_num(df.loc[mask, 'mg1'] * df.loc[mask, 'g1'])  )
    df.loc[mask, 'aca1'] = (np.nan_to_num(df.loc[mask, 'ca1'] * df.loc[mask, 'g1'])  )
    
    mask = (df[var_break] == brk) & (df['g2'] > 0)
    
    df.loc[mask, 'afe2'] = (np.nan_to_num(df.loc[mask, 'fe2'] * df.loc[mask, 'g2'])  )
    df.loc[mask, 'asi2'] = (np.nan_to_num(df.loc[mask, 'si2'] * df.loc[mask, 'g2'])  )
    df.loc[mask, 'ap2'] = (np.nan_to_num(df.loc[mask, 'p2'] * df.loc[mask, 'g2'])    )
    df.loc[mask, 'aal2'] = (np.nan_to_num(df.loc[mask, 'al2'] * df.loc[mask, 'g2'])  )
    df.loc[mask, 'amn2'] = (np.nan_to_num(df.loc[mask, 'mn2'] * df.loc[mask, 'g2'])  )
    df.loc[mask, 'apf2'] = (np.nan_to_num(df.loc[mask, 'pf2'] * df.loc[mask, 'g2'])  )
    df.loc[mask, 'ati2'] = (np.nan_to_num(df.loc[mask, 'ti2'] * df.loc[mask, 'g2'])  )
    df.loc[mask, 'amg2'] = (np.nan_to_num(df.loc[mask, 'mg2'] * df.loc[mask, 'g2'])  )
    df.loc[mask, 'aca2'] = (np.nan_to_num(df.loc[mask, 'ca2'] * df.loc[mask, 'g2'])  )
    
    mask = (df[var_break] == brk) & (df['g3'] > 0)

    df.loc[mask, 'afe3'] = (np.nan_to_num(df.loc[mask, 'fe3'] * df.loc[mask, 'g3'])  )
    df.loc[mask, 'asi3'] = (np.nan_to_num(df.loc[mask, 'si3'] * df.loc[mask, 'g3'])  )
    df.loc[mask, 'ap3'] = (np.nan_to_num(df.loc[mask, 'p3'] * df.loc[mask, 'g3'])    )
    df.loc[mask, 'aal3'] = (np.nan_to_num(df.loc[mask, 'al3'] * df.loc[mask, 'g3'])  )
    df.loc[mask, 'amn3'] = (np.nan_to_num(df.loc[mask, 'mn3'] * df.loc[mask, 'g3'])  )
    df.loc[mask, 'apf3'] = (np.nan_to_num(df.loc[mask, 'pf3'] * df.loc[mask, 'g3'])  )
    df.loc[mask, 'ati3'] = (np.nan_to_num(df.loc[mask, 'ti3'] * df.loc[mask, 'g3'])  )
    df.loc[mask, 'amg3'] =(np.nan_to_num( df.loc[mask, 'mg3'] * df.loc[mask, 'g3'])  )
    df.loc[mask, 'aca3'] = (np.nan_to_num(df.loc[mask, 'ca3'] * df.loc[mask, 'g3'])  )
    
    mask = (df[var_break] == brk) & (df['g4'] > 0)

    df.loc[mask, 'afe4'] = (np.nan_to_num(df.loc[mask, 'fe4'] * df.loc[mask, 'g4'])  )
    df.loc[mask, 'asi4'] = (np.nan_to_num(df.loc[mask, 'si4'] * df.loc[mask, 'g4'])  )
    df.loc[mask, 'ap4'] =  (np.nan_to_num(df.loc[mask, 'p4'] * df.loc[mask, 'g4'] )  )
    df.loc[mask, 'aal4'] = (np.nan_to_num(df.loc[mask, 'al4'] * df.loc[mask, 'g4'])  )
    df.loc[mask, 'amn4'] = (np.nan_to_num(df.loc[mask, 'mn4'] * df.loc[mask, 'g4'])  )
    df.loc[mask, 'apf4'] = (np.nan_to_num(df.loc[mask, 'pf4'] * df.loc[mask, 'g4'])  )
    df.loc[mask, 'ati4'] = (np.nan_to_num(df.loc[mask, 'ti4'] * df.loc[mask, 'g4'])  )
    df.loc[mask, 'amg4'] = (np.nan_to_num(df.loc[mask, 'mg4'] * df.loc[mask, 'g4'])  )
    df.loc[mask, 'aca4'] = (np.nan_to_num(df.loc[mask, 'ca4'] * df.loc[mask, 'g4'])  )
    
    # Zera onde retido nas faixas = 0
    
    mask = (df[var_break] == 'FX') & (df['g1'] == 0) 
    
    df.loc[mask, 'afe1'] = 0
    df.loc[mask, 'asi1'] = 0
    df.loc[mask, 'ap1']  = 0
    df.loc[mask, 'aal1'] = 0
    df.loc[mask, 'amn1'] = 0
    df.loc[mask, 'apf1'] = 0
    df.loc[mask, 'ati1'] = 0
    df.loc[mask, 'amg1'] = 0
    df.loc[mask, 'aca1'] = 0
    
    mask = (df[var_break] == 'FX') & (df['g2'] == 0)
    
    df.loc[mask, 'afe2'] = 0
    df.loc[mask, 'asi2'] = 0
    df.loc[mask, 'ap2']  = 0 
    df.loc[mask, 'aal2'] = 0
    df.loc[mask, 'amn2'] = 0
    df.loc[mask, 'apf2'] = 0
    df.loc[mask, 'ati2'] = 0
    df.loc[mask, 'amg2'] = 0
    df.loc[mask, 'aca2'] = 0
    
    mask = (df[var_break] == 'FX') & (df['g3'] == 0)

    df.loc[mask, 'afe3'] = 0
    df.loc[mask, 'asi3'] = 0
    df.loc[mask, 'ap3']  = 0
    df.loc[mask, 'aal3'] = 0
    df.loc[mask, 'amn3'] = 0
    df.loc[mask, 'apf3'] = 0
    df.loc[mask, 'ati3'] = 0
    df.loc[mask, 'amg3'] = 0
    df.loc[mask, 'aca3'] = 0
    
    mask = (df[var_break] == 'FX') & (df['g4'] == 0)

    df.loc[mask, 'afe4'] = 0
    df.loc[mask, 'asi4'] = 0
    df.loc[mask, 'ap4']  = 0
    df.loc[mask, 'aal4'] = 0
    df.loc[mask, 'amn4'] = 0
    df.loc[mask, 'apf4'] = 0
    df.loc[mask, 'ati4'] = 0
    df.loc[mask, 'amg4'] = 0
    df.loc[mask, 'aca4'] = 0
    
    df = df.rename(columns=str.upper)
    
    return df
