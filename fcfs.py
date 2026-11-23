
def fcfs(processos):
    tempo = 0
    fila_prontos = []
    bloqueados = []
    executando = None
    finalizados = 0

    while finalizados < len(processos):

        for processo in processos:
            if processo["chegada"] == tempo:
                processo["estado"] = "pronto"
                fila_prontos.append(processo)

        if executando is None and fila_prontos:
            executando = fila_prontos.pop(0)
            executando["estado"] = "executando"

            if executando["primeira_execucao"] is None:
                executando["primeira_execucao"] = tempo

        if executando is not None:
            executando["restante"] -= 1

        for processo in bloqueados.copy():
            processo["restante"] -= 1

            if processo["restante"] == 0:
                processo["indice"] += 1

                indice = processo["indice"]

                processo["restante"] = processo["atividades"][indice]

                processo["estado"] = "pronto"

                fila_prontos.append(processo)
                bloqueados.remove(processo)

        if executando is not None:
            if executando["restante"] == 0:

                executando["indice"] += 1

                if executando["indice"] == len(executando["atividades"]):
                    executando["estado"] = "finalizado"
                    finalizados += 1

                else:
                    executando["estado"] = "bloqueado"

                    indice = executando["indice"]

                    executando["restante"] = executando["atividades"][indice]

                    bloqueados.append(executando)

                executando = None

        tempo += 1

    soma_respostas = 0

    for processo in processos:
        resposta = processo["primeira_execucao"] - processo["chegada"]
        soma_respostas += resposta
        
    tempo_medio_resposta = soma_respostas / len(processos)
    throughput = finalizados / tempo

    return {
        "tempo_total": tempo,
        "finalizados": finalizados,
        "tempo_medio_resposta": tempo_medio_resposta,
        "throughput": throughput
    }
