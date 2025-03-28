def calcular_puntos(stats):
    kills, assists, deaths = stats.value()
    return kills * 3 + assists + 1 if deaths else 0



