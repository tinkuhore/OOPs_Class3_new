class bank:

    def transaction(self):
        print('total transaction value')

    def account_oppening(self):
        print('this is ur account status')

    def deposit(self):
        print('this is ur deposit amount')

    def test(self):
        print('this is from bank class')

class hdfc_bank(bank):
    def hdfc_to_icici(self):
        print('this are all ur tranctions with icici')

    def test(self):
        print('this is from hdfc_bank class')

class icici(hdfc_bank):
    pass

x = icici()
x.deposit()
x.test()