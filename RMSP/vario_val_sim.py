# Função valida variograma

def vario_val_sim(dom,simcache,variograms,cmps,wts_var,var_lst,grid_aval,num_real,lags):

    principals = {var: variograms[var].get_principals() for var in var_lst}

    # Build grid searches from principal directions
    gridlags, _ = rmsp.Lags(lags[0],lags[1],lags[2]).get_lags_tols()
    gridsearches = {
        var: rmsp.ExpVarioSearchGrid(p[0]["azm"], p[0]["incl"], gridlags)
        for var, p in principals.items()
    }

    search_dir = {
        var: rmsp.ExpVarioSearch(p[0]["azm"], p[0]["incl"], rmsp.Lags(lags[0],lags[1],lags[2]))
        for var, p in principals.items()}

    # Compute directional experimental variograms from data
    expvarios_dir = {}
    for var in var_lst:
        expvarios_dir[var] = rmsp.ExpVario("traditional").calculate(
            cmps, var, search_dir[var])         
    
    tabs = rmsp.Tabs()
    
    for var in var_lst:
        print(f"\nProcessing {var}...")
    
        sill = rmsp.variance(cmps[var], cmps[wts_var])
    
        gridvario = rmsp.ExpVario(
            standardize=False, sill=sill
        ).calculate_sim(
           simcache,
            var,
            [gridsearches[var]],
            grid_aval.griddef,
            reals=num_real,
            permit_standardized=False,
        )
    
        fig, axes = expvarios_dir[var].gridplot(
            figsize=(6, 4),
            c="C3",
            label="Data Dir.",
            model_kws={"label": "Model"},
            zorder=100,
        )
    
        azm = principals[var][0]["azm"]
        incl = principals[var][0]["incl"]
    
        for i, ax in enumerate(axes):
            gridvario.plot_reals(i, ax=ax, c_avg="k", zorder=-1)
            
        variograms[var].plot_draw(ax, azm, incl, c="C0") 
        
        fig.suptitle(f"Directional Variograms: {var}", fontsize=14)
        fig.savefig(folder_img +'\\'+f"{dom}_{var}_variovarcheck.png")
        
        tabs.add(var, fig)
        
        
    return tabs
