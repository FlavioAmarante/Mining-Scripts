# Tratamento dos intervalos com Granulometria <2%

def ddb_trata_gra(df1, var_break,brk):

    import pandas as pd
    import numpy as np

    df = df1.copy()
    df['FLAG'] = ''
    
    df = df.rename(columns=str.lower)
    
    # Verifica se a coluna FLAG existe no DataFrame
    if 'flag' not in df.columns:
        df['flag'] = ''
    # G1 <2%
    mask = (df[var_break] == brk) & (df['g1'] < 2) & (df['g1'] > 0) & (~df['afe1'].isna()) 
    df.loc[mask, 'flag'] =      'x'
    df.loc[mask, 'g2'] =    (np.nan_to_num(df.loc[mask, 'g2']  )) + (np.nan_to_num(df.loc[mask, 'g1']    ))
    df.loc[mask, 'afe2'] =  (np.nan_to_num(df.loc[mask, 'afe2'])) + (np.nan_to_num(df.loc[mask, 'afe1']  ))
    df.loc[mask, 'asi2'] =  (np.nan_to_num(df.loc[mask, 'asi2'])) + (np.nan_to_num(df.loc[mask, 'asi1']  ))
    df.loc[mask, 'ap2'] =   (np.nan_to_num(df.loc[mask, 'ap2'] )) + (np.nan_to_num(df.loc[mask, 'ap1']   ))
    df.loc[mask, 'aal2'] =  (np.nan_to_num(df.loc[mask, 'aal2'])) + (np.nan_to_num(df.loc[mask, 'aal1']  ))
    df.loc[mask, 'amn2'] =  (np.nan_to_num(df.loc[mask, 'amn2'])) + (np.nan_to_num(df.loc[mask, 'amn1']  ))
    df.loc[mask, 'apf2'] =  (np.nan_to_num(df.loc[mask, 'apf2'])) + (np.nan_to_num(df.loc[mask, 'apf1']  ))
    df.loc[mask, 'ati2'] =  (np.nan_to_num(df.loc[mask, 'ati2'])) + (np.nan_to_num(df.loc[mask, 'ati1']  ))
    df.loc[mask, 'amg2'] =  (np.nan_to_num(df.loc[mask, 'amg2'])) + (np.nan_to_num(df.loc[mask, 'amg1']  ))
    df.loc[mask, 'aca2'] =  (np.nan_to_num(df.loc[mask, 'aca2'])) + (np.nan_to_num(df.loc[mask, 'aca1']  )) 
    
    df.loc[mask,  'g1'] = 0
    df.loc[mask,  'afe1'] = 0
    df.loc[mask,  'asi1'] = 0
    df.loc[mask,  'ap1'] = 0
    df.loc[mask,  'aal1'] = 0
    df.loc[mask,  'amn1'] = 0
    df.loc[mask,  'apf1'] = 0
    df.loc[mask,  'ati1'] = 0
    df.loc[mask,  'amg1'] = 0
    df.loc[mask,  'aca1'] = 0
    
    df.loc[mask,  'fe1'] = np.nan
    df.loc[mask,  'si1'] = np.nan
    df.loc[mask,  'p1'] = np.nan
    df.loc[mask,  'al1'] = np.nan
    df.loc[mask, 'mn1'] = np.nan
    df.loc[mask, 'pf1'] = np.nan
    df.loc[mask, 'ti1'] = np.nan
    df.loc[mask, 'mg1'] = np.nan
    df.loc[mask, 'ca1'] = np.nan
    
    # G2 <2%
    mask = (df[var_break] == brk) & (df['g2'] < 2) & (df['g2'] > 0)  & (~df['afe2'].isna()) 
    df.loc[mask, 'flag'] =      'x'
    df.loc[mask, 'g3'] =    (np.nan_to_num(  df.loc[mask, 'g3'])) + (np.nan_to_num(df.loc[mask, 'g2']   ))
    df.loc[mask, 'afe3'] =  (np.nan_to_num(df.loc[mask, 'afe3'])) + (np.nan_to_num(df.loc[mask, 'afe2'] ))
    df.loc[mask, 'asi3'] =  (np.nan_to_num(df.loc[mask, 'asi3'])) + (np.nan_to_num(df.loc[mask, 'asi2'] ))
    df.loc[mask, 'ap3'] =   (np.nan_to_num( df.loc[mask, 'ap3'])) + (np.nan_to_num(df.loc[mask, 'ap2']  ))
    df.loc[mask, 'aal3'] =  (np.nan_to_num(df.loc[mask, 'aal3'])) + (np.nan_to_num(df.loc[mask, 'aal2'] ))
    df.loc[mask, 'amn3'] =  (np.nan_to_num(df.loc[mask, 'amn3'])) + (np.nan_to_num(df.loc[mask, 'amn2'] ))
    df.loc[mask, 'apf3'] =  (np.nan_to_num(df.loc[mask, 'apf3'])) + (np.nan_to_num(df.loc[mask, 'apf2'] ))
    df.loc[mask, 'ati3'] =  (np.nan_to_num(df.loc[mask, 'ati3'])) + (np.nan_to_num(df.loc[mask, 'ati2'] ))
    df.loc[mask, 'amg3'] =  (np.nan_to_num(df.loc[mask, 'amg3'])) + (np.nan_to_num(df.loc[mask, 'amg2'] ))
    df.loc[mask, 'aca3'] =  (np.nan_to_num(df.loc[mask, 'aca3'])) + (np.nan_to_num(df.loc[mask, 'aca2'] ))  
    
    df.loc[mask,  'g2'] = 0
    df.loc[mask,  'afe2'] = 0
    df.loc[mask,  'asi2'] = 0
    df.loc[mask,  'ap2'] = 0
    df.loc[mask,  'aal2'] = 0
    df.loc[mask,  'amn2'] = 0
    df.loc[mask,  'apf2'] = 0
    df.loc[mask,  'ati2'] = 0
    df.loc[mask,  'amg2'] = 0
    df.loc[mask,  'aca2'] = 0
    
    df.loc[mask,  'fe2'] = np.nan
    df.loc[mask,  'si2'] = np.nan
    df.loc[mask,  'p2'] = np.nan
    df.loc[mask,  'al2'] = np.nan
    df.loc[mask, 'mn2'] = np.nan
    df.loc[mask, 'pf2'] = np.nan
    df.loc[mask, 'ti2'] = np.nan
    df.loc[mask, 'mg2'] = np.nan
    df.loc[mask, 'ca2'] = np.nan
    
    # G3 <2%
    mask = (df[var_break] == brk) & (df['g3'] < 2) & (df['g3'] > 0)  & (~df['afe3'].isna()) 
    df.loc[mask, 'flag'] =      'x'
    df.loc[mask, 'g4'] =    (np.nan_to_num(  df.loc[mask, 'g4'])) + (np.nan_to_num(df.loc[mask, 'g3']   ))
    df.loc[mask, 'afe4'] =  (np.nan_to_num(df.loc[mask, 'afe4'])) + (np.nan_to_num(df.loc[mask, 'afe3'] ))
    df.loc[mask, 'asi4'] =  (np.nan_to_num(df.loc[mask, 'asi4'])) + (np.nan_to_num(df.loc[mask, 'asi3'] ))
    df.loc[mask, 'ap4'] =   (np.nan_to_num( df.loc[mask, 'ap4'])) + (np.nan_to_num(df.loc[mask, 'ap3']  ))
    df.loc[mask, 'aal4'] =  (np.nan_to_num(df.loc[mask, 'aal4'])) + (np.nan_to_num(df.loc[mask, 'aal3'] ))
    df.loc[mask, 'amn4'] =  (np.nan_to_num(df.loc[mask, 'amn4'])) + (np.nan_to_num(df.loc[mask, 'amn3'] ))
    df.loc[mask, 'apf4'] =  (np.nan_to_num(df.loc[mask, 'apf4'])) + (np.nan_to_num(df.loc[mask, 'apf3'] ))
    df.loc[mask, 'ati4'] =  (np.nan_to_num(df.loc[mask, 'ati4'])) + (np.nan_to_num(df.loc[mask, 'ati3'] ))
    df.loc[mask, 'amg4'] =  (np.nan_to_num(df.loc[mask, 'amg4'])) + (np.nan_to_num(df.loc[mask, 'amg3'] ))
    df.loc[mask, 'aca4'] =  (np.nan_to_num(df.loc[mask, 'aca4'])) + (np.nan_to_num(df.loc[mask, 'aca3'] )) 
    
    df.loc[mask,  'g3'] = 0
    df.loc[mask,  'afe3'] = 0
    df.loc[mask,  'asi3'] = 0
    df.loc[mask,  'ap3'] = 0
    df.loc[mask,  'aal3'] = 0
    df.loc[mask,  'amn3'] = 0
    df.loc[mask,  'apf3'] = 0
    df.loc[mask,  'ati3'] = 0
    df.loc[mask,  'amg3'] = 0
    df.loc[mask,  'aca3'] = 0
    
    df.loc[mask,  'fe3'] = np.nan
    df.loc[mask,  'si3'] = np.nan
    df.loc[mask,  'p3'] = np.nan
    df.loc[mask,  'al3'] = np.nan
    df.loc[mask, 'mn3'] = np.nan
    df.loc[mask, 'pf3'] = np.nan
    df.loc[mask, 'ti3'] = np.nan
    df.loc[mask, 'mg3'] = np.nan
    df.loc[mask, 'ca3'] = np.nan

    # G4 <4%
    mask = (df[var_break] == brk) & (df['g4'] < 2) & (df['g4'] > 0)  & (~df['afe4'].isna()) 
    df.loc[mask, 'flag'] =      'x'
    df.loc[mask, 'g3'] =   (np.nan_to_num(   df.loc[mask, 'g3'])) + (np.nan_to_num(df.loc[mask, 'g4']    ))
    df.loc[mask, 'afe3'] = (np.nan_to_num( df.loc[mask, 'afe3'])) + (np.nan_to_num(df.loc[mask, 'afe4']  ))
    df.loc[mask, 'asi3'] = (np.nan_to_num( df.loc[mask, 'asi3'])) + (np.nan_to_num(df.loc[mask, 'asi4']  ))
    df.loc[mask, 'ap3'] =  (np.nan_to_num(  df.loc[mask, 'ap3'])) + (np.nan_to_num(df.loc[mask, 'ap4']   ))
    df.loc[mask, 'aal3'] = (np.nan_to_num( df.loc[mask, 'aal3'])) + (np.nan_to_num(df.loc[mask, 'aal4']  ))
    df.loc[mask, 'amn3'] = (np.nan_to_num( df.loc[mask, 'amn3'])) + (np.nan_to_num(df.loc[mask, 'amn4']  ))
    df.loc[mask, 'apf3'] = (np.nan_to_num( df.loc[mask, 'apf3'])) + (np.nan_to_num(df.loc[mask, 'apf4']  ))
    df.loc[mask, 'ati3'] = (np.nan_to_num( df.loc[mask, 'ati3'])) + (np.nan_to_num(df.loc[mask, 'ati4']  ))
    df.loc[mask, 'amg3'] = (np.nan_to_num( df.loc[mask, 'amg3'])) + (np.nan_to_num(df.loc[mask, 'amg4']  ))
    df.loc[mask, 'aca3'] = (np.nan_to_num( df.loc[mask, 'aca3'])) + (np.nan_to_num(df.loc[mask, 'aca4']  )) 
    
    df.loc[mask,  'g4'] = 0
    df.loc[mask,  'afe4'] = 0
    df.loc[mask,  'asi4'] = 0
    df.loc[mask,  'ap4'] = 0
    df.loc[mask,  'aal4'] = 0
    df.loc[mask,  'amn4'] = 0
    df.loc[mask,  'apf4'] = 0
    df.loc[mask,  'ati4'] = 0
    df.loc[mask,  'amg4'] = 0
    df.loc[mask,  'aca4'] = 0
    
    df.loc[mask,  'fe4'] = np.nan
    df.loc[mask,  'si4'] = np.nan
    df.loc[mask,  'p4'] = np.nan
    df.loc[mask,  'al4'] = np.nan
    df.loc[mask, 'mn4'] = np.nan
    df.loc[mask, 'pf4'] = np.nan
    df.loc[mask, 'ti4'] = np.nan
    df.loc[mask, 'mg4'] = np.nan
    df.loc[mask, 'ca4'] = np.nan
    
    # G3 <2%
    mask = (df[var_break] == brk) & (df['g3'] < 2) & (df['g3'] > 0)  & (~df['afe3'].isna()) 
    df.loc[mask, 'flag'] =      'x'
    df.loc[mask, 'g2'] =   (np.nan_to_num(   df.loc[mask, 'g2'])) + (np.nan_to_num(df.loc[mask, 'g3']    ))
    df.loc[mask, 'afe2'] = (np.nan_to_num( df.loc[mask, 'afe2'])) + (np.nan_to_num(df.loc[mask, 'afe3']  ))
    df.loc[mask, 'asi2'] = (np.nan_to_num( df.loc[mask, 'asi2'])) + (np.nan_to_num(df.loc[mask, 'asi3']  ))
    df.loc[mask, 'ap2'] =  (np.nan_to_num(  df.loc[mask, 'ap2'])) + (np.nan_to_num(df.loc[mask, 'ap3']   ))
    df.loc[mask, 'aal2'] = (np.nan_to_num( df.loc[mask, 'aal2'])) + (np.nan_to_num(df.loc[mask, 'aal3']  ))
    df.loc[mask, 'amn2'] = (np.nan_to_num( df.loc[mask, 'amn2'])) + (np.nan_to_num(df.loc[mask, 'amn3']  ))
    df.loc[mask, 'apf2'] = (np.nan_to_num( df.loc[mask, 'apf2'])) + (np.nan_to_num(df.loc[mask, 'apf3']  ))
    df.loc[mask, 'ati2'] = (np.nan_to_num( df.loc[mask, 'ati2'])) + (np.nan_to_num(df.loc[mask, 'ati3']  ))
    df.loc[mask, 'amg2'] = (np.nan_to_num( df.loc[mask, 'amg2'])) + (np.nan_to_num(df.loc[mask, 'amg3']  ))
    df.loc[mask, 'aca2'] = (np.nan_to_num( df.loc[mask, 'aca2'])) + (np.nan_to_num(df.loc[mask, 'aca3']  )) 
    
    df.loc[mask,  'g3'] = 0
    df.loc[mask,  'afe3'] = 0
    df.loc[mask,  'asi3'] = 0
    df.loc[mask,  'ap3'] = 0
    df.loc[mask,  'aal3'] = 0
    df.loc[mask,  'amn3'] = 0
    df.loc[mask,  'apf3'] = 0
    df.loc[mask,  'ati3'] = 0
    df.loc[mask,  'amg3'] = 0
    df.loc[mask,  'aca3'] = 0
    df.loc[mask,  'fe3'] = np.nan
    df.loc[mask,  'si3'] = np.nan
    df.loc[mask,  'p3'] = np.nan
    df.loc[mask,  'al3'] = np.nan
    df.loc[mask, 'mn3'] = np.nan
    df.loc[mask, 'pf3'] = np.nan
    df.loc[mask, 'ti3'] = np.nan
    df.loc[mask, 'mg3'] = np.nan
    df.loc[mask, 'ca3'] = np.nan
    
    # G2 <2%
    mask = (df[var_break] == brk) & (df['g2'] < 2) & (df['g2'] > 0)  & (~df['afe2'].isna()) 
    df.loc[mask, 'flag'] =      'x'
    df.loc[mask, 'g1'] =   (np.nan_to_num(   df.loc[mask, 'g1'] ))+ (np.nan_to_num(df.loc[mask, 'g2']   ))
    df.loc[mask, 'afe1'] = (np.nan_to_num( df.loc[mask, 'afe1'] ))+ (np.nan_to_num(df.loc[mask, 'afe2'] ))
    df.loc[mask, 'asi1'] = (np.nan_to_num( df.loc[mask, 'asi1'] ))+ (np.nan_to_num(df.loc[mask, 'asi2'] ))
    df.loc[mask, 'ap1'] =  (np.nan_to_num(  df.loc[mask, 'ap1'] ))+ (np.nan_to_num(df.loc[mask, 'ap2']  ))
    df.loc[mask, 'aal1'] = (np.nan_to_num( df.loc[mask, 'aal1'] ))+ (np.nan_to_num(df.loc[mask, 'aal2'] ))
    df.loc[mask, 'amn1'] = (np.nan_to_num( df.loc[mask, 'amn1'] ))+ (np.nan_to_num(df.loc[mask, 'amn2'] ))
    df.loc[mask, 'apf1'] = (np.nan_to_num( df.loc[mask, 'apf1'] ))+ (np.nan_to_num(df.loc[mask, 'apf2'] ))
    df.loc[mask, 'ati1'] = (np.nan_to_num( df.loc[mask, 'ati1'] ))+ (np.nan_to_num(df.loc[mask, 'ati2'] ))
    df.loc[mask, 'amg1'] = (np.nan_to_num( df.loc[mask, 'amg1'] ))+ (np.nan_to_num(df.loc[mask, 'amg2'] ))
    df.loc[mask, 'aca1'] = (np.nan_to_num( df.loc[mask, 'aca1'] ))+ (np.nan_to_num(df.loc[mask, 'aca2'] ))  
    
    df.loc[mask,  'g2'] = 0
    df.loc[mask,  'afe2'] = 0
    df.loc[mask,  'asi2'] = 0
    df.loc[mask,  'ap2'] = 0
    df.loc[mask,  'aal2'] = 0
    df.loc[mask,  'amn2'] = 0
    df.loc[mask,  'apf2'] = 0
    df.loc[mask,  'ati2'] = 0
    df.loc[mask,  'amg2'] = 0
    df.loc[mask,  'aca2'] = 0
    df.loc[mask,  'fe2'] = np.nan
    df.loc[mask,  'si2'] = np.nan
    df.loc[mask,  'p2'] = np.nan
    df.loc[mask,  'al2'] = np.nan
    df.loc[mask, 'mn2'] = np.nan
    df.loc[mask, 'pf2'] = np.nan
    df.loc[mask, 'ti2'] = np.nan
    df.loc[mask, 'mg2'] = np.nan
    df.loc[mask, 'ca2'] = np.nan 
            
    df = df.rename(columns=str.upper)
    return df
