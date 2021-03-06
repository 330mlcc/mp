__author__ = 'Administrator'

def useFilter(n):
    return n % 2 == 1

lists = list(filter(useFilter,range(10)))
print(lists)

def myStrip(str):
    return str and str.strip()

lists2 = list(filter(myStrip,['a','','b',None,'c',' ']))
print(lists2)

lists3 = list(range(2,21))
print(lists3)

def main():
    for n in primes():
        if n < 20:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()