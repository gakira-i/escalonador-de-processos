# A pesquisa feita para implementação do código foi feita em inglês, sendo assim, alguns termos estão no idioma (Ex: FCFS [First Come First Served])

def ordenacao(processo):
    return processo[0]

def fcfs(nomeArquivo):
    processos = []
    try:
        with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print(f"O arquivo '{nomeArquivo}' não foi encontrado.")
        return

    # Leitura e processamento das linhas do arquivo
    for i, linha in enumerate(linhas):
        linhaLimpa = linha.strip()
        if not linhaLimpa:
            continue
        
        partes = linhaLimpa.split(":")
        ci = int(partes[0].strip()) # ci: Ciclo Inicial
        ciclos = [int(v.strip()) for v in partes[1].split(",")]
        pid = f"p{i+1}" # pid: ID do Processo
        totalCpu = sum(ciclos[0::2])
        totalEs = sum(ciclos[1::2])
        
        # Estrutura do processo: [ci, ciclos, faseAtual, tempoRestanteFase, pid, totalCpu, totalEs]
        processos.append([ci, ciclos, 0, ciclos[0], pid, totalCpu, totalEs])

    if not processos:
        print("O arquivo não contém processos válidos para simulação.")
        return

    # Ordena utilizando a primeira função criada
    processos.sort(key=ordenacao)

    tempo = 0
    filaProntos = []
    bloqueados = []
    finalizados = []
    
    linhaTempo = []
    atual, inicioBloco = None, 0

    while len(finalizados) < len(processos):
        # Chegada de novos processos com base no CI e no tempo atual do relógio
        while processos and processos[0][0] <= tempo:
            filaProntos.append(processos.pop(0))

        # Atualiza E/S (processos bloqueados)
        novos_prontos = []
        for p in bloqueados:
            p[3] -= 1  # Decrementa o tempo restante da fase de E/S
            if p[3] == 0:
                p[2] += 1  # Avança para a próxima fase (que será de CPU)
                p[3] = p[1][p[2]]  # Define o tempo da nova fase de CPU
                novos_prontos.append(p)
        
        for p in novos_prontos:
            bloqueados.remove(p)
            filaProntos.append(p)

        # Execução na CPU
        status = "Parado"
        if filaProntos:
            p = filaProntos.pop(0)
            status = p[4]
            
            p[3] -= 1  # Executa 1 ciclo de clock na CPU
            
            if p[3] == 0:
                if p[2] + 1 < len(p[1]):  # Se ainda tem fases de E/S pendentes
                    p[2] += 1
                    p[3] = p[1][p[2]]
                    bloqueados.append(p)
                else:  # Terminou todas as fases de CPU e E/S
                    ct = tempo + 1
                    tt = ct - p[0]
                    wt = tt - p[5] - p[6]
                    finalizados.append([p[4], ct, tt, wt])
            else:
                filaProntos.insert(0, p)

        # Agrupa a linha do tempo para evitar repetições excessivas
        if status != atual:
            if atual is not None:
                linhaTempo.append(f"[{inicio_bloco} -> {tempo}] {atual}")
            atual, inicio_bloco = status, tempo

        tempo += 1

    if atual is not None:
        linhaTempo.append(f"[{inicio_bloco} -> {tempo}] {atual}")

    # Exibição dos resultados organizados
    print(f"--- Relatório da Simulação (Arquivo: {nomeArquivo}) ---")
    print("\nLinha do tempo compactada:")
    for bloco in linhaTempo:
        print(bloco)

    print("\nResultados Finais [CT (Término), TT (Turnaround), WT (Espera)]:")
    for p in sorted(finalizados):
        print(f"{p[0]}: Término={p[1]}, Turnaround={p[2]}, Espera={p[3]}")

if __name__ == "__main__":
    arquivoEntrada = "exemplo_entrada.txt"
    fcfs(arquivoEntrada)