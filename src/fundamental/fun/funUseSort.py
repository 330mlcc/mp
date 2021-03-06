__author__ = 'Administrator'

#lists = sorted([36, 5, -12, 9, -21])
#print('sorted([36, 5, -12, 9, -21]) : ',lists)

#lists1 = sorted([36, 5, -12, 9, -21], key=abs)
#print('sorted([36, 5, -12, 9, -21], key=abs) : ',lists1)

def main():
    for n in primes():
        if n < 10:
            print('the main funcation, the value is : ',n)
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