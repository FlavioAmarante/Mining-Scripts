# Calcula Fechamento Quimico para bases de dados com Fe3O4

def feq_feo(fe, si, p, al, mn, pf, ti, mg, ca, f3):

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
    f3 = np.nan_to_num(f3)

    fq = -99

    if mn > 2.5:
        fq = round((fe * 1.429729 - (f3 * 0.034550)) + si + p * 2.2913 + al + mn * 1.4368 + pf + ca + mg + ti,3)
    else:
        fq = round((fe * 1.429729 - (f3 * 0.034550)) + si + p * 2.2913 + al + mn * 1.2912 + pf + ca + mg + ti,3)

    if fq > 0:
        return fq
    else:
        return np.nan  
