from leitorSO import ler_processos
from fcfs import fcfs
from round_robin import round_robin


while True:
    print("\n=== SIMULADOR DE ESCALONAMENTO ===")
    print("1 - FCFS")
    print("2 - Round Robin")
    print("0 - Sair")

    opcao = input("Escolha o algoritmo: ")

    if opcao == "0":
        print("Simulador encerrado.")
        break

    if opcao != "1" and opcao != "2":
        print("Opção inválida. Tente novamente.")
        continue


    try:
        processos = ler_processos("processos.txt")
    except (ValueError, OSError) as erro:
        print("Erro na leitura:", erro)
        continue

    if opcao == "1":
        resultados = fcfs(processos)

    elif opcao == "2":

        try:
            quantum = int(input("Informe o quantum: "))
        except ValueError:
            print("O quantum deve ser um número inteiro.")
            continue

        if quantum <= 0:
            print("O quantum deve ser positivo.")
            continue

        resultados = round_robin(processos, quantum)

    print("\n=== RESULTADOS ===")

    for processo in processos:
        resposta = (
            processo["primeira_execucao"]
            - processo["chegada"]
        )

        print(
            f"{processo['id']}: "
            f"estado = {processo['estado']}, "
            f"tempo de resposta = {resposta}"
        )


    print("\nTempo total:", resultados["tempo_total"])
    print("Processos finalizados:", resultados["finalizados"])
    print("Tempo médio de resposta:", resultados["tempo_medio_resposta"])
    print("Throughput:", resultados["throughput"])


    print("\nDeseja realizar outra simulação?")
    print("1 - Sim")
    print("0 - Não")

    repetir = input("Escolha: ")

    while repetir != "1" and repetir != "0":
        print("Opção inválida. Tente novamente.")
        repetir = input("Escolha: ")

    if repetir == "0":
        print("Simulador encerrado.")
        break