# Migra variável entre modelos
def migra_var(mb1,mb2,var,prefixo,tipo,condition,folder_bm,folder_scripts):

    #Necessário script: bm_merge.py

    from maptek import vulcan as vl
    import pandas as pd
    import subprocess    
    
    backgroud = ''
    val = 0
    
    if tipo == 'float':
        backgroud = '-99.0'
        val = 1
    elif tipo == 'integer':
        backgroud = '-99.0'
        val = 1
    elif var == 'lito':
        backgroud = 'vazio'
        val = 1
    elif tipo == 'name':
        backgroud = 'n'
        val = 1
    else:
        print('Tipo não identificado')
        print('Tipos aceitaveis: "float","integer" ou "name"')
        val = 0
        
    if val == 1:
        
        new_var= prefixo+var
        # Verifica e/ou adiciona variáveis aos modelo de blocos
        bmf1 = vl.block_model(r'{}\{}'.format(folder_bm,mb1))
        bmf1.add_variable(new_var, tipo, backgroud, 'variavel auxiliar') 
        bmf1.close()

        bmf2 = vl.block_model(r'{}\{}'.format(folder_bm,mb2))
        bmf2.add_variable(new_var, tipo, backgroud, 'variavel auxiliar') 
        bmf2.close()

        subprocess.call('bexpr {} {} {}'.format(folder_bm+'\\'+mb2,new_var,var))
        subprocess.call('python {}\\bm_merge.py {} {} "{}" {} 0 ""'.format(folder_scripts,folder_bm+'\\'+mb2,folder_bm+'\\'+mb1,condition,new_var))
    
        print('Variável copiada:',new_var)
        print('Modelo de blocos que recebeu a variável:', mb1)
