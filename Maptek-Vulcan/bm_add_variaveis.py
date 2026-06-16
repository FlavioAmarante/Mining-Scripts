def bm_add_variaveis(caminho_modelo, dicionario_vars):
    import os
    import subprocess
    if not os.path.exists(caminho_modelo):
        print(f"Erro: Modelo não encontrado em {caminho_modelo}")
        return

    cmd = ["bedvar", caminho_modelo]

    input_str = ""

    for nome, (default, tipo, desc) in dicionario_vars.items():

        # 🔴 Correção importante para tipo name
        if tipo == 'name' and default == 'vazio':
            default = "''"   # Vulcan precisa string vazia válida

        input_str += f"+ {nome} {tipo} {default}\n"

    try:
        processo = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = processo.communicate(input=input_str)

        print("STDOUT:\n", stdout)
        print("STDERR:\n", stderr)

        if processo.returncode == 0:
            print("Processo finalizado — verifique o modelo.")
        else:
            print(f"Erro ao rodar bedvar: {stderr}")

    except Exception as e:
        print(f"Erro inesperado: {e}")
