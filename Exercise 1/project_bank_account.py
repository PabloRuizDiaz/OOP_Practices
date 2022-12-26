from datetime import datetime, timezone
import numbers
import itertools


class TimeZone:
    @property
    def time_utc(self):
        return datetime.now(timezone.utc)


class Account:
    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'}
    _deposit_interest_rate = 0.5        # percentage
    _transaction_number = itertools.count()

    def __init__(self, customer_id, first_name, last_name, initial_balance=0):
        self._customer_id = self.check_id_customer(customer_id)
        self._first_name = first_name
        self._last_name = last_name
        self._full_name = None
        self._balance = self.valid_balance(initial_balance)

    ### Check correct ID ###
    @property
    def account_number(self):
        return self._customer_id

    def check_id_customer(self, customer_id):
        if not isinstance(customer_id, numbers.Number):
            raise ValueError('the customer ID must be a number!')
        
        if len(str(customer_id)) != 6:
            raise ValueError('the customer ID must be a number of 6 digits!')
        
        return customer_id
    
    ### Full Name ###
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self.check_names(value, 'First Name')
        self._first_name = value
        self._full_name = None

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.check_names(value, 'Last Name')
        self._last_name = value
        self._full_name = None

    def check_names(self, value, type_value):
        if (value is None) or (len(str(value).strip()) == 0):
            raise ValueError('{} cannot be empty!' .format(type_value))
    
    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = '{}, {}' .format(self._last_name, self._first_name)
        
        return self._full_name

    ### Balance ###
    @property
    def balance(self):
        return self._balance

    def valid_balance(self, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value of balance must be a integral number.')
        
        if value < 0:
            raise ValueError('Value of balance must be equal or more than cero.')
        
        return value

    ### Bank account movements ###
    def deposit(self, value):
        self.check_movement(value, 'deposit')
        
        confirmation = self.confirmation_number(
            Account._transaction_codes['deposit'], 
            self._customer_id)
        
        self._balance += value

        return confirmation

    def withdraw(self, value):
        self.check_movement(value, 'withdraw')

        if value > self.balance:
            confirmation = self.confirmation_number(
                Account._transaction_codes['rejected'],
                self._customer_id)
        
        else:
            confirmation = self.confirmation_number(
                Account._transaction_codes['withdraw'],
                self._customer_id)
                
            self._balance -= value

        return confirmation

    def check_movement(self, value, movement_type):
        if not isinstance(value, numbers.Real) or value <= 0:
            raise ValueError('Amount of {} is not correct!' .format(movement_type))
        
    ### Interest ###
    @classmethod
    def deposit_interest_rate(cls):
        return cls._deposit_interest_rate

    @classmethod
    def set_deposit_interest_rate(cls, value=0):
        if not isinstance(value, numbers.Real) or value < 0:
            raise ValueError('Interest rate is incorrect!')
        
        cls._deposit_interest_rate = value

    def pay_interest(self):
        confirmation = self.confirmation_number(
            Account._transaction_codes['interest'],
            self._customer_id)
        
        self._balance += round((self.balance * Account.deposit_interest_rate() / 100), 2)

        return confirmation

    ### Confirmation Number ###
    def confirmation_number(self, transaction_type, account_id):
        now = TimeZone()
        time_utc = datetime.strftime(now.time_utc, '%Y%m%d%H%M%S')

        self.transaction_code = transaction_type
        self.transaction_id = next(Account._transaction_number)
        self.time_utc = datetime.strftime(now.time_utc, '%Y-%m-%dT%H%M%S')

        return '{}-{}-{}-{}' .format(transaction_type, account_id, time_utc, self.transaction_id)



customer = Account(140568, 'Paul', 'McPeter', 100)
print(customer.__dict__)
print(customer.first_name)
print(customer.last_name)
print(customer.full_name)
customer.last_name = 'MacDonald'
print(customer.full_name)
print(customer.__dict__)
print(customer.balance)
print(customer.deposit(150))
print(customer.balance)
print(customer.withdraw(500))
print(customer.withdraw(50))
