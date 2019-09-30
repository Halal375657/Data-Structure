def fibonacci(n):
    if n in [1,2]:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def test_fibonacci():
    fibo_list = [1,1,2,3,5,8,13,21,34,55,89]
    for n, f in enumerate(fibo_list):
        assert fibonacci(n+1) == f
