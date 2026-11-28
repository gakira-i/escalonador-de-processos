SIMULADOR DE ESCALONAMENTO DE PROCESSOS EM SISTEMAS OPERACIONAIS


Disciplina: Sistemas Operacionais

Instituicao: Universidade Estadual de Maringa (UEM)

Linguagem: Python

1. DESCRIÇÃO GERAL

Este projeto implementa um simulador baseado em ciclos de clock para

avaliação comparativa de algoritmos de escalonamento de processos em uma única

CPU (com operações de Entrada/Saida paralelas e sem custo de troca de

contexto).



Algoritmos implementados:

FCFS (First-Come First-Served): Não preemptivo.

Round Robin (RR): Preemptivo por fatia de tempo (quantum).



Métricas calculadas ao final da simulação:

Tempo total de simulação (ciclos de clock);

Quantidade de processos finalizados;

Tempo médio de resposta (TMR);

Vazão (Throughput);

Turnaround médio e tempo médio de espera.


2. REQUISITOS E COMPILAÇÃO

Por ser desenvolvido em Python, não há necessidade de geracao de binário

ou compilação prévia do código-fonte.

Requisitos:

Python 3.8 ou superior instalado no sistema operacional;

Utiliza apenas bibliotecas padrao do Python.


3. ESTRUTURA DO ARQUIVO DE ENTRADA

O simulador lê um arquivo de texto (.txt) onde cada linha representa um processo

no seguinte formato:

  <CI>: <TCPU1>, <TES1>, <TCPU2>, <TES2>, ..., <TCPUn>

Onde:

<CI>    : Ciclo de clock inicial em que o processo chega ao sistema.

<TCPUi> : Quantidade de ciclos de clock exigidos na CPU na i-ésima rajada.

<TESi>  : Quantidade de ciclos de clock gastos na operação de E/S.



Observações sobre o formato:

Toda linha deve iniciar e terminar com um valor de rajada de CPU.

Linhas em branco e linhas iniciadas com '#' (comentarios) sao ignoradas.



Exemplo válido de arquivo de entrada (processos.txt):

  # Carga de trabalho de referencia

  0: 3, 9, 5, 15, 2

  1: 15, 5, 3

  4: 6, 1, 25, 2, 23, 4, 9

  5: 1, 20, 3, 25, 2

  9: 7, 2, 9, 1, 8, 1, 20, 1, 18, 3, 9


4. PASSO A PASSO PARA EXECUCAO E PARAMETRIZACAO

Abra o terminal na pasta raiz do projeto e execute o simulador conforme a

interface utilizada no script principal:

A) Execução via linha de comando (CLI):

   Sintaxe:

     python main.py <arquivo_entrada> <algoritmo> [quantum]



   Parâmetros:

    <arquivo_entrada> : Caminho para o arquivo .txt com os processos.

    <algoritmo>       : 'fcfs' para FCFS ou 'rr' para Round Robin.

    [quantum]         : Inteiro positivo representando o quantum em ciclos de

                           clock (obrigatorio apenas quando algoritmo = 'rr').



   Exemplos de execução:

     1. Executar com FCFS:

        python main.py entrada.txt fcfs



     2. Executar com Round Robin (quantum = 2 ciclos):

        python main.py entrada.txt rr 2



     3. Executar com Round Robin (quantum = 5 ciclos):

        python main.py entrada.txt rr 5



     4. Executar com Round Robin (quantum = 10 ciclos):

        python main.py entrada.txt rr 10



     5. Executar com Round Robin (quantum = 20 ciclos):

        python main.py entrada.txt rr 20



B) Execução direta pelo codigo (caso nao utilize argumentos CLI):

   Abra o arquivo main.py, localize o bloco principal `if __name__ == "__main__":`

   e ajuste as variaveis de configuracao:



     arquivo = "entrada.txt"   # Nome/caminho do arquivo de entrada

     quantum = 2               # Valor inteiro > 0 para o Round Robin



   Em seguida, execute no terminal:

     python main.py


5. DECLARAÇÃO DE USO DE INTELIGÊNCIA ARTIFICIAL

Em conformidade com as diretrizes da disciplina e o guia de uso de IA da UEM,

ferramentas de IA generativa foram utilizadas exclusivamente como apoio

conceitual na validação da logica de simulação por ciclos e na revisão

estrutural da documentação. Todo o código-fonte e os experimentos

foram implementados, testados e compreendidos pelos autores.
