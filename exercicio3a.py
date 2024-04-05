intervalos_0_25 = 0
intervalos_26_50 = 0
intervalos_51_75 = 0
intervalos_76_100 = 0

while True:
    num = int(input())
    
    if num < 0:
        break
    
    if 0 <= num <= 25:
        intervalos_0_25 += 1
    elif 26 <= num <= 50:
        intervalos_26_50 += 1
    elif 51 <= num <= 75:
        intervalos_51_75 += 1
    elif 76 <= num <= 100:
        intervalos_76_100 += 1

print(f'{intervalos_0_25} {intervalos_26_50} {intervalos_51_75} {intervalos_76_100}')
