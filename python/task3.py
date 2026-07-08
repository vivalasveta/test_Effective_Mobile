def prime_factors(n):
    factors = [] #Переменная, в которой мы будем хранить список найденных простых чисел
    divisor = 2 #число, на которое мы пробуем делить
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor) #добавляем число в список
            n = n // divisor
        divisor = divisor + 1
    return factors
