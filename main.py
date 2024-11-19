from src.modulo import generar_numeros_aleatorios, comparar_resultados

def pedir_numeros_usuario():
    while True:
        try:
            # Pedir al usuario que ingrese 5 números separados por comas
            entrada = input("Por favor, ingresa 5 números separados por comas: ")
            numeros_usuario = [int(num.strip()) for num in entrada.split(",")]
            
            # Verificar que se ingresen exactamente 5 números
            if len(numeros_usuario) != 5:
                print("Debes ingresar exactamente 5 números.")
                continue
            
            return numeros_usuario
        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar solo números enteros separados por comas.")

def main():
    print("¡Bienvenido al sorteo de la lotería!")
    
    # Pedir los números al usuario
    numeros_usuario = pedir_numeros_usuario()
    
    # Generar los 5 números sorteados aleatoriamente
    numeros_sorteo = generar_numeros_aleatorios()
    print("Los números sorteados son:", numeros_sorteo)
    
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
