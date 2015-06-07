import copy


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


NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)]


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):

    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result
