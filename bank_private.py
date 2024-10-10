#Создаем класс
class BankAccount:
    #создаем базовые параметры
    def __init__(self, balance):
        #создаем приватную переменную чтобы скрыть ее значения до вывода
        self.__balance = balance # приватная переменная
    #создаем функцию по прибавлению к переменной баланс
    def deposit(self, amount):
        if amount > 0: # проверка прибавления
            self.__balance += amount #прибавление

    #функция по вычитанию из баланса
    def withdraw(self, amount):
        if amount <= self.__balance: # проверка что размер вычита не меньше чем баланс
            self.__balance -= amount # вычитание из баланса
        else: #если не подходит условию
            print("Недостаточно средств") # печатание что нет среств
    #сохранение новой инфы
    def get_balance(self):
        return self.__balance #сохранялка
account=BankAccount(1000) #нач баланс
account.deposit(500) # прибавление
print(account.get_balance()) #печатание новой сохраненной инфы