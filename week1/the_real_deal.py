def sum_of_divisors(n):
    summ = 0
    for i in range(1, n + 1):
        if n % i == 0:
            summ += i
    return summ


def is_prime(n):
    n = abs(n)
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_number_of_divisors(n):
    summ = 0
    for i in range(1, n + 1):
        if n % i == 0:
            summ += 1
    return is_prime(summ)


def contains_digit(number, digit):
    number = str(number)
    digit = str(digit)
    if number.count(digit) > 0:
        return True
    return False


def contains_digits(number, digits):
    number = str(number)
    for digit in digits:
        if number.count(str(digit)) == 0:
            return False
    return True


def is_number_balanced(n):
    n = str(n)
    if len(n) == 1:
        return True
    first = n[:len(n)//2]
    if len(n) % 2 == 1:
        second = n[len(n)//2 + 1:]
    else:
        second = n[len(n)//2:]
    summ = 0
    for i in range(len(first)):
        summ += int(first[i])
    for i in range(len(second)):
        summ -= int(second[i])
    if summ == 0:
        return True
    return False


def count_substrings(haystack, needle):
    return haystack.count(needle)


def zero_insert(n):
    n = str(n)
    result = n[0]
    for i in range(len(n) - 1):
        if n[i] == n[i+1] or int(n[i]) + int(n[i+1]) == 10:
            result = result + '0' + n[i+1]
        else:
            result += n[i+1]
    return int(result)


def sum_matrix(m):
    summ = 0
    for i in m:
        summ += sum(i)
    return summ
