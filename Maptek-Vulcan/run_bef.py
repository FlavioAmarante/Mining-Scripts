# Run Maptek Vulcan Bef

def run_bef(bmf, lst_befs, estima_ver, pasta):
    import subprocess
    import time

    total_befs = len(lst_befs)
    contador_global = 0
    total_execucoes = sum(len(x) for x in estima_ver)

    inicio_total = time.time()

    for i, bef in enumerate(lst_befs):

        print(f"\n BEF [{i+1}/{total_befs}] -> {bef}")

        for j, versao in enumerate(estima_ver[i]):

            contador_global += 1

            progresso = f"[{contador_global}/{total_execucoes}]"
            nome_exec = f"{bef.replace('.bef','')} | {versao}"

            print(f"\n{progresso} Estimando: {nome_exec}")

            report = f"rep_{bef.replace('.bef','')}_{versao}.bef_report"

            comando = f'djbmest -r "{pasta}\\{report}" "{bmf}" "{pasta}\\{bef}" {versao.upper()}'

            inicio = time.time()

            try:
                resultado = subprocess.run(
                    comando,
                    capture_output=True,
                    text=True,
                    check=True,
                    shell=True
                )

                tempo = time.time() - inicio

                print(f" OK ({tempo:.2f}s)")

                if resultado.stdout:
                    print("----- STDOUT -----")
                    print(resultado.stdout)

                if resultado.stderr:
                    print("----- STDERR -----")
                    print(resultado.stderr)

            except subprocess.CalledProcessError as e:

                tempo = time.time() - inicio

                print(f" ERRO ({tempo:.2f}s)")
                print("----- STDOUT -----")
                print(e.stdout or "")
                print("----- STDERR -----")
                print(e.stderr or "")

                print("\n Interrompendo execução.")
                break

    total_tempo = time.time() - inicio_total
    print(f"\n Tempo total: {total_tempo:.2f}s")
