# Junta arquivo .las ara .csv
def las_to_csv(folder_path, output_file,step):
    import os
    import pandas as pd
    import lasio
    import numpy as np
    dfs = []
    for file in os.listdir(folder_path):
        if file.endswith(".las"):
            las = lasio.read(os.path.join(folder_path, file))
            df = las.df()
            df['WELL'] = os.path.splitext(file)[0]
            df['ST'] = las.well.STRT.value
            df['END'] = las.well.STOP.value
            df['WL'] = las.params.WLEV.value
            dfs.append(df)
    merged_df = pd.concat(dfs)
    merged_df = merged_df.reset_index()
    merged_df['FROM'] = merged_df['DEPT']
    
    df_grouped = merged_df.groupby('WELL')
    
    def calc_val(group):
        prev_depth = None
        results = []
        for _, row in group.iterrows():
            current_depth = row["FROM"]
            if prev_depth is None:
                results.append([0, current_depth])
            else:
                results.append([prev_depth, current_depth])
            prev_depth = current_depth
        return results

    # Apply the calculation to each group
    result_df = df_grouped.apply(calc_val).explode()

    # Combine column names
    result_df .columns = ["prev_depth", "current_depth"]
    res = result_df.to_frame(name='from_to')
    res = res.reset_index()
    res = res.assign(FROM = lambda df: df.from_to.map(lambda v: v[0]), TO = lambda df: df.from_to.map(lambda v: v[1]))
    merged_df['DE'] = res['FROM']
    merged_df['ATE'] = res['TO']
    merged_df['FURO'] = merged_df['WELL'].str.replace(f'_{step}', '')
    merged_df.replace(np.nan,-99.00, inplace=True)
    merged_df.to_csv(output_file, index=False)
    merged_df.replace(-99.00,np.nan, inplace=True)
    return merged_df
