# Calcula Fechamento Químico no dataframe
def calc_fechaq(df1,var_break,brk,inplace=True):    
    import numpy as np
    import pandas as pd

    df = df1.copy()
    
    df.reset_index()
    df = df.rename(columns=str.upper)
    #mask = (df[var_break] == brk)

    if inplace == True:
        print('Fechamento químico substituição')
        for i in df.index:
            if df.loc[i,var_break]==brk:
                df.loc[i,'FQGL']=feq(df.loc[i,'FEGL'],df.loc[i,'SIGL'],df.loc[i,'PGL'],df.loc[i,'ALGL'],df.loc[i,'MNGL'],df.loc[i,'PFGL'],df.loc[i,'TIGL'],df.loc[i,'MGGL'],df.loc[i,'CAGL'])
                df.loc[i,'FQ1']=feq(df.loc[i,'FE1'],df.loc[i,'SI1'],df.loc[i,'P1'],df.loc[i,'AL1'],df.loc[i,'MN1'],df.loc[i,'PF1'],df.loc[i,'TI1'],df.loc[i,'MG1'],df.loc[i,'CA1'])
                df.loc[i,'FQ2']=feq(df.loc[i,'FE2'],df.loc[i,'SI2'],df.loc[i,'P2'],df.loc[i,'AL2'],df.loc[i,'MN2'],df.loc[i,'PF2'],df.loc[i,'TI2'],df.loc[i,'MG2'],df.loc[i,'CA2'])
                df.loc[i,'FQ3']=feq(df.loc[i,'FE3'],df.loc[i,'SI3'],df.loc[i,'P3'],df.loc[i,'AL3'],df.loc[i,'MN3'],df.loc[i,'PF3'],df.loc[i,'TI3'],df.loc[i,'MG3'],df.loc[i,'CA3'])
                df.loc[i,'FQ4']=feq(df.loc[i,'FE4'],df.loc[i,'SI4'],df.loc[i,'P4'],df.loc[i,'AL4'],df.loc[i,'MN4'],df.loc[i,'PF4'],df.loc[i,'TI4'],df.loc[i,'MG4'],df.loc[i,'CA4'])
              
    
    else:
        print('Fechamento químico nova variável *_C')
        for i in df.index:
            if df.loc[i,var_break]==brk:
                df.loc[i,'FQGL_C']=feq(df.loc[i,'FEGL'],df.loc[i,'SIGL'],df.loc[i,'PGL'],df.loc[i,'ALGL'],df.loc[i,'MNGL'],df.loc[i,'PFGL'],df.loc[i,'TIGL'],df.loc[i,'MGGL'],df.loc[i,'CAGL'])
                df.loc[i,'FQ1_C']=feq(df.loc[i,'FE1'],df.loc[i,'SI1'],df.loc[i,'P1'],df.loc[i,'AL1'],df.loc[i,'MN1'],df.loc[i,'PF1'],df.loc[i,'TI1'],df.loc[i,'MG1'],df.loc[i,'CA1'])
                df.loc[i,'FQ2_C']=feq(df.loc[i,'FE2'],df.loc[i,'SI2'],df.loc[i,'P2'],df.loc[i,'AL2'],df.loc[i,'MN2'],df.loc[i,'PF2'],df.loc[i,'TI2'],df.loc[i,'MG2'],df.loc[i,'CA2'])
                df.loc[i,'FQ3_C']=feq(df.loc[i,'FE3'],df.loc[i,'SI3'],df.loc[i,'P3'],df.loc[i,'AL3'],df.loc[i,'MN3'],df.loc[i,'PF3'],df.loc[i,'TI3'],df.loc[i,'MG3'],df.loc[i,'CA3'])
                df.loc[i,'FQ4_C']=feq(df.loc[i,'FE4'],df.loc[i,'SI4'],df.loc[i,'P4'],df.loc[i,'AL4'],df.loc[i,'MN4'],df.loc[i,'PF4'],df.loc[i,'TI4'],df.loc[i,'MG4'],df.loc[i,'CA4'])      
    
    df = df.rename(columns=str.upper)
    return df
