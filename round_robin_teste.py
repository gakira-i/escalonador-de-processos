

from pathlib import Path
from leitorSO import ler_processos
from round_robin import RoundRobin

pasta = Path(__file__).resolve().parent
processos = ler_processos(pasta / "processos.txt")

rr = RoundRobin(processos, quantum=2)
rr.executar()

print("\nTempos de resposta:")

for processo in processos:
    resposta = (
        processo["primeira_execucao"] - processo["chegada"]
    )

    print(processo["id"], ":", resposta)


for evento in rr.historico:
    print(evento)

print("\nTempo total:", rr.tempo)

for processo in processos:
    print(processo["id"], processo["estado"])

print(
    "Tempo médio de resposta:",
    rr.calcular_tempo_medio_resposta()
)

print(
    "Throughput:",
    rr.calcular_throughput()
)

