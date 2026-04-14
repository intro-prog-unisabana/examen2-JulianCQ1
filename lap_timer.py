# lap_timer.py
# Libreria de funciones para registrar tiempos de vuelta en una carrera.
#
# Estructura del diccionario (timer):
#   - 'max':   numero maximo de vueltas permitidas (int)
#   - 'times': lista con los tiempos de cada vuelta (list)
#   - 'total': tiempo acumulado de todas las vueltas (float)


def init(max_laps):
    vueltas = {
        'max': max_laps,
        'times': [],
        'total': 0.0
    }
    return vueltas


def add_lap(timer, time):
    if len(timer['times']) >= timer['max']:
        return timer 
    timer['times'].append(time)
    timer['total'] += time
    return timer



def count(timer):
   count = len(timer['times'])
   return count
    


def cumulative_time(timer):
    total = timer['total']
    return total

def format_laps(timer):
   x = str(timer['times'])
   return x
  


def fastest_lap(timer):
    times = timer['times']
    if not times:
        return None

    fastest = times[0]
    for t in times:
        if t < fastest:
            fastest = t

    return fastest


def fastest_multi_lap(timer, k):
    times = timer['times']
    n = len(times)
    if k > n and k >= 0:
       return None
    min_sum = sum(times[0:k])
    current_sum = min_sum
    for i in range(k, n):
        current_sum += times[i] - times[i - k]
        if current_sum < min_sum:
            min_sum = current_sum
    return min_sum

def longest_decreasing_streak(timer):
    times = timer['times']
    if not times:
        return 0
    max_streak = 1
    current_streak = 1
    for i in range(1, len(times)):
        if times[i] < times[i - 1]:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 1 
    return max_streak
 
  

def main():
    # crear un cronometro para el record mundial de 100m de Usain Bolt,
    # dividiendo la carrera en 10 segmentos (o "vueltas")
    timer = init(10)
    timer = add_lap(timer, 1.85)
    timer = add_lap(timer, 1.02)
    timer = add_lap(timer, 0.91)
    timer = add_lap(timer, 0.87)
    timer = add_lap(timer, 0.85)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.83)
    timer = add_lap(timer, 0.90)

    # imprimir estadisticas
    print("numero de vueltas =", count(timer))                    # 10
    print("tiempo acumulado =", cumulative_time(timer))           # 9.69
    print("vuelta mas rapida =", fastest_lap(timer))              # 0.82
    print("50m mas rapidos =", fastest_multi_lap(timer, 5))       # 4.14
    print("racha mas larga =", longest_decreasing_streak(timer))  # 6

    # imprimir tiempos
    # [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.9]
    print(format_laps(timer))


if __name__ == "__main__":
    main()
