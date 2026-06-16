# Gerador de .bef para NN da densidade        
def nn_den_bef(df,path,file_name):
    
    file_path = path +'\\'+file_name+'.txt'

    start_file = '''*
*  Written: 23-Jul-2023 17:27:10*
*'''
    end_file  = '''END$FILE'''
    
    arq = []
    arq.append(start_file)
    
    for i in range(df.shape[0]):
  
        bmf = df['bmf'][i]
        condition = df['cond'][i]
        database = df['database'][i]
        geocod = df['geocod'][i]
        projeto = df['projeto'][i]
        flag = df['flag'][i]
        setor = df['setor'][i]

        az = df['az'][i]
        pl = df['pl'][i]
        dip = df['dip'][i]
        
        aniso_x=df['aniso_x'][i]
        aniso_y=df['aniso_y'][i]
        aniso_z=df['aniso_z'][i]
        major_search   = df['major_search'][i]
        semi_search    = df['semi_search'][i]
        minor_search   = df['minor_search'][i]
    
        est_id = df['est_id'][i]
          
        output = f'''
BEGIN$DEF {est_id}_block_centroid
 alt_centroid_x=' '
 alt_centroid_y=' '
 alt_centroid_z=' '
 is_alt_block_centroid='N'
 is_alt_centroid_x='N'
 is_alt_centroid_y='N'
 is_alt_centroid_z='N'
END$DEF {est_id}_block_centroid
*
BEGIN$DEF {est_id}_block_match
 condition='{condition}'
 value_1='{geocod.lower()}'
 variable_1='lito'
END$DEF {est_id}_block_match
*
BEGIN$DEF {est_id}_data_domain
 maximum_w=100.000000000000
 minimum_w=-98.000000000000
 s_field='GEOCOD'
 select_criteria='{setor}'
 select_fields='SETOR'
 specific_string='{geocod.upper()}'
 w_field='DEN'
END$DEF {est_id}_data_domain
*
BEGIN$DEF {est_id}_data_format
 aniso_distance=' '
 aniso_w_distance=' '
 avg_distance_default=0.000000000000
 cart_distance=' '
 cart_w_distance=' '
 cross_dhid=' '
 cross_smp_from_fld=' '
 cross_smp_name_fld=' '
 cross_smp_to_fld=' '
 datasheet='den'
 dcl_field=' '
 dcl_neg='N'
 decluster='N'
 description=' '
 environment='cvrd'
 extra_var=0.000000000000
 flag_value={flag}
 flag_variable='flag_dens_nn'
 identifier='{projeto}{projeto}'
 input_var_1='DEN'
 ivd_distance=' '
 ivd_w_distance=' '
 keys='*'
 min_samples_1=1.000000000000
 min_valid_1=0.000000000000
 octants_coded=' '
 octants_used=' '
 output_default_1=-99.000000000000
 output_var_1='dens_n_nn'
 project='{projeto}'
 samples_file='{database}'
 use_cross_dhid='N'
 use_cross_validation='N'
 use_global_kriging='N'
 use_jacknife='N'
 variable='dens_n_nn'
 variable_default=-99.000000000000
 w_field='DEN'
 x_field='MIDX'
 y_field='MIDY'
 z_field='MIDZ'
 zero_missing_1='N'
END$DEF {est_id}_data_format
*
BEGIN$DEF {est_id}_krige_parms
 alt_rot_alpha='{az}'
 alt_rot_beta='{dip}'
 alt_rot_zeta='{pl}'
 alt_sd_major_search=' '
 alt_sd_minor_search=' '
 alt_sd_semi_search=' '
 aniso_x={aniso_x}
 aniso_y={aniso_y}
 aniso_z={aniso_z}
 NO_avg_discretize
 box_search='N'
 dh_limit=10.000000000000
 est_dh_max=10.000000000000
 est_dh_min=1.000000000000
 hy_field='DEN'
 hy_limit=0.000000000000
 hy_major=50.000000000000
 hy_minor=50.000000000000
 hy_semi=50.000000000000
 i_search='N'
 is_alt_rot_alpha='Y'
 is_alt_rot_beta='Y'
 is_alt_rot_zeta='Y'
 is_alt_sd_major_search='N'
 is_alt_sd_minor_search='N'
 is_alt_sd_semi_search='N'
 is_std_rot_alpha='N'
 is_std_rot_beta='N'
 is_std_rot_zeta='N'
 is_std_sd_major_search='Y'
 is_std_sd_minor_search='Y'
 is_std_sd_semi_search='Y'
 krige_mean=0.000000000000
 lmvar=' '
 major_search={major_search}
 max_sam_oct=1.000000000000
 max_samples=1.000000000000
 min_num_oct=1.000000000000
 min_sam_oct=1.000000000000
 min_samples=1.000000000000
 minor_search={minor_search}
 oct_search_plus='N'
 oct_search_type='E'
 parent='I'
 parent_block_x=0.000000000000
 parent_block_y=0.000000000000
 parent_block_z=0.000000000000
 parent_x_var=' '
 parent_y_var=' '
 parent_z_var=' '
 power=2.000000000000
 read_parent_size='N'
 rot_alpha=0.000000000000
 rot_beta=0.000000000000
 rot_zeta=0.000000000000
 sel_by_cart_dist='N'
 semi_search={semi_search}
 tol_duplicates=0.000000000000
 use_dh_limit='N'
 use_est_limit='N'
 use_hy_limit='N'
 user_parent_size='N'
 x_disc_pnts=1.000000000000
 y_disc_pnts=1.000000000000
 z_disc_pnts=1.000000000000
END$DEF {est_id}_krige_parms
*
BEGIN$DEF {est_id}_postik
 grade_over=' '
 grade_under=' '
 hyperbolic='N'
 ikmean=' '
 ikvariance=' '
 ivtype=0.000000000000
 ltpar=1.000000000000
 max_disc=70.000000000000
 mpar=1.000000000000
 prob=0.000000000000
 prob_for_value=' '
 utpar=1.000000000000
 value_for_prob=' '
 varred=0.000000000000
 zmax=10.000000000000
 zmin=1.000000000000
 zvalue=0.000000000000
END$DEF {est_id}_postik
*
BEGIN$DEF {est_id}_remote
 count=0.000000000000
END$DEF {est_id}_remote
*
BEGIN$DEF {est_id}_soft_bound
 n_bound=0.000000000000
 soft_field=' '
END$DEF {est_id}_soft_bound
*
BEGIN$DEF {est_id}_spec_version
 version='15.4.0.1140.ef6667be'
END$DEF {est_id}_spec_version
*
BEGIN$DEF {est_id}_str_cutoff_mn
 nugget=0.100000000000
 num_struct=0.000000000000
 NO_use_bm_variables
END$DEF {est_id}_str_cutoff_mn
*
BEGIN$DEF {est_id}_type
 type='KNIS'
 version='V15.4'
END$DEF {est_id}_type
*    '''
        arq.append(output)    
    arq.append(end_file)
    arq = ''.join(arq)
    
    # Criação do novo arquivo com a extensão .bef
    bef_file_path = file_path.replace('.txt', '.bef')

    # Escrita do novo arquivo
    with open(bef_file_path, 'w') as file:
        file.write(arq)
