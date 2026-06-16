
def var_mb_check(nome_modelo, pasta_modelo, bin_path=r"C:\Program Files\Maptek\Vulcan 2025\bin\exe"):
    import subprocess
    import os
    import re
    """
    Executa o utilitário 'bhead' para listar as variáveis de um modelo de blocos.
    
    :param nome_modelo: Nome do arquivo (ex: 'bm_cladio_teste_v01.bmf')
    :param pasta_modelo: Caminho da pasta (ex: 'C:\\Dados\\ITA_testes\\Cladio_Project')
    :return: Lista com os nomes das variáveis encontradas
    """
    caminho_completo = os.path.join(pasta_modelo, nome_modelo)
    executable = os.path.join(bin_path, "bhead.exe")
    
    if not os.path.exists(caminho_completo):
        print(f"Erro: Modelo não encontrado em {caminho_completo}")
        return []

    # O bhead exibe as informações no stdout
    cmd = [executable, caminho_completo]
    
    try:
        processo = subprocess.run(cmd, capture_output=True, text=True, check=True)
        saida = processo.stdout
        

        # O bhead geralmente lista as variáveis após um cabeçalho específico.
        # Aqui usamos um Regex para identificar nomes de variáveis comuns
        # Esta lógica depende do formato de saída do bhead da sua versão.
        variaveis = re.findall(r"Variable Name\s+:\s+(\w+)", saida)
        
        # Se a regex não encontrar, exibimos a saída bruta para você conferir
        if not variaveis:
            print("Não foi possível extrair via regex, saída bruta:")
            print(saida)
            
        return variaveis

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar bhead: {e.stderr}")
        return []
