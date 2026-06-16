# Gera E-type Sim

def gerar_etype(folder_path, file_list, output_filename="resultado_etype.csv"):
  import pandas as pd
  import os
    
    lista_dfs = []
    
    print(f"Iniciando processamento de {len(file_list)} arquivos...")

    for i, file_name in enumerate(file_list):
        file_path = os.path.join(folder_path, file_name)
        
        df = pd.read_csv(file_path)

        lista_dfs.append(df)
        
    df_total = pd.concat(lista_dfs)
    
    df_etype = df_total.groupby(['X', 'Y', 'Z'], as_index=False)['Den'].mean()
    
    output_path = os.path.join(folder_path, output_filename)
    df_etype.to_csv(output_path, index=False)
    
    print(f"Sucesso! Arquivo E-type salvo em: {output_path}")
    
    return df_etype
