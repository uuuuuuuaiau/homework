import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"The function {func.__name__}  was completed in {execution_time} seconds")
        return result
    return wrapper

@timing_decorator
def example_function():
    time.sleep(2)
    print("function completed")

example_function()

import unittest

class TestTimingDecorator(unittest.TestCase):

    def test_execution_time(self):
        @timing_decorator
        def test_function():
            time.sleep(1)
            return "Test function completed"

        result = test_function()
        self.assertEqual(result, "Test function completed")

if __name__ == '__main__':
    unittest.main()