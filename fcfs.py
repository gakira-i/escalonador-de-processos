
from simuladorSO import Simulador


class FCFS(Simulador):
    def __init__(self, processos):
        super().__init__(processos)

    def selecionar_processo(self):
        if self.executando is None and self.fila_prontos:
            processo = self.fila_prontos.popleft()
            self.iniciar_execucao(processo)
###E onde está a regra de não preempção?
##Ela está no comportamento conjunto dos dois arquivos.

##No FCFS, não existe nenhum método que interrompa um processo por quantum. Enquanto seu surto de CPU não terminar, self.executando continuará ocupado.

##Por isso, mesmo que outro processo chegue, o processo atual continua executando.