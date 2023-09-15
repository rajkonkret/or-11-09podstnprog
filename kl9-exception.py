class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # raise MyException("Wystąpił wyjątek")  # rzucenie wyjątku
    # raise ZeroDivisionError  # - można rzucac tez wyjątki wbudowane w pythona : ZeroDivisionError
    print(2 / 0)  # ZeroDivisionError: division by zero
except MyException:
    print("wystąpił wyjątek MyException")  # wystąpił wyjątek MyException
except Exception as e:
    print("Błąd", e)

# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\or-11-09podstnprog\
#   kl9-exception.py", line 6, in <module>
#     raise MyException("Wystąpił wyjątek")
# MyException: Wystąpił wyjątek

print("Nadal działam")  # Nadal działam
# 11:15