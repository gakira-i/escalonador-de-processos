
def fcfs(processos):
    tempo = 0
    fila_prontos = []
    bloqueados = []
    executando = None
    finalizados = 0

    while finalizados < len(processos):

        # Verifica a chegada dos processos.
        for processo in processos:
            if processo["chegada"] == tempo:
                processo["estado"] = "pronto"
                fila_prontos.append(processo)

        # Seleciona o primeiro processo da fila.
        if executando is None and fila_prontos:
            executando = fila_prontos.pop(0)
            executando["estado"] = "executando"

            # Registra a primeira execução.
            if executando["primeira_execucao"] is None:
                executando["primeira_execucao"] = tempo

        # Executa um ciclo de CPU.
        if executando is not None:
            executando["restante"] -= 1

        # Executa um ciclo de E/S.
        for processo in bloqueados.copy():
            processo["restante"] -= 1

            # Verifica se a E/S terminou.
            if processo["restante"] == 0:
                processo["indice"] += 1

                indice = processo["indice"]

                processo["restante"] = processo["atividades"][indice]

                processo["estado"] = "pronto"

                fila_prontos.append(processo)
                bloqueados.remove(processo)

        # Verifica se a atividade de CPU terminou.
        if executando is not None:
            if executando["restante"] == 0:

                executando["indice"] += 1

                # Verifica se o processo terminou.
                if executando["indice"] == len(executando["atividades"]):
                    executando["estado"] = "finalizado"
                    finalizados += 1

                # Caso contrário, realiza E/S.
                else:
                    executando["estado"] = "bloqueado"

                    indice = executando["indice"]

                    executando["restante"] = executando["atividades"][indice]

                    bloqueados.append(executando)

                # Libera a CPU.
                executando = None

        # Avança o relógio da simulação.
        tempo += 1

    # Calcula o tempo médio de resposta.
    soma_respostas = 0

    for processo in processos:
        resposta = processo["primeira_execucao"] - processo["chegada"]
        soma_respostas += resposta

    tempo_medio_resposta = soma_respostas / len(processos)

    # Calcula o throughput.
    throughput = finalizados / tempo

    # Retorna os resultados da simulação.
    return {
        "tempo_total": tempo,
        "finalizados": finalizados,
        "tempo_medio_resposta": tempo_medio_resposta,
        "throughput": throughput
    }
