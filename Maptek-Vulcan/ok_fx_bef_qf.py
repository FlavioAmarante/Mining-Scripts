# Gerador de .bef para Krigagem das faixas

def ok_fx_bef(df,path,file_name):

    file_path = path +'\\'+file_name+'.txt'

    start_file = '''*
*  Written: 23-Jul-2023 17:27:10*
*'''
    end_file  = '''END$FILE'''
    
    arq = []
    arq.append(start_file)
    
    for i in range(df.shape[0]):
  
        bmf = df['bmf'][i] #ok
        condition = df['cond'][i] #ok
        flag = df['flag'][i] 
        database = df['database'][i] #ok
        geocod = df['geocod'][i] #ok
        geocod2 = df['geocod2'][i] #ok
        projeto = df['projeto'][i] #ok

        az = df['az'][i]  #ok
        pl = df['pl'][i] #ok
        dip = df['dip'][i] #ok
        max_sam_oct = df['max_sam_oct'][i].round(12)
        max_samples = df['max_samples'][i].round(12)
        min_samples = float(df['min_samples'][i])
        length = df['length'][i]
        out = df['out'][i]
        fegl_lim = df['fegl_lim'][i]

        major_search   = df['major_search'][i].round(12)
        semi_search    = df['semi_search'][i].round(12)
        minor_search   = df['minor_search'][i].round(12)
        disc_x         = df['disc_x'][i].round(12)
        disc_y         = df['disc_y'][i].round(12)
        disc_z         = df['disc_z'][i].round(12)
        par_block_x    = df['par_block_x'][i].round(12)
        par_block_y    = df['par_block_y'][i].round(12)
        par_block_z    = df['par_block_z'][i].round(12)        
        
        mj_str_1_range = df['mj_str_1_range'][i].round(12)
        mj_str_2_range = df['mj_str_2_range'][i].round(12)
        sm_str_1_range = df['sm_str_1_range'][i].round(12)
        sm_str_2_range = df['sm_str_2_range'][i].round(12)
        mn_str_1_range = df['mn_str_1_range'][i].round(12)
        mn_str_2_range = df['mn_str_2_range'][i].round(12)

        nu =               df['nu'][i].round(12)
        str_1_diff_sill =  df['str_1_diff_sill'][i].round(12)
        str_2_diff_sill =  df['str_2_diff_sill'][i].round(12)
        var_type_1 =       df['var_type_1'][i].round(12)
        var_type_2 =       df['var_type_2'][i].round(12)
        est_id =           df['est_id'][i]
    
        output = f'''
BEGIN$DEF {est_id}_block_centroid
 alt_centroid_x=' '
 alt_centroid_y=' '
 alt_centroid_z=' '
 is_alt_block_centroid='N'
 is_alt_centroid_x='N'
 is_alt_centroid_y='N'
 is_alt_centroid_z='N'
END$DEF hc_block_centroid
*
BEGIN$DEF {est_id}_block_match
 condition='{condition}'
 value_1='{geocod.lower()}'
 variable_1='lito'
END$DEF {est_id}_block_match
*
BEGIN$DEF {est_id}_data_domain
 ignore_w=-99.000000000000
 s_field='GEOCOD'
 BEGIN$TAB select_criteria
   '{length}'
   '{fegl_lim}'
   '{out}'
 END$TAB select_criteria
 BEGIN$TAB select_fields
   'LENGTH'
   'FEGL'
   'OUT'
 END$TAB select_fields
 BEGIN$TAB specific_string
   '{geocod.upper()}'
   '{geocod2.upper()}'
 END$TAB specific_string
 w_field='AFE1'
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
 datasheet='cac'
 dcl_field=' '
 dcl_neg='N'
 decluster='N'
 description=' '
 dist_c_an='ndist'
 dist_c_an_default=-99.000000000000
 environment=' '
 extra_var=1.000000000000
 flag_value={flag}
 flag_variable='flag'
 h_field='DHID'
 h_field_sample_db='DHID'
 identifier='{projeto}{projeto}'
 input_var_1='AFE1'
 input_var_10='AP2'
 input_var_11='AP3'
 input_var_12='AP4'
 input_var_13='AAL1'
 input_var_14='AAL2'
 input_var_15='AAL3'
 input_var_16='AAL4'
 input_var_17='AMN1'
 input_var_18='AMN2'
 input_var_19='AMN3'
 input_var_2='AFE2'
 input_var_20='AMN4'
 input_var_21='ATI1'
 input_var_22='ATI2'
 input_var_23='ATI3'
 input_var_24='ATI4'
 input_var_25='ACA1'
 input_var_26='ACA2'
 input_var_27='ACA3'
 input_var_28='ACA4'
 input_var_29='AMG1'
 input_var_3='AFE3'
 input_var_30='AMG2'
 input_var_31='AMG3'
 input_var_32='AMG4'
 input_var_33='APF1'
 input_var_34='APF2'
 input_var_35='APF3'
 input_var_36='APF4'
 input_var_37='G1'
 input_var_38='G2'
 input_var_39='G3'
 input_var_4='AFE4'
 input_var_40='G4'
 input_var_5='ASI1'
 input_var_6='ASI2'
 input_var_7='ASI3'
 input_var_8='ASI4'
 input_var_9='AP1'
 ivd_distance=' '
 ivd_w_distance=' '
 keys='*'
 kriging_efficiency='ke'
 kriging_efficiency_default=-99.000000000000
 min_samples_1=1.000000000000
 min_samples_10=1.000000000000
 min_samples_11=1.000000000000
 min_samples_12=1.000000000000
 min_samples_13=1.000000000000
 min_samples_14=1.000000000000
 min_samples_15=1.000000000000
 min_samples_16=1.000000000000
 min_samples_17=1.000000000000
 min_samples_18=1.000000000000
 min_samples_19=1.000000000000
 min_samples_2=1.000000000000
 min_samples_20=1.000000000000
 min_samples_21=1.000000000000
 min_samples_22=1.000000000000
 min_samples_23=1.000000000000
 min_samples_24=1.000000000000
 min_samples_25=1.000000000000
 min_samples_26=1.000000000000
 min_samples_27=1.000000000000
 min_samples_28=1.000000000000
 min_samples_29=1.000000000000
 min_samples_3=1.000000000000
 min_samples_30=1.000000000000
 min_samples_31=1.000000000000
 min_samples_32=1.000000000000
 min_samples_33=1.000000000000
 min_samples_34=1.000000000000
 min_samples_35=1.000000000000
 min_samples_36=1.000000000000
 min_samples_37=1.000000000000
 min_samples_38=1.000000000000
 min_samples_39=1.000000000000
 min_samples_4=1.000000000000
 min_samples_40=1.000000000000
 min_samples_5=1.000000000000
 min_samples_6=1.000000000000
 min_samples_7=1.000000000000
 min_samples_8=1.000000000000
 min_samples_9=1.000000000000
 min_valid_1=0.000000000000
 min_valid_10=0.000000000000
 min_valid_11=0.000000000000
 min_valid_12=0.000000000000
 min_valid_13=0.000000000000
 min_valid_14=0.000000000000
 min_valid_15=0.000000000000
 min_valid_16=0.000000000000
 min_valid_17=0.000000000000
 min_valid_18=0.000000000000
 min_valid_19=0.000000000000
 min_valid_2=0.000000000000
 min_valid_20=0.000000000000
 min_valid_21=0.000000000000
 min_valid_22=0.000000000000
 min_valid_23=0.000000000000
 min_valid_24=0.000000000000
 min_valid_25=0.000000000000
 min_valid_26=0.000000000000
 min_valid_27=0.000000000000
 min_valid_28=0.000000000000
 min_valid_29=0.000000000000
 min_valid_3=0.000000000000
 min_valid_30=0.000000000000
 min_valid_32=0.000000000000
 min_valid_33=0.000000000000
 min_valid_34=0.000000000000
 min_valid_35=0.000000000000
 min_valid_36=0.000000000000
 min_valid_37=0.000000000000
 min_valid_38=0.000000000000
 min_valid_39=0.000000000000
 min_valid_4=0.000000000000
 min_valid_40=0.000000000000
 min_valid_5=0.000000000000
 min_valid_6=0.000000000000
 min_valid_7=0.000000000000
 min_valid_8=0.000000000000
 min_valid_9=0.000000000000
 num_holes='nholes'
 num_holes_default=-99.000000000000
 num_samples='ncomp'
 num_samples_default=-99.000000000000
 octants_coded=' '
 octants_used=' '
 output_default_1=-99.000000000000
 output_default_10=-99.000000000000
 output_default_11=-99.000000000000
 output_default_12=-99.000000000000
 output_default_13=-99.000000000000
 output_default_14=-99.000000000000
 output_default_15=-99.000000000000
 output_default_16=-99.000000000000
 output_default_17=-99.000000000000
 output_default_18=-99.000000000000
 output_default_19=-99.000000000000
 output_default_2=-99.000000000000
 output_default_20=-99.000000000000
 output_default_21=-99.000000000000
 output_default_22=-99.000000000000
 output_default_23=-99.000000000000
 output_default_24=-99.000000000000
 output_default_25=-99.000000000000
 output_default_26=-99.000000000000
 output_default_27=-99.000000000000
 output_default_28=-99.000000000000
 output_default_29=-99.000000000000
 output_default_3=-99.000000000000
 output_default_30=-99.000000000000
 output_default_31=-99.000000000000
 output_default_32=-99.000000000000
 output_default_33=-99.000000000000
 output_default_34=-99.000000000000
 output_default_35=-99.000000000000
 output_default_36=-99.000000000000
 output_default_37=-99.000000000000
 output_default_38=-99.000000000000
 output_default_39=-99.000000000000
 output_default_4=-99.000000000000
 output_default_40=-99.000000000000
 output_default_5=-99.000000000000
 output_default_6=-99.000000000000
 output_default_7=-99.000000000000
 output_default_8=-99.000000000000
 output_default_9=-99.000000000000
 output_var_1='afe1'
 output_var_10='ap2'
 output_var_11='ap3'
 output_var_12='ap4'
 output_var_13='aal1'
 output_var_14='aal2'
 output_var_15='aal3'
 output_var_16='aal4'
 output_var_17='amn1'
 output_var_18='amn2'
 output_var_19='amn3'
 output_var_2='afe2'
 output_var_20='amn4'
 output_var_21='ati1'
 output_var_22='ati2'
 output_var_23='ati3'
 output_var_24='ati4'
 output_var_25='aca1'
 output_var_26='aca2'
 output_var_27='aca3'
 output_var_28='aca4'
 output_var_29='amg1'
 output_var_3='afe3'
 output_var_30='amg2'
 output_var_31='amg3'
 output_var_32='amg4'
 output_var_33='apf1'
 output_var_34='apf2'
 output_var_35='apf3'
 output_var_36='apf4'
 output_var_37='g1'
 output_var_38='g2'
 output_var_39='g3'
 output_var_4='afe4'
 output_var_40='g4'
 output_var_5='asi1'
 output_var_6='asi2'
 output_var_7='asi3'
 output_var_8='asi4'
 output_var_9='ap1'
 project='ita'
 samples_file='{database}'
 sg_field='LENGTH'
 slope_of_regression='sr'
 slope_of_regression_default=-99.000000000000
 use_cross_dhid='N'
 use_cross_validation='N'
 use_global_kriging='N'
 use_jacknife='N'
 variable='afe1'
 variable_default=-99.000000000000
 variance='var_krig'
 variance_default=-99.000000000000
 w_field='AFE1'
 wt_mean='wm'
 wt_mean_default=-99.000000000000
 x_field='MIDX'
 y_field='MIDY'
 z_field='MIDZ'
 zero_missing_1='N'
 zero_missing_10='N'
 zero_missing_11='N'
 zero_missing_12='N'
 zero_missing_13='N'
 zero_missing_14='N'
 zero_missing_15='N'
 zero_missing_16='N'
 zero_missing_17='N'
 zero_missing_18='N'
 zero_missing_19='N'
 zero_missing_2='N'
 zero_missing_20='N'
 zero_missing_21='N'
 zero_missing_22='N'
 zero_missing_23='N'
 zero_missing_24='N'
 zero_missing_25='N'
 zero_missing_26='N'
 zero_missing_27='N'
 zero_missing_28='N'
 zero_missing_29='N'
 zero_missing_3='N'
 zero_missing_30='N'
 zero_missing_31='N'
 zero_missing_32='N'
 zero_missing_33='N'
 zero_missing_34='N'
 zero_missing_35='N'
 zero_missing_36='N'
 zero_missing_37='N'
 zero_missing_38='N'
 zero_missing_39='N'
 zero_missing_4='N'
 zero_missing_40='N'
 zero_missing_5='N'
 zero_missing_6='N'
 zero_missing_7='N'
 zero_missing_8='N'
 zero_missing_9='N'
END$DEF {est_id}_data_format
*
BEGIN$DEF {est_id}_krige_parms
 alt_rot_alpha='{az}'
 alt_rot_beta='{dip}'
 alt_rot_zeta='{pl}'
 alt_sd_major_search=' '
 alt_sd_minor_search=' '
 alt_sd_semi_search=' '
 NO_avg_discretize
 box_search='N'
 dh_limit=10.000000000000
 est_dh_max=10.000000000000
 est_dh_min=1.000000000000
 hy_field='AFE1'
 hy_limit=0.000000000000
 hy_major=50.000000000000
 hy_minor=50.000000000000
 hy_semi=50.000000000000
 i_search='O'
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
 max_sam_oct={max_sam_oct}
 max_samples={max_samples}
 min_num_oct=1.000000000000
 min_sam_oct=1.000000000000
 min_samples={min_samples}
 minor_search={minor_search}
 oct_search_plus='N'
 oct_search_type='E'
 parent='P'
 parent_block_x={par_block_x}
 parent_block_y={par_block_y}
 parent_block_z={par_block_z}
 parent_x_var=' '
 parent_y_var=' '
 parent_z_var=' '
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
 user_parent_size='Y'
 x_disc_pnts={disc_x}
 y_disc_pnts={disc_y}
 z_disc_pnts={disc_z}
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
 mj_str_1_range='{mj_str_1_range}'
 mj_str_2_range='{mj_str_2_range}'
 mn_str_1_range='{mn_str_1_range}'
 mn_str_2_range='{mn_str_2_range}'
 nugget={nu}
 num_struct=2.000000000000
 sm_str_1_range='{sm_str_1_range}'
 sm_str_2_range='{sm_str_2_range}'
 str_1_diff_sill={str_1_diff_sill}
 str_1_rot_alpha='{az}'
 str_1_rot_beta='{dip}'
 str_1_rot_zeta='{pl}'
 str_2_diff_sill={str_2_diff_sill}
 str_2_rot_alpha='{az}'
 str_2_rot_beta='{dip}'
 str_2_rot_zeta='{pl}'
 use_bm_variables
 var_type_1={var_type_1}
 var_type_2={var_type_2}
END$DEF {est_id}_str_cutoff_mn
*
BEGIN$DEF {est_id}_type
 type='KNOB'
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
