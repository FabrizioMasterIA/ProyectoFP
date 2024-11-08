from src.modulo import generar_numeros_aleatorios, pedir_numeros_usuario, comparar_resultados

def main():
    print("¡Bienvenido al sorteo de la lotería!")
    
    # Generar los 5 números sorteados aleatoriamente
    numeros_sorteo = generar_numeros_aleatorios()
    print("Los números sorteados son:", numeros_sorteo)
    
    # Pedir los números al usuario
    numeros_usuario = pedir_numeros_usuario()
    
    # Comparar los números del usuario con los sorteados
    acertados, numeros_acertados = comparar_resultados(numeros_usuario, numeros_sorteo)
    
    # Mostrar el resultado
    if acertados == 5:
        print("¡Felicidades! Has acertado todos los números y has ganado el premio mayor.")
    elif acertados > 0:
        print(f"¡Has acertado {acertados} números! Los números acertados son: {numeros_acertados}.")
    else:
        print("No has acertado ningún número. ¡Sigue participando!")
    
if __name__ == "__main__":
    main()
