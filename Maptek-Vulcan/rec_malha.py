# Calcula Rec. Malha

def rec_malha(MB,lito_ore):
    
    import pandas as pd
    import numpy as np
    from maptek import vulcan as vl
    import subprocess
    
    rm_calc = pd.DataFrame()
    rm_calc['rec_malhan'] = -99.00
    rm_calc['lito'] = 'vazio'

    with vl.block_model(MB, "w") as bm:

        # Carimbo classificação
        rm_calc['dila'] = bm['dila']
        rm_calc['ero'] = bm['ero']
        rm_calc['fegl'] = bm['fegl']
        rm_calc['ik'] = bm['ik']

        # Busca variável Lito
        rm_calc['lito'] = bm['lito']

        rm_calc.replace(-99.00,np.nan, inplace=True)
        m1 = (rm_calc['ik']>=0) & (rm_calc['fegl']>=0) & (rm_calc['lito'].isin(lito_ore))

        med = (m1) & (rm_calc['dila']==1) & (rm_calc['ero']==0)
        ind = (m1) & (rm_calc['dila']==2) & (rm_calc['ero']==0)
        ind2 = (m1) & (rm_calc['dila']==1) & (rm_calc['ero']==1) 
        inf = (m1) & (rm_calc['dila']==2) & (rm_calc['ero']==1) 
        inf2 = (m1) & (rm_calc['dila']==0) & (rm_calc['ero']==1)
        inf3 = (m1) & (rm_calc['dila']==3) & (rm_calc['ero']==1)
        inf4 = (m1) & (rm_calc['dila']==0) & (rm_calc['ero']==0)
        inf5 = (m1) & (rm_calc['dila']==3) & (rm_calc['ero']==0)

        rm_calc.loc[med, 'rec_malhan'] = 1 
        rm_calc.loc[ind, 'rec_malhan'] = 2  
        rm_calc.loc[ind2, 'rec_malhan'] = 2
        rm_calc.loc[inf, 'rec_malhan'] = 3
        rm_calc.loc[inf2, 'rec_malhan'] = 3
        rm_calc.loc[inf3, 'rec_malhan'] = 3
        rm_calc.loc[inf4, 'rec_malhan'] = 3
        rm_calc.loc[inf5, 'rec_malhan'] = 3

        rm_calc.replace(np.nan,-99.00, inplace=True)
        bm['rec_malhan'] = rm_calc['rec_malhan']

    inv = ["'medido'","'indicado'","'inferido'"]   
    for j in range(len(inv)):
        subprocess.call(f'bexpr -C "rec_malhan eq {j+1}" {MB} rec_malha "{inv[j]}"')  
