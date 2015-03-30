def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum


def fibonacci(n):
    numbs = []
    fib2 = 0
    fib1 = 1
    tmp = 0
    while (n):
        numbs.append(fib1)
        tmp = fib2
        fib2 = fib1
        fib1 = fib2 + tmp
        n -= 1
    return numbs


def sum_of_digits(n):
    n = abs(n)
    sum = 0
    nstr = str(n)
    for i in range(len(nstr)):
        sum += int(nstr[i])
    return sum


def fact_digits(n):
    sum = 0
    while (n > 0):
        sum += factorial(n % 10)
        n = n//10
    return sum


def palindrome(obj):
    st = str(obj)
    bol = True
    for i in range(len(st)):
        if(st[i] != st[len(st)-1-i]):
            bol = False
            break
    return bol


def to_digits(n):
    dig = []
    while(n > 0):
        dig.append(n % 10)
        n = n//10
    dig.reverse()
    return dig


def to_number(digits):
    num = 0
    pos = 1
    digits.reverse()
    for i in digits:
        num += i*pos
        pos *= 10
    return num


def fib_number(n):
    fib_num = fibonacci(n)
    res = ""
    for numb in fib_num:
        res += str(numb)
    return res


def count_vowels(st):
    summ = 0
    lower = st.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for vowel in vowels:
        summ += lower.count(vowel)
    return summ


def count_consonants(st):
    summ = 0
    lower = st.lower()
    vowels = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    for vowel in vowels:
        summ += lower.count(vowel)
    return summ


def char_histogram(string):
    answer = {}
    for i in range(len(string)):
        if string[i] in answer.keys():
            answer[string[i]] += 1
            continue
        else:
            answer[string[i]] = 1
    return answer


def p_score(n):
    summ = 1
    while not palindrome(n):
        summ += 1
        n_reverse = str(n)[::-1]
        n = n + int(n_reverse)
    return summ


def is_increasing(seq):
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]:
            return False
    return True


def is_decreasing(seq):
    for i in range(len(seq)-1):
        if seq[i] <= seq[i+1]:
            return False
    return True


def next_hack(n):
    n += 1
    while not palindrome(bin(n)[2::]) or bin(n)[2::].count('1') % 2 == 0:
        n += 1
    return n
