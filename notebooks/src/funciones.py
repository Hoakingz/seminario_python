def calcular_puntos(stats):
    kills, assists, deaths = stats
    return kills * 3 + assists + 1 if deaths else 0

def orden_de_jugadores(round):
    dicc = {}
    for player, stats in round.items():
        dicc[player] = calcular_puntos(stats.values())
    dicc = dict(sorted(dicc.items(),key = lambda item: item[1], reverse=True ))
    return dicc

    
