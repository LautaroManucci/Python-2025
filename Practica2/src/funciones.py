def calcular_puntos(kills, assists, deaths, puntos):
    return kills * puntos['kill'] + assists * puntos['assist'] + deaths * puntos['death']

def procesar_ronda(round_data, players, puntos):
    round_scores = {}
    
    for player, stats in round_data.items():
        kills = stats['kills']
        assists = stats['assists']
        deaths = 1 if stats['deaths'] else 0
        
        points = calcular_puntos(kills, assists, deaths, puntos)
        
        if player not in players:
            players[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0}
        
        players[player]['kills'] += kills
        players[player]['assists'] += assists
        players[player]['deaths'] += deaths
        players[player]['points'] += points
        round_scores[player] = points
    
    mvp = max(round_scores, key=round_scores.get)
    players[mvp]['mvps'] += 1

def mostrar_ranking(titulo, ranking):
    print(titulo)
    print("Jugador   Kills  Asistencias  Muertes  MVPs  Puntos")
    print("-"*55)
    for player, stats in ranking:
        print(f"{player:<11} {stats['kills']:<9} {stats['assists']:<10} {stats['deaths']:<6} {stats['mvps']:<6} {stats['points']:<6}")
    print("-"*55)
    print()