import random

def generar_numeros_aleatorios():
    """Genera una lista de 5 números aleatorios entre 1 y 50 sin repetirse."""
    return random.sample(range(1, 51), 5)

def pedir_numeros_usuario():
    """Pide al usuario que ingrese 5 números entre 1 y 50 y los valida."""
    while True:
        try:
            # Pedir al usuario que ingrese 5 números
            numeros = input("Introduce 5 números entre 1 y 50, separados por espacio: ")
            numeros_usuario = [int(num) for num in numeros.split()]
            
            # Verificar que el usuario haya ingresado exactamente 5 números válidos
            if len(numeros_usuario) != 5:
                print("Debes ingresar exactamente 5 números.")
                continue
            
            if any(num < 1 or num > 50 for num in numeros_usuario):
                print("Los números deben estar entre 1 y 50.")
                continue
            
            if len(set(numeros_usuario)) != 5:
                print("No puedes repetir números.")
                continue
            
            return numeros_usuario
        except ValueError:
            print("Por favor, ingresa solo números enteros.")

def comparar_resultados(numeros_usuario, numeros_sorteo):
    """Compara los números del usuario con los números sorteados."""
    numeros_acertados = set(numeros_usuario) & set(numeros_sorteo)
    return len(numeros_acertados), numeros_acertados
