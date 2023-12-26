import functools

def safe_calculator(func):
    @functools.wraps(func)
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)


result = calculate("2 + 2")
print(result)

result = calculate("10 / 0")
print(result)