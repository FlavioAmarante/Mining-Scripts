# Gerador de .bdf para construção do modelo de blocos
def bdf(df,topo,solido,file_path):
    import os
    import pandas as pd
    import numpy as np
    start_file = '''*
*  Written: XX-XX-XXXX 00:00:00*
*'''
    end_file  = '''END$FILE'''

    arq = []
    arq.append(start_file)
      
    # Rotação do modelo
    bearing = float(df['bearing'])
    dip = float(df['dip'])
    plunge = float(df['plunge'])

    #Origin
    ox = float(df['ox'])
    oy = float(df['oy'])
    oz = float(df['oz'])

    # Offset (distância da origem)
    #Start Offset
    xs = float(df['xs'])
    ys = float(df['ys'])
    zs = float(df['zs'])
    #END Offset
    xe = float(df['xe'])
    ye = float(df['ye'])
    ze = float(df['ze'])

    # Bloco sizes (tamanho dos blocos)
    # Parent block size
    px = float(df['px'])
    py = float(df['py'])
    pz = float(df['pz'])
    # Sub-blocks size
    sx = float(df['sx'])
    sy = float(df['sy'])
    sz = float(df['sz'])

    # Condition
    condt = df['condition'][0]

    output = f'''
BEGIN$DEF header
 align_blocks
 bearing={bearing}
 dip={dip}
 n_schemas=2.000000000000
 n_variables=2.000000000000
 plunge={plunge}
 x_origin={ox}
 y_origin={oy}
 z_origin={oz}
END$DEF header
*
BEGIN$DEF variable_1
 default='0'
 description='topografia'
 name='topo'
 type='byte'
END$DEF variable_1
*
BEGIN$DEF variable_2
 default='0'
 description='Marcar estimativa'
 name='ff_expand'
 type='integer'
END$DEF variable_2
*
BEGIN$DEF schema_1
 block_max_x={px}
 block_max_y={py}
 block_max_z={pz}
 block_min_x={px}
 block_min_y={py}
 block_min_z={pz}
 description='parent'
 schema_max_x={xe}
 schema_max_y={ye}
 schema_max_z={ze}
 schema_min_x={xs}
 schema_min_y={ys}
 schema_min_z={zs}
END$DEF schema_1
*
BEGIN$DEF schema_2
 block_max_x={px}
 block_max_y={py}
 block_max_z={pz}
 block_min_x={sx}
 block_min_y={sy}
 block_min_z={sz}
 description='subblocks'
 schema_max_x={xe}
 schema_max_y={ye}
 schema_max_z={ze}
 schema_min_x={xs}
 schema_min_y={ys}
 schema_min_z={zs}
END$DEF schema_2
*
BEGIN$DEF boundary_1
 inversion='None'
 priority=1.000000000000
 projection='Z'
 selection_file=' '
 triangulation='{topo}'
 value='1'
 variable='topo'
END$DEF boundary_1
*
BEGIN$DEF boundary_2
 inversion='None'
 priority=1.000000000000
 projection='Z'
 selection_file=' '
 triangulation='{solido}'
 value='1'
 variable='ff_expand'
END$DEF boundary_2
*
BEGIN$DEF limit_1
 block_max_x={sx}
 block_max_y={sy}
 block_max_z={sz}
 value='1'
 variable='ff_expand'
END$DEF limit_1
*
BEGIN$DEF exception_1
 condition='{condt}'
END$DEF exception_1
*
BEGIN$DEF boundaries
 n_boundaries=2.000000000000
 n_exceptions=1.000000000000
 n_limits=1.000000000000
END$DEF boundaries
*
BEGIN$DEF file_format
 file_format='T'
END$DEF file_format
END$FILE
*    '''
    arq.append(output)    
    arq.append(end_file)
    arq = ''.join(arq)
    
    # Criação do novo arquivo com a extensão .bdf
    bef_file_path = file_path.replace('.txt', '.bdf')

    # Ensure that the directories exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Escrita do novo arquivo
    with open(file_path, 'w') as file:
        file.write(arq)
 
