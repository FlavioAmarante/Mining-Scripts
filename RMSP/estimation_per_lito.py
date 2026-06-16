# Função Estimativa por Domínio
def estima_per_dom(comps, msk_comps, bm, msk_bm, lst_lito, lst_vars, k_estimator):
import rmsp
import pandas as pd
    for i in lst_lito:
        if i in lst_lito:
            print("Domain:", i)
            mlt = bm["LITO"] == i
            for j in lst_vars:
                print("Variável:", j)
                estgrid = k_estimator.estimate(
                    bm[(msk_bm & mlt)],
                    comps[(comps.CLI == i) & (msk_comps)],
                    j,
                    output=["estimate", "estimate_var"],
                )
                bm.loc[(msk_bm & mlt), f"{j}"], bm.loc[(msk_bm & mlt), f"{j}_VAR"] = (
                    estgrid["estimate"],
                    estgrid["estimate_var"],
                )
