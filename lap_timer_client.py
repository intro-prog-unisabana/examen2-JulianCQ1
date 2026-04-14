
import lap_timer


def main():
    filename = input("Enter the CSV file name:\n")
    
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
    timer = lap_timer.init(n)
    for _ in range(n):
        time = float(file.readline().strip())
        timer = lap_timer.add_lap(timer, time)
   
    result = lap_timer.longest_decreasing_streak(timer)
    print("Racha decreciente mas larga =", result)
    
 

if __name__ == "__main__":
    main()
