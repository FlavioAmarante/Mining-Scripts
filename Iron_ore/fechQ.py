# Fechamento Químico
def feq(fe, si, p, al, mn, pf, ti, mg, ca):
    import numpy as np
    
    fe = np.nan_to_num(fe)
    si = np.nan_to_num(si)
    p = np.nan_to_num(p)
    al = np.nan_to_num(al)
    mn = np.nan_to_num(mn)
    pf = np.nan_to_num(pf)
    ti = np.nan_to_num(ti)
    mg = np.nan_to_num(mg)
    ca = np.nan_to_num(ca)
    
    fq = -99.00
        
    if mn <= 2.5:
        fq = round((fe  * 1.4297) + si +  (p * 2.2913)  + al + (mn * 1.2912) + pf + ca + mg + ti,3)
    else:
        fq = round((fe  * 1.4297) + si +  (p * 2.2913)  + al + (mn * 1.4369) + pf + ca + mg + ti,3)
        
    if fq > 0:
        return fq
    else:
        return np.nan
