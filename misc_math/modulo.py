import timeit
from sympy.ntheory import divisors
from memory_profiler import profile


@profile
def factoring(n):
    a=range(1,n)
    return a,divisors(n, generator=True)
@profile
def fibo(n):
    a =list(fib(n))
    return a

def fib(n):
    a,b =0,1
    while a<n:
        a , b = b,a+b
        yield a
    




if __name__ == '__main__':
    starttime = timeit.default_timer()
    a=list(fibo(100000000000000000000000000000000))
    print(a)
    endtime = timeit.default_timer()