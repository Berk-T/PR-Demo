def sum(a, b):
    return a + b


def multiply(a, b):
    result = 1
    for _ in range(b):
        result = sum(result, a)
    return result
