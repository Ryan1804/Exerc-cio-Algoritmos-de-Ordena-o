import os
import glob
import time

def insertion_sort(A, n):
    tempo_inicial = time.time()

    pivo = None
    for i in range(1, n):
        pivo = A[i]
        j = i - 1
        while j >= 0 and A[j] > pivo:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = pivo

    tempo_final = time.time()
    tempo_iteracao = tempo_final - tempo_inicial

    print(f"Tempo da iteracao(Insertion Sort): {tempo_iteracao:.6f} segundos")

    return tempo_iteracao

def selection_sort(A, n):
    tempo_inicial = time.time()

    for i in range(0, n - 1):
        i_min = i
        for j in range(i + 1, n):
            if A[j] < A[i_min]:
                i_min = j
        if A[i] != A[i_min]:
            temp = A[i]
            A[i] = A[i_min]
            A[i_min] = temp

    tempo_final = time.time()
    tempo_iteracao = tempo_final - tempo_inicial

    print(f"Tempo da iteracao(Selection Sort): {tempo_iteracao:.6f} segundos")

    return tempo_iteracao


def executa_algoritmos():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    arquivos = glob.glob("instancias-num/*.IN")

    for arquivo in arquivos:
        print(f"Processando arquivo: {arquivo}")
        with open(arquivo, 'r') as f:
            lista = [int(linha.strip()) for linha in f]
        
        lista_insertion = lista[:]
        lista_selection = lista[:]
        
        print("Executando Insertion Sort...")
        tempo_insertion_sort = insertion_sort(lista_insertion, len(lista_insertion))

        print("Executando Selection Sort...")
        tempo_selection_sort = selection_sort(lista_selection, len(lista_selection))

        if tempo_insertion_sort < tempo_selection_sort:
            diferenca = tempo_selection_sort - tempo_insertion_sort
            percentual = (diferenca / tempo_selection_sort) * 100
            print(f"Insertion Sort foi mais rapido por {diferenca:.6f} segundos ({percentual:.2f}%).")

        elif tempo_selection_sort < tempo_insertion_sort:
            diferenca = tempo_insertion_sort - tempo_selection_sort
            percentual = (diferenca / tempo_insertion_sort) * 100
            print(f"Selection Sort foi mais rapido por {diferenca:.6f} segundos ({percentual:.2f}%).")

        else:
            print("Ambos os algoritmos tiveram o mesmo tempo de execucao.")

        print()

executa_algoritmos()