# Calcula globais
def calc_glb(df1,var_break,brk,inplace=True):    
    import numpy as np
    import pandas as pd
    
    lst_teores=['fe', 'si', 'p', 'al', 'mn', 'pf', 'ti', 'mg', 'ca']
    
    df = df1.copy()
    df.columns = df.columns.str.lower()
    df.reset_index()
    
    cols_df =list(df.columns)
    print(cols_df)
    
    if inplace == True:
        print('Calculo globais substituição')
        
        for i in lst_teores:
          df[f'{i}gl_bkp'] = df[f'{i}gl']
          
          if 'g23' in cols_df:
            mask = (df[var_break] == brk)&(df[f'g1'].notna())&(df[f'g2'].notna())&(df[f'g3'].notna())&(df[f'g4'].notna())

            df.loc[mask, f'{i}gl'] = (  (np.nan_to_num(df.loc[mask, f'{i}1'] * df.loc[mask, 'g1']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}2'] * df.loc[mask, 'g2']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}3'] * df.loc[mask, 'g3']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}4'] * df.loc[mask, 'g4'])))/ (df.loc[mask, 'g1'] + df.loc[mask, 'g2'] + df.loc[mask, 'g3'] + df.loc[mask, 'g4'])
            
            mask2 = (df[var_break] == brk) & (df[f'{i}1'].notna()) & (df[f'{i}23'].notna()) & (df[f'{i}4'].notna())
            mask3 = (df[var_break] == brk) & (df[f'{i}1'].isna()) | (df[f'{i}23'].isna()) | (df[f'{i}4'].isna())
            	
            df.loc[mask2, f'{i}gl'] = ((np.nan_to_num(df.loc[mask2, f'{i}1'] * df.loc[mask2, 'g1']))
                                          + (np.nan_to_num(df.loc[mask2, f'{i}23'] * df.loc[mask2, 'g23']))
                                          + (np.nan_to_num(df.loc[mask2, f'{i}4'] * df.loc[mask2, 'g4'])))/ (df.loc[mask2, 'g1'] + df.loc[mask2, 'g4']+df.loc[mask2, 'g23'])
            df.loc[mask3, f'{i}gl'] = df.loc[mask3, f'{i}gl_bkp']
                               
          
          else:
            mask = (df[var_break] == brk)
            df.loc[mask, f'{i}gl'] = (  (np.nan_to_num(df.loc[mask, f'{i}1'] * df.loc[mask, 'g1']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}2'] * df.loc[mask, 'g2']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}3'] * df.loc[mask, 'g3']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}4'] * df.loc[mask, 'g4'])))/ (df.loc[mask, 'g1'] + df.loc[mask, 'g2'] + df.loc[mask, 'g3'] + df.loc[mask, 'g4'])
          mnan = (df[ f'{i}gl'].isna())
          df.loc[mnan, f'{i}gl'] =  df.loc[mnan, f'{i}gl_bkp']               
               
    else:
        print('Calculo globais nova variável *_c')
        
        for i in lst_teores:
          df[f'{i}gl_bkp'] = df[f'{i}gl']
          
          if 'g23' in cols_df:
            mask = (df[var_break] == brk)&(df[f'g1'].notna())&(df[f'g2'].notna())&(df[f'g3'].notna())&(df[f'g4'].notna())

            df.loc[mask, f'{i}gl_c'] = (  (np.nan_to_num(df.loc[mask, f'{i}1'] * df.loc[mask, 'g1']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}2'] * df.loc[mask, 'g2']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}3'] * df.loc[mask, 'g3']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}4'] * df.loc[mask, 'g4'])))/ (df.loc[mask, 'g1'] + df.loc[mask, 'g2'] + df.loc[mask, 'g3'] + df.loc[mask, 'g4'])
            
            mask2 = (df[var_break] == brk) & (df[f'{i}1'].notna()) & (df[f'{i}23'].notna()) & (df[f'{i}4'].notna())
            mask3 = (df[var_break] == brk) & (df[f'{i}1'].isna()) | (df[f'{i}23'].isna()) | (df[f'{i}4'].isna())
            	
            df.loc[mask2, f'{i}gl_c'] = ((np.nan_to_num(df.loc[mask2, f'{i}1'] * df.loc[mask2, 'g1']))
                                          + (np.nan_to_num(df.loc[mask2, f'{i}23'] * df.loc[mask2, 'g23']))
                                          + (np.nan_to_num(df.loc[mask2, f'{i}4'] * df.loc[mask2, 'g4'])))/ (df.loc[mask2, 'g1'] + df.loc[mask2, 'g4']+df.loc[mask2, 'g23'])
            df.loc[mask3, f'{i}gl_c'] = df.loc[mask3, f'{i}gl_bkp']
                               
          
          else:
            mask = (df[var_break] == brk)
            df.loc[mask, f'{i}gl_c'] = (  (np.nan_to_num(df.loc[mask, f'{i}1'] * df.loc[mask, 'g1']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}2'] * df.loc[mask, 'g2']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}3'] * df.loc[mask, 'g3']))
                                      + (np.nan_to_num(df.loc[mask, f'{i}4'] * df.loc[mask, 'g4'])))/ (df.loc[mask, 'g1'] + df.loc[mask, 'g2'] + df.loc[mask, 'g3'] + df.loc[mask, 'g4'])
          mnan = (df[ f'{i}gl_c'].isna())
          df.loc[mnan, f'{i}gl_c'] =  df.loc[mnan, f'{i}gl_bkp']          
           
    df = df.rename(columns=str.upper)
    return df
