def verifica_fibonacci(n):
    a=0 ; b=1
    while b < n:
        a, b = b, a + b
    if b == n:
        print(f"{n} pertence à sequência de Fibonacci.")
    else:
        print(f"{n} não pertence à sequência de Fibonacci.")

numero = int(input("Informe um número: "))
verifica_fibonacci(numero)
