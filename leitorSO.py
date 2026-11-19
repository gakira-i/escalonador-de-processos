
def ler_processos(caminho):
    processos = []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, start=1):
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
                chegada = int(chegada_texto.strip())
            except ValueError:
                raise ValueError(
                    f"Linha {numero}: chegada deve ser um inteiro."
                )

            if chegada < 0:
                raise ValueError(
                    f"Linha {numero}: chegada não pode ser negativa."
                )

            # Converte os tempos de CPU e E/S.
            try:
                atividades = [
                    int(valor.strip())
                    for valor in atividades_texto.split(",")
                ]
            except ValueError:
                raise ValueError(
                    f"Linha {numero}: atividades devem ser inteiros."
                )

            # Verifica se as durações são positivas.
            if any(valor <= 0 for valor in atividades):
                raise ValueError(
                    f"Linha {numero}: durações devem ser positivas."
                )



            # Verifica se a sequência termina com CPU.
            if len(atividades) % 2 == 0:
                raise ValueError(
                    f"Linha {numero}: a sequência deve terminar com CPU .")

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


if __name__ == "__main__":
    try:
        processos = ler_processos("processos1.txt")

        print("Arquivo carregado com sucesso!")

        for processo in processos:
            print(processo)

    except FileNotFoundError:
        print("Erro: arquivo processos.txt não encontrado.")

    except ValueError as erro:
        print(f"Erro no arquivo: {erro}")
