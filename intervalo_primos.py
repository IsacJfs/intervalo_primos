print("Calculador de primos")
print("Valores muito grandes podem demorar para serem processados")

numero_coletado = int(input("Digite um número inteiro: \n"))    # Coleta o número que vai ser utlizado
lista_primos = []   # armazena os números primos calculados
lista_generica = []  # lista que armazena resultado das divisões antes de determinar se o valor é primo

for principal in range(numero_coletado, 1, -1):
    # Laço criado com range que vai do número digitado até 1 com passo de -1
    lista_generica.clear()  # limpa a lista genérica a cada ciclo do for
    for secundario in range(2, principal):
        # laço onde o resto da divisão de todos os números contidos entre dois e o principal e o número secundário
        # serão armazenados
        valor = principal % secundario
        lista_generica.append(valor)
    if not 0 in lista_generica:
        # Confere se existe alguma divisão com resto zero, caso não, o número é primo
        lista_primos.append(principal)

print(f"Existem {len(lista_primos)} números primos de 2 a {numero_coletado}")
print(f"São eles : \n{lista_primos}")
