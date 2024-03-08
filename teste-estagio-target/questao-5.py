def inverter_string(palavra):
    caracteres_invertidos = []

    for i in range(len(palavra) - 1, -1, -1):
        caracteres_invertidos.append(palavra[i])

    resultado = ''.join(caracteres_invertidos)

    return resultado


entrada = input("Digite uma palavra ou frase: ")
saida = inverter_string(entrada)
print(f"original: {entrada}")
print(f"invertida: {saida}")