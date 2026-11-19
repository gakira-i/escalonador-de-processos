

from simuladorSO import Simulador


class RoundRobin(Simulador):
    def __init__(self, processos, quantum):
        super().__init__(processos)

        if quantum <= 0:
            raise ValueError("O quantum deve ser maior que zero.")

        self.quantum = quantum
        self.tempo_quantum = 0

    def selecionar_processo(self):
        if self.executando is None and self.fila_prontos:
            processo = self.fila_prontos.popleft()
            self.iniciar_execucao(processo)
            self.tempo_quantum = 0

    def executar_ciclo_cpu(self):
        super().executar_ciclo_cpu()

        if self.executando is not None:
            self.tempo_quantum += 1

    def verificar_preempcao(self):
        if self.executando is None:
            return

        if self.tempo_quantum < self.quantum:
            return

        processo = self.executando

        processo["estado"] = "pronto"
        self.fila_prontos.append(processo)

        self.historico.append(
            f"Ciclo {self.tempo + 1}: "
            f"{processo['id']} esgotou o quantum "
            "e voltou à fila de prontos."
        )

        self.executando = None
        self.tempo_quantum = 0

    
