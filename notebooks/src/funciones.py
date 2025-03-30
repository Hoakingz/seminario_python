def calcular_puntos(stats):
    kills, assists , deaths = stats
    return kills * 3 + assists + ((-1) if deaths else 0)

def orden_de_jugadores(round):
    dicc = {}
    for player, stats in round.items():
        dicc[player] = calcular_puntos(stats.values())
    dicc_sorted = dict(sorted(dicc.items(),key = lambda item: item[1], reverse=True ))
    return dicc_sorted

def inicializar_valores(round):
    dicc_inicializado={}
    for player in round.keys():
        if player not in dicc_inicializado:
            dicc_inicializado[player] = dict(kills =0,assists = 0,deaths= 0, MVP = 0,points= 0)
    return dicc_inicializado
