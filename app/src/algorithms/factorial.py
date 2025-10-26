def calculate_factorial(value: int):
    values = []

    def _helper(n):
        nonlocal values

        if n == 1:
            values.append(1)
            return 1

        factorial = n * _helper(n - 1)
        values.append(factorial)

        return factorial

    _helper(value)

    return values
