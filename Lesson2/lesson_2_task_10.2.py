from math import ceil

def bank(X, Y):
    for _ in range(Y):
        X += X * 0.10  
    return X

in_deposit = 15000  
years = 7              
sum = bank(in_deposit, years)
final_sum = ceil(sum)
print(f"Сумма на счету спустя {years} лет: {final_sum} рублей")