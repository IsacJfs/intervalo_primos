import numpy as np
print("Calculador de primos")
print("Valores muito grandes podem demorar para serem processados")

numero_coletado = int(input("Digite um número inteiro: \n"))    # Coleta o número que vai ser utlizado
lista_primos = np.array([])   # armazena os números primos calculados
lista_generica = np.array([])
inteiros = np.array([])

array_inicial = np.arange(numero_coletado, 1, -1)

for numero in np.arange(len(array_inicial), 2, -1):
    lista_generica = numero / array_inicial
    inteiros = np.count_nonzero(lista_generica.astype(int) == lista_generica)
    if inteiros == 1:
        lista_primos = np.append(lista_primos, numero)

lista_primos = np.append(lista_primos, [2])
print(f"Existem {len(lista_primos)} números primos de 2 a {numero_coletado}")
print(f"São eles : \n{lista_primos}")


