# class Triangle:
#     def __init__(self, side1, side2, side3, corner1, corner2, corner3):
#         if (side1 > 0 and side2 > 0 and side3 > 0 and corner1 > 0 and corner2 > 0 and corner3 > 0 and 180 == corner1 +
#                 corner2 + corner3 and side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
#             self.__side1 = side1
#             self.__side2 = side2
#             self.__side3 = side3
#             self.__corner1 = corner1
#             self.__corner2 = corner2
#             self.__corner3 = corner3
#         else:
#             print('Вы создали не треугольник!')
#
#     def set_side1(self, side1):
#         if side1 > 0:
#             self.__side1 = side1
#         else:
#             print('Сторона треугольника не может быть меньше 0!')
#
#     def set_side2(self, side2):
#         if side2 > 0:
#             self.__side2 = side2
#         else:
#             print('Сторона треугольника не может быть меньше 0!')
#
#     def set_side3(self, side3):
#         if side3 > 0:
#             self.__side3 = side3
#         else:
#             print('Сторона треугольника не может быть меньше 0!')
#
#     def set_corner1(self, corner1):
#         if corner1 > 0:
#             self.__corner1 = corner1
#         else:
#             print('Угол треугольника не может быть меньше 0!')
#
#     def set_corner2(self, corner2):
#         if corner2 > 0:
#             self.__corner2 = corner2
#         else:
#             print('Угол треугольника не может быть меньше 0!')
#
#     def set_corner3(self, corner3):
#         if corner3 > 0:
#             self.__corner3 = corner3
#         else:
#             print('Угол треугольника не может быть меньше 0!')
#
#     def get_side1(self):
#         return self.__side1
#
#     def get_side2(self):
#         return self.__side2
#
#     def get_side3(self):
#         return self.__side3
#
#     def get_corner1(self):
#         return self.__corner1
#
#     def get_corner2(self):
#         return self.__corner2
#
#     def get_corner3(self):
#         return self.__corner3
#
#     def perimetr(self):
#         if (self.__side1 + self.__side2 > self.__side3 and self.__side1 + self.__side3 > self.__side2 and self.__side2 +
#                 self.__side3 > self.__side1):
#             return self.__side1 + self.__side2 + self.__side3
#         else:
#             print('Треугольник не существует!')
#
#     def square(self):
#         if (self.__side1 + self.__side2 > self.__side3 and self.__side1 + self.__side3 > self.__side2 and self.__side2 +
#                 self.__side3 > self.__side1):
#             p = self.__side1 + self.__side2 + self.__side3
#             s = (p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3)) ** 0.5
#             return s
#         else:
#             print('Треугольник не существует!')
#
#     def theViewIs(self):
#         if (self.__side1 > 0 and self.__side2 > 0 and self.__side3 > 0 and self.__corner1 > 0 and self.__corner2 > 0 and
#                 self.__corner3 > 0 and 180 == self.__corner1 + self.__corner2 + self.__corner3 and
#                 self.__side1 + self.__side2 > self.__side3 and self.__side1 + self.__side3 > self.__side2 and
#                 self.__side2 + self.__side3 > self.__side1):
#             if (self.__side1 == self.__side2 and self.__side3 == self.__side2 and
#                     self.__corner1 == self.__corner2 == self.__corner3 == 60):
#                 print('Вы создали равносторонний треугольник!')
#             if (self.__side1 ** 2 == self.__side2 ** 2 + self.__side3 ** 2 or
#                     self.__side2 ** 2 == self.__side3 ** 2 + self.__side1 ** 2 or
#                     self.__side3 ** 2 == self.__side1 ** 2 + self.__side2 ** 2 and self.__corner1 == 90 and
#                     self.__corner1 == self.__corner2 + self.__corner3 or self.__corner2 == 90 and
#                     self.__corner2 == self.__corner3 + self.__corner1 or
#                     self.__corner3 == 90 and self.__corner3 == self.__corner1 + self.__corner2):
#                 print('Вы создали прямоугольный треугольник!')
#             if self.__side1 == self.__side2 or self.__side2 == self.__side3 or self.__side1 == self.__side3:
#                 print('Вы создали равнобедренный треугольник!')
#         else:
#             print('Вы создали не треугольник!')
#
#
# trig = Triangle(10, 10, 10, 60, 60, 60)
# trig.theViewIs()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Money:
#     def __init__(self, coin, penny):
#         self.__coin = coin
#         self.__penny = penny
#
#     def set_coin(self, coin):
#         self.__coin = coin
#
#     def set_penny(self, penny):
#         self.__penny = penny
#
#     def get_coin(self):
#         return self.__coin
#
#     def get_penny(self):
#         return self.__penny
#
#     def __str__(self):
#         return f'{self.__coin},{self.__penny}'
#
#     def addMoney(self, money):
#         return Money(self.__coin + money.__coin, self.__penny + money.__penny)
#
#     def subMoney(self, money):
#         return Money(abs(self.__coin - money.__coin), abs(self.__penny - money.__penny))
#
#
# someMoney = Money(1, 2)
# someMoney2 = Money(3, 4)
# print(someMoney.addMoney(someMoney2))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import os
#
#
# class Bankomat:
#     def __init__(self):
#         self.__money = 0
#         self.__idBankomat = 'HB2342NF5432'
#
#     def getMoney(self):
#         return self.__money
#
#     def setMoney(self, money):
#         self.__money = self.__money + money
#
#     def subMoney(self, money):
#         if money > self.__money:
#             print('Недостаточно средств!')
#         else:
#             if money < 10 or money > 1000:
#                 print('Сумма снятия наличных не может быть больше 1000 и менее 10 руб за одну денежную операцию!')
#             else:
#                 if money % 20 == 0 or money % 50 == 0 or money % 100 == 0:
#                     self.__money = self.__money - money
#                 else:
#                     print('В банкомате нет курюр с такой суммой!')
#
#
#     def info(self):
#         print(f'Приветствуем Вас в нашем банкомате!\nID банкомата: {self.__idBankomat}!')
#
#
# bankomat = Bankomat()
#
# while True:
#     print('Выберите действие:')
#     print('0. Просмотр информации о банкомате')
#     print('1. Пополнить счет банкомата')
#     print('2. Снять деньги со счета банкомата')
#     print('3. Просмотр баланса банкомата')
#     print('4. Выход')
#     choice = int(input('Выберите действие: '))
#     if choice == 0:
#         bankomat.info()
#     elif choice == 1:
#         bankomat.setMoney(int(input('Введите сумму: ')))
#     elif choice == 2:
#         bankomat.subMoney(int(input('Введите сумму: ')))
#     elif choice == 3:
#         print(bankomat.getMoney())
#     elif choice == 4:
#         break
#     else:
#         print('Неверный выбор!')
#         os.system('pause')
#         continue
#     os.system('pause')
#     os.system('cls')
# print('Программа завершена!')