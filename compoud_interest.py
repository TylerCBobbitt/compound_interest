principal = float(input('Enter the principal amount: '))
rate = float(input('Enter the rate : '))
years = int(input('Enter the number of years to save: '))

amount = principal

for year in range(years):
    print(year + 1, end=' ')
    amount = amount * (1 + rate)
    print(round(amount, 2))
