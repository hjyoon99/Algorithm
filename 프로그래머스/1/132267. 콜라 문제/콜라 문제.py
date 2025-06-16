def solution(a, b, n):
    count = 0;
    while(n >= a):
        exchange = n // a
        get = exchange * b
        count += get
        n = n % a + get
    return count