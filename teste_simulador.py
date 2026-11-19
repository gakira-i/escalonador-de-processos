
from pathlib import Path
from leitorSO import ler_processos
from simuladorSO import Simulador

pasta = Path(__file__).resolve().parent
processos = ler_processos(pasta / "processos.txt")

# Quantum escolhido para o teste.
simulador = Simulador(processos, quantum = 2)

simulador.executar()

print("Histórico da simulação:")

for evento in simulador.historico:
    print(evento)

print("\nTempo total:", simulador.tempo)

print("\nEstados finais:")
for processo in processos:
    print(processo["id"], processo["estado"])
