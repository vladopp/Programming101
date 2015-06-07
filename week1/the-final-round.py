import calendar


def count_words(arr):
    dic = {}
    for word in arr:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


def unique_words_count(arr):
    arr2 = []
    for word in arr:
        if word not in arr2:
            arr2.append(word)
    return len(arr2)


def nan_expand(times):
    if times != 0:
        return "Not a " * times + "NaN"
    else:
        return ""


def iteration_of_nan_expand(expanded):
    if expanded[len(expanded)-3:] != 'NaN' and len(expanded[:len(expanded)-3]) % 6 != 0:
        return False
    elif expanded.count("Not a ") != len(expanded[:len(expanded)-3])/6:
            return False
    else:
        return expanded.count("Not a ")


def prime_factorization(n):
    result = []
    cur_divisor = 2
    while n != 1:
        counter = 0
        while n % cur_divisor == 0:
            counter += 1
            n = n // cur_divisor
        if counter != 0:
            result.append((cur_divisor, counter))
        cur_divisor += 1
    return result


def group(ls):
    group = []
    tmp = []
    i = 0
    p = 0
    while i != len(ls):
        while p != len(ls):
            if ls[i] == ls[p]:
                tmp.append(ls[p])
            else:
                break
            p += 1
        group.append(tmp)
        tmp = []
        i = p
    return group


def max_consecutive(items):
    return max([len(x) for x in group(items)])


def group_by(func, seq):
    result = {}
    for elm in seq:
        if func(elm) in result.keys():
            result[func(elm)].append(elm)
        else:
            result[func(elm)] = [elm]
    return result


def list_of_divisors(n):
    divisors = group([1, 1, 1, 2, 3, 1, 1])
    div = 1
    while div <= n:
        if n % div == 0:
            divisors.append(div)
        div += 1
    divisors.reverse()
    return divisors


def prepare_meal(number):
    import math
    n = 0

    for num in list_of_divisors(number):
        if math.log(num, 3) % 1 == 0:
            n = int(math.log(num, 3))
            break
    if number % 5 == 0 and n != 0:
        return "spam " * n + "and eggs"
    elif number % 5 == 0 and n == 0:
        return "eggs"
    else:
        return "spam" * n


def reduce_file_path(path):
    items = path.split("/")
    items = [x for x in items if x != '.' and x != '']

    print(items)

    for i in range(len(items)):
        if len(items) > 0:
            if items[len(items)-1] == '..':
                items.pop()
                if len(items) > 0:
                    items.pop()
    path = "/".join(items)
    path = "/"+path
    return path


def is_an_bn(word):
    if word == "":
        return True

    a = set(word[0:int(len(word) / 2)])
    b = set(word[int(len(word) / 2):])

    if a == {'a'} and b == {'b'} and len(word) % 2 == 0:
        return True

    return False


def is_credit_card_valid(number):
    num = str(number)
    if len(num) % 2 == 0:
        return False

    summ = 0

    for i in range(len(num)):
        if i % 2 == 0:
            summ += int(num[i])
        else:
            asd = int(num[i]) * 2
            while asd != 0:
                summ += (asd % 10)
                asd = asd // 10

    if summ % 10 == 0:
        return True
    else:
        return False


def is_prime(n):
    n = abs(n)
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def goldbach(n):
    result = []
    primes = [x for x in range(2, n + 1) if is_prime(x)]

    for a in primes:
        if a <= n / 2:
            result.append([(a, b) for b in primes if a + b == n])

    return [res[0] for res in result if res != []]


def magic_square(matrix):
    length = len(matrix)
    summ = sum(matrix[0])

    for elm in matrix:
        if summ != sum(elm):
            return False

    for n in range(length):
        tempsum = 0
        for m in range(length):
            tempsum += matrix[m][n]
        if tempsum != summ:
            return False

    diagonal1 = 0

    for i in range(length):
        diagonal1 += matrix[i][i]
    if diagonal1 != summ:
        return False

    diagonal2 = 0

    for p in range(length):
        diagonal2 += matrix[length-1-p][p]
    if diagonal2 != summ:
        return False

    return True


def friday_years(start, end):
    result = 0

    for year in range(start, end + 1):
        fridays_in_year = 0
        for month in range(1, 13):
            weeks = calendar.monthcalendar(year, month)
            for row in weeks:
                if row[4] != 0:
                    fridays_in_year += 1

        if fridays_in_year == 53:
            result += 1

    return result
