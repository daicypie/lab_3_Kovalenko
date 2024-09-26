import math

def gauss(x, mu=32, sigma=18):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(- ((x - mu) ** 2) / (2 * sigma ** 2))

# print(gauss(1))

# print(gauss (1, mu=32, sigma=18))

x = int(input("Уведіть x: "))

print(f"x= {x}: {gauss(1, mu=32, sigma=18 )}")