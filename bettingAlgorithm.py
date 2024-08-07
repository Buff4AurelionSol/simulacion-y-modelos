import random
from tabulate import tabulate
import pandas as pd

SALDO_INICIAL = 100

def hacer_apuesta(saldo_actual):
    if saldo_actual < 5:
        return saldo_actual
    apuesta_maxima = min(100, saldo_actual)  # La apuesta no puede exceder el saldo actual
    apuesta = random.randint(5, apuesta_maxima)
    return apuesta

def comprobar_juego(dado):
    return dado % 2 == 0

def jugar():
    saldo_actual = SALDO_INICIAL
    perdidas_acumuladas = 0
    ganancias_acumuladas = 0 

    while perdidas_acumuladas < 100 and ganancias_acumuladas <= 500:
        dado = random.randint(1, 6)
        if comprobar_juego(dado):
            apuesta = 2 * hacer_apuesta(saldo_actual)
            saldo_actual += apuesta
            ganancias_acumuladas += apuesta
        else: 
            apuesta = hacer_apuesta(saldo_actual)
            saldo_actual -= apuesta
            perdidas_acumuladas += apuesta
        
        # Si el saldo actual es negativo, el jugador no puede seguir jugando
        if saldo_actual <= 0:
            break

    resultados = [ganancias_acumuladas, perdidas_acumuladas]
    return resultados

if __name__ == "__main__":
    numero_ganadores = 0
    numero_perdedores = 0
    juegos = []
    total_ganancias = 0
    total_perdidas = 0

    for i in range(500):
        resultados = jugar()
        juego_num = i + 1
        estado = "GANADOR" if resultados[0] >= 500 else "PERDEDOR"
        juegos.append([juego_num, estado, resultados[0], resultados[1]])
        total_ganancias += resultados[0]
        total_perdidas += resultados[1]
        if estado == "GANADOR":
            numero_ganadores += 1 
        else:
            numero_perdedores += 1

    # Calcular promedios
    promedio_ganancias = total_ganancias / 500
    promedio_perdidas = total_perdidas / 500

    # Mostrar resultados de cada juego en consola
    headers = ["Juego Número", "Estado", "Ganancias", "Pérdidas"]
    print(tabulate(juegos, headers, tablefmt="grid"))

    # Guardar los resultados en un archivo CSV
    df = pd.DataFrame(juegos, columns=headers)
    df.to_csv('resultados_juegos.csv', index=False)
    
    # Mostrar resumen
    resumen = [
        ["Número de ganadores", numero_ganadores],
        ["Número de perdedores", numero_perdedores],
        ["Promedio de ganancias", promedio_ganancias],
        ["Promedio de pérdidas", promedio_perdidas]
    ]
    print("\nRESUMEN")
    print(tabulate(resumen, tablefmt="grid"))
