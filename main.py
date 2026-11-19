
from pathlib import Path

from leitorSO import ler_processos
from fcfs import FCFS
from round_robin import RoundRobin
from simuladorSO import Simulador


pasta = Path(__file__).resolve().parent

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

    processos = ler_processos(pasta / "processos.txt")
    simulador: Simulador
    if opcao == "1":
        simulador = FCFS(processos)

    elif opcao == "2":
        quantum = int(input("Informe o quantum: "))
        simulador = RoundRobin(processos, quantum)

    simulador.executar()

    print("\n=== HISTÓRICO DA SIMULAÇÃO ===")

    for evento in simulador.historico:
        print(evento)

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

    print("Tempo total:", simulador.tempo)
    print(
        "Tempo médio de resposta:",
        simulador.calcular_tempo_medio_resposta()
    )
    print(
        "Throughput:",
        simulador.calcular_throughput()
    )

    print("\nDeseja realizar outra simulação?")
    print("1 - Sim")
    print("0 - Não")

    repetir = input("Escolha: ")

    if repetir == "0":
        print("Simulador encerrado.")
        break
