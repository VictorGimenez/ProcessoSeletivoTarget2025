def fib(n,num):
    vetor_fibo=[]
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
        vetor_fibo.append(a)
        if(num == a):
            print(f"O número {num} está na sequẽncia de fibonacci")
    return vetor_fibo

num_input = int(input("Informe um número que deseja saber se está ou não na sequência de fibonacci\n=>"))
limite = int(input("Informe um número até onde deseja imprimir a sequência de fibonacci\n=>"))
print(fib(limite,num_input))