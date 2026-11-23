
def ler_processos(caminho):
    processos = []

    with open(caminho, "r") as arquivo:
        numero = 0

        for linha in arquivo:
            numero += 1
            linha = linha.strip()

            # Ignora linhas vazias.
            if not linha:
                continue

            # Verifica se existe o separador.
            if ":" not in linha:
                raise ValueError(
                    f"Linha {numero}: falta o separador ':'."
                )

            chegada_texto, atividades_texto = linha.split(":", 1)

            # Verifica se os campos estão preenchidos.
            if not chegada_texto.strip() or not atividades_texto.strip():
                raise ValueError(
                    f"Linha {numero}: dados incompletos."
                )

            # Converte o ciclo de chegada.
            try:
                chegada = int(chegada_texto)
            except ValueError:
                raise ValueError(
                    f"Linha {numero}: chegada deve ser um inteiro."
                )

            if chegada < 0:
                raise ValueError(
                    f"Linha {numero}: chegada não pode ser negativa."
                )

            # Converte e valida os tempos de CPU e E/S.
            atividades = []

            for valor in atividades_texto.split(","):
                try:
                    duracao = int(valor)
                except ValueError:
                    raise ValueError(
                        f"Linha {numero}: atividade deve ser um inteiro."
                    )

                if duracao <= 0:
                    raise ValueError(
                        f"Linha {numero}: duração deve ser positiva."
                    )

                atividades.append(duracao)

            # Verifica se a sequência termina com CPU.
            if len(atividades) % 2 == 0:
                raise ValueError(
                    f"Linha {numero}: a sequência deve terminar com CPU."
                )

            # Monta o processo.
            processo = {
                "id": f"P{numero}",
                "chegada": chegada,
                "atividades": atividades,
                "indice": 0,
                "restante": atividades[0],
                "estado": "novo",
                "primeira_execucao": None
            }

            processos.append(processo)

    if not processos:
        raise ValueError("O arquivo não contém processos.")

    return processos

