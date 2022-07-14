class bank:

    def transaction(self):
        print('total transaction value')

    def account_oppening(self):
        print('this is ur account status')

    def deposit(self):
        print('this is ur deposit amount')

    def test(self):
        print('this is a test method from bank class')

class hdfc_bank:
    def hdfc_to_icici(self):
        print('this are all ur transactions with icici')

    def test(self):
        print('this is a method from hdfc_bank class')

class ineuron_bank :
    def account_status_icici(self):
        print('printing account status in icici')

class icici( hdfc_bank,bank, ineuron_bank):
    pass

i = icici()
i.deposit()
i.hdfc_to_icici()
i.transaction()
i.account_oppening()
i.test()
i.account_status_icici()