class BankError(Exception):
    def __init__(self, message=""):
        super().__init__()
        self.message = message
    def __str__(self):
        return self.message

class InvalidAmountError(BankError):
    def __init__(self):
        super().__init__("Некорректная сумма")

class InsufficientFundsError(BankError):
    def __init__(self):
        super().__init__("Недостаточно средств")

class AccountBlockedError(BankError):
    def __init__(self):
        super().__init__("Аккаунт заблокирован")

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError
    elif (balance - amount) < 0:
        raise InsufficientFundsError
    return balance - amount

# withdraw(15, 10)
# withdraw(5, 10) - InsufficientFundsError
# withdraw(5, -10) - InvalidAmountError