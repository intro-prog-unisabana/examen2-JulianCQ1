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
  for i in timer['times']:
    min = timer['times'][0]
    if i < min:
      min = i
    return min
  


def fastest_multi_lap(timer, k):
    times = timer['times']
    n = len(times)
    if k > n and k == 0:
       return None
    min_sum = sum(times[0:k])
    # TODO: Implementar
    pass


def longest_decreasing_streak(timer):
    """
    Retorna la longitud maxima de una secuencia de vueltas consecutivas
    donde los tiempos disminuyen estrictamente.
    """
    # TODO: Implementar
    pass


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
