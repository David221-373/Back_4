''' П1 Минимум 2 разные функции, которые принимают на вход один или несколько параметров.
Функции ДОЛЖНЫ выбрасывать исключение при определённых значениях входных параметров.
Функции НЕ ДОЛЖНЫ содержать никаких обработчиков исключений. '''

def func1(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def func2(a,b):
    if isinstance(a,str) or isinstance(b,str):
        raise TypeError
    return a*b

''' П2 Функция, которая принимает на вход один или несколько параметров.  
Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.  
Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть 
какая-нибудь логика, связанная с обработкой исключения.  
Обработчик НЕ ДОЛЖЕН содержать блок finally.'''

def func3(value):
    try:
        if value < 0:
            raise ValueError("Отрицательное значение не допускается.")
        elif value == 0:
            raise ValueError("Нулевое значение не допускается.")

        print(f"Обрабатываю значение: {value}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

''' П3 Функция, которая принимает на вход один или несколько параметров.
Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть
какая-нибудь логика, связанная с обработкой исключения.
Обработчик ДОЛЖЕН содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.'''

def func4(value):
    success = False
    try:
        if value < 0:
            raise ValueError('Отрицательные значения не допускаются')
        elif value == 0:
            raise ZeroDivisionError('Нулевые значения не допускаются')

        print(f'Обработка значения: {value}')
        success = True

    except Exception as e:
        print(f'Произошла ошибка: {e}')

    finally:
        if success:
            print('Функция обработала данные корректно')
        elif not success:
            print('Некорректный ввод данных')

        print('Функция завершила выполнение')

''' П4 Минимум 3 разные функции, которые принимают на вход один или несколько параметров.  
Функции ДОЛЖНЫ выбрасывать исключения при определённых значениях входных параметров.  
Функции ДОЛЖНЫ содержать НЕСКОЛЬКО обработчиков РАЗНЫХ типов исключений (минимум 3 типа исключений). Внутри блоков обработки исключения 
ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.  
Каждый обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.'''

def func5 (a, b):
    try:
        result = a / b
        return result
    except TypeError as te:
        print(f"Ошибка: {te}. Убедитесь, что оба параметра являются числами.")
    except ValueError as ve:
        print(f"Ошибка: {ve}. Проверьте значение делителя.")
    except Exception as e:
        print(f'Неизвестная ошибка{e}')
    finally:
        print("Завершение работы функции divide_numbers.")

def func6 (x):
    try:
        if x < 0:
            raise ArithmeticError("Квадратный корень из отрицательного числа не может быть вычислен.")
        result = x ** 0.5
        return result
    except ArithmeticError as ae:
        print(f"Ошибка: {ae}. Пожалуйста, введите неотрицательное число.")
    except TypeError as te:
        print(f"Ошибка: {te}. Убедитесь, что введено число.")
    except Exception as e:
        print(f'Неизвестная ошибка{e}')
    finally:
        print("Завершение работы функции calculate_square_root.")

def func7(str1, str2):
    try:
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError("Оба параметра должны быть строками.")
        if len(str1) == 0 or len(str2) == 0:
            raise ValueError("Строки не должны быть пустыми.")
        result = str1 + str2
        return result
    except TypeError as te:
        print(f"Ошибка: {te}. Убедитесь, что оба параметра являются строками.")
    except ValueError as ve:
        print(f"Ошибка: {ve}. Пожалуйста, проверьте длину строк.")
    except Exception as e:
        print(f"Ошибка: {e}. Произошла непредвиденная ошибка.")
    finally:
        print("Завершение работы функции func7.")


''' П5 Функция, которая принимает на вход один или несколько параметров.  
Функция ДОЛЖНА генерировать исключения при определённых условиях (в Python есть конструкция для генерации исключений).  
Функция ДОЛЖНА содержать обработчики всех исключений, которые генерируются внутри этой функции. Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.  
Обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
'''


def process_numbers(*args):
    try:
        if len(args) == 0:
            raise ValueError("Необходимо передать хотя бы один аргумент.")

        total = 0
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError(f"Неверный тип: {num}. Ожидались числа.")
            if num < 0:
                raise ValueError(
                    f"Отрицательное число: {num}. Ожидались только положительные числа.")

            total += num

        return total

    except ValueError as ve:
        print(f"Ошибка: {ve}. Пожалуйста, проверьте переданные значения.")
    except TypeError as te:
        print(f"Ошибка: {te}. Убедитесь, что все аргументы являются числами.")
    except Exception as e:
        print(f"Ошибка: {e}. Произошла непредвиденная ошибка.")

    finally:
        print("Завершение работы функции process_numbers.")


''' П6 Минимум 3 разных пользовательских исключения и примеры их использования'''
class MyCustomError1 (Exception):
    def __init__(self, message):
        if message:
            self.message = message
        else:
            self.message = "No text"

    def __str__(self):

        if self.message:
            return f'MyCustomError, {self.message}'
        else:
            return 'MyCustomError has been raised'



# raise MyCustomError1('')
########################################################################################################################

class InsufficientBalanceError(Exception):
    """Исключение, возникающее при недостаточном балансе на счете."""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Недостаточно средств на счете.")
        self.balance -= amount
        print(f"Снято: {amount}, оставшийся баланс: {self.balance}")

account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientBalanceError as e:
    print(e)

########################################################################################################################
class ExceedsCharacterLimitError(Exception):
    """Исключение, возникающее при превышении лимита символов в строке."""
    pass

def validate_string_length(message):
    max_length = 30
    if len(message) > max_length:
        raise ExceedsCharacterLimitError(f"Строка превышает максимальный лимит в {max_length} символов.")
    print(f"Строка '{message}' соответствует требованиям.")

try:
    validate_string_length("Это очень длинная строка, которая явно превышает лимит.")
except ExceedsCharacterLimitError as e:
    print(e)


'''П7  Функция, которая принимает на вход один или несколько параметров.  
Функция ДОЛЖНА выбрасывать пользовательское исключение, созданное на шаге 6. при определённых значениях входных параметров.  
Функция ДОЛЖНА содержать МИНИМУМ ОДИН обработчик исключений. Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.  
Обработчик МОЖЕТ содержать блок finally.'''


def func8(message):
    try:
        if isinstance(message, str):
            validate_string_length(message)
            print(f'Ваша строка: {message} ')
        else:
            print('Вы ввели число, а надо строку')
    except ExceedsCharacterLimitError as e:
        print(f'Произошла ошибка {e}')

#func8('101010100110100101010110011010111001110111010010101')
#func8(8)


''' П8 Минимум 3 функции, демонстрирующие работу исключений.  
Алгоритм функций необходимо придумать самостоятельно'''

class NumbersError(Exception):
    pass
class EvenError(NumbersError):
    pass

class NegativeError(NumbersError):
    pass

def no_even(numbers):
    if all(x % 2 != 0 for x in numbers):
        return True
    raise EvenError("В списке не должно быть чётных чисел")


def no_negative(numbers):
    if all(x >= 0 for x in numbers):
        return True
    raise NegativeError("В списке не должно быть отрицательных чисел")


def func9():
    print("Введите числа в одну строку через пробел:")
    try:
        numbers = [int(x) for x in input().split()]
        if no_negative(numbers) and no_even(numbers):
            print(f"Сумма чисел равна: {sum(numbers)}.")
    except NumbersError as e:
        print(f"Произошла ошибка: {e}.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}.")

