def inverter_caracteres(string):
    return ''.join([string[i] for i in range(len(string)-1,-1,-1)])

palavra = input("Digite uma palavra qualquer\n=>")
print(inverter_caracteres(palavra))