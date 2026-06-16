# Calcula Índice de Risco e Classifica Inventário Mineral

def cls_ir(MB,ir_med_max,ir_ind_max,setor,lito_ore):

    from maptek import vulcan as vl
    import pandas as pd
    import numpy as np
    import subprocess

    #ir_calc = pd.DataFrame()
    
    lst_vars = ['lito','fegl','nholes','setor']
    
    ir_calc = bmf_get([MB],lst_vars)
    
    ir_calc['ir'] = -99.00
    ir_calc['inventoryn'] = -99.00
    
    with vl.block_model(MB, "w") as bm:

        # Reset variável
        var_default_ir = bm.field_default('ir')
        var_ir = bm['ir']   
        var_ir.fill(var_default_ir)
        bm['ir'] = var_ir
        var_default_cls = bm.field_default('inventoryn')
        var_cls = bm['inventoryn']   
        var_cls.fill(var_default_cls)
        bm['inventoryn'] = var_cls
    
        # Calculo do IR
        ik_val = bm['ik']
        mask1 = (ik_val>=0) & (ir_calc['lito'].isin(lito_ore))
        ir_calc['ik'] = bm['ik']
        ir_calc['var_ik'] = bm['var_ik']
        ir_calc.replace(-99.00,np.nan, inplace=True)
        ir_calc.loc[mask1, 'ir'] = np.sqrt(((1 - ir_calc['ik'])**2) + ((ir_calc['var_ik'])**2))

        # Dataframe para BM
        ir_calc.replace(np.nan,-99.00, inplace=True)
        bm['ir'] = ir_calc['ir']
 
        # Carimbo classificação
        
        ir_calc.replace(-99.00,np.nan, inplace=True)
        
        inf = (ir_calc['ik']>=0) & (ir_calc['fegl']>=0) & (ir_calc['lito'].isin(lito_ore)) & (ir_calc['setor'].isin(setor))
        ind = (inf) & (ir_calc['ir']>=ir_med_max) & (ir_calc['ir']<ir_ind_max)
        med = (inf) & (ir_calc['ir']>=0) & (ir_calc['ir']<ir_med_max)
        ind2 = (med) & (ir_calc['nholes']<2)

        ir_calc.loc[inf, 'inventoryn'] = 3
        ir_calc.loc[ind, 'inventoryn'] = 2
        ir_calc.loc[med, 'inventoryn'] = 1
        ir_calc.loc[ind2, 'inventoryn'] = 2
    
        # Dataframe para BM
        ir_calc.replace(np.nan,-99.00, inplace=True)
        bm['inventoryn'] = ir_calc['inventoryn']
        
    inv = ["'medido'","'indicado'","'inferido'"]

    for j in range(len(inv)):
        subprocess.call(f'bexpr -C "inventoryn eq {j+1}" {MB} inventory "{inv[j]}"')
