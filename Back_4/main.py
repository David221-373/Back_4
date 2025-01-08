from functions import *

def main():
    print('-------------------------------------------------------------------------')
    func1(5,1)
    func2(4,2)
    func3(5)
    func4(8)
    func5(30,2)
    func6(3)
    func7('1010110001',4)
    process_numbers(5,4,9)

    account = BankAccount(100)
    try:
        account.withdraw(150)
    except InsufficientBalanceError as e:
        print(e)

    try:
        validate_string_length("1010100101010101011100110101011001011001110100101")
    except ExceedsCharacterLimitError as e:
        print(e)

    func8('skkkkkkkkkkkks ')
    func9()


if __name__ == "__main__":
    main()