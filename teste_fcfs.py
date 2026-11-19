
from pathlib import Path
from leitorSO import ler_processos
from fcfs import FCFS

pasta = Path(__file__).resolve().parent
processos = ler_processos(pasta / "processos.txt")

fcfs = FCFS(processos)

fcfs.executar()

for evento in fcfs.historico:
    print(evento)

print("\nTempo total:", fcfs.tempo)

for processo in processos:
    print(processo["id"], processo["estado"])

print(
    "Tempo médio de resposta:",
    fcfs.calcular_tempo_medio_resposta()
)

print(
    "Throughput:",
    fcfs.calcular_throughput()
)
