
from collections import deque


class Simulador:
    def __init__(self, processos):
        self.processos = processos
        self.tempo = 0
        self.fila_prontos = deque()
        self.bloqueados = []
        self.executando = None
        self.historico = []

    def registrar_chegadas(self):
        for processo in self.processos:
            if (
                processo["estado"] == "novo"
                and processo["chegada"] == self.tempo
            ):
                processo["estado"] = "pronto"
                self.fila_prontos.append(processo)

                self.historico.append(
                    f"Ciclo {self.tempo}: "
                    f"{processo['id']} chegou."
                )

    def todos_finalizados(self):
        return all(
            processo["estado"] == "finalizado"
            for processo in self.processos
        )

    def selecionar_processo(self):
        raise NotImplementedError(
            "O algoritmo deve implementar selecionar_processo()."
        )

    def iniciar_execucao(self, processo):
        self.executando = processo
        processo["estado"] = "executando"

        if processo["primeira_execucao"] is None:
            processo["primeira_execucao"] = self.tempo

        self.historico.append(
            f"Ciclo {self.tempo}: "
            f"{processo['id']} entrou na CPU."
        )

    def executar_ciclo_cpu(self):
        if self.executando is None:
            self.historico.append(
                f"Ciclo {self.tempo}: CPU ociosa."
            )
            return

        processo = self.executando
        processo["restante"] -= 1

        self.historico.append(
            f"Ciclo {self.tempo}: "
            f"{processo['id']} executou CPU. "
            f"Restam {processo['restante']} ciclos."
        )

    def executar_ciclo_es(self):
        for processo in self.bloqueados[:]:
            processo["restante"] -= 1

            self.historico.append(
                f"Ciclo {self.tempo}: "
                f"{processo['id']} executou E/S. "
                f"Restam {processo['restante']} ciclos."
            )

            if processo["restante"] == 0:
                processo["indice"] += 1

                processo["restante"] = processo["atividades"][
                    processo["indice"]
                ]

                processo["estado"] = "pronto"
                self.fila_prontos.append(processo)
                self.bloqueados.remove(processo)

                self.historico.append(
                    f"Ciclo {self.tempo + 1}: "
                    f"{processo['id']} terminou E/S "
                    "e voltou à fila de prontos."
                )

    def finalizar_surto_cpu(self):
        if self.executando is None:
            return

        processo = self.executando

        if processo["restante"] > 0:
            return

        processo["indice"] += 1

        if processo["indice"] < len(processo["atividades"]):
            processo["restante"] = processo["atividades"][
                processo["indice"]
            ]

            processo["estado"] = "bloqueado"
            self.bloqueados.append(processo)

            self.historico.append(
                f"Ciclo {self.tempo + 1}: "
                f"{processo['id']} iniciou E/S."
            )

        else:
            processo["estado"] = "finalizado"

            self.historico.append(
                f"Ciclo {self.tempo + 1}: "
                f"{processo['id']} finalizado."
            )

        self.executando = None

    def verificar_preempcao(self):
        pass

   
    def executar(self):
        while not self.todos_finalizados():
            self.registrar_chegadas()
            self.selecionar_processo()

            self.executar_ciclo_cpu()
            self.executar_ciclo_es()

            self.finalizar_surto_cpu()
            self.verificar_preempcao()

            self.tempo += 1


    def calcular_tempo_medio_resposta(self):
        soma = 0

        for processo in self.processos:
            resposta = (
                processo["primeira_execucao"]
                - processo["chegada"]
            )
            soma += resposta

        media = soma / len(self.processos)

        return media

    def calcular_throughput(self):
        finalizados = 0

        for processo in self.processos:
            if processo["estado"] == "finalizado":
                finalizados += 1

        if self.tempo == 0:
            return 0

        throughput = finalizados / self.tempo

        return throughput
