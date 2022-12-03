class Phonebook():
    def __init__(self,surname,adress,phone_number):
        self.surname=surname
        self.adress=adress
        self.phone_number=phone_number
    def info(self):
        print("\nСоздан класс Персона")
        print("Имя: {0}, Адрес: {1}, Номер телефона: {2}".format(self.surname,self.adress,self.phone_number))
        
#создание дочерних классов
class Organisation(Phonebook):
    def __init__(self,surname,adress,phone_number,fax):
        super().__init__(surname,adress,phone_number)
        self.fax=fax
    def info(self):
        Phonebook.info(self)
        print("Создан подкласс Организация")
        print("Факс: {0}".format(self.fax))
class Friend(Phonebook):
    def __init__(self,surname,adress,phone_number,date_of_birth):
        super().__init__(surname,adress,phone_number)
        self.date_of_birth=date_of_birth
    def info(self):
        Phonebook.info(self)
        print("Создан подкласс Друг")
        print("Дата рождения: {0}".format(self.date_of_birth))
main=[]
n=int(input("Введите количество персон: "))
for i in range (n):
    choose=input("Какой элемент создаём? 1)Персона 2)Огранизация 3)Друг: ")
    surname1=input("Введите фамилию: ")
    adress1=input("Введите адрес: ")
    phone_number1=input("Введите номер телефона: ")
    spisok=[surname1,adress1,phone_number1]
    main.append(spisok)
    if choose=="1":
        per=Phonebook(surname1,adress1,phone_number1)
        per.info()
        print()
    if choose=="2":
        fax1=input("Введите номер факса организации: ")
        org=Organisation(surname1,adress1,phone_number1,fax1)
        org.info()
        print()
        spisok.append(fax1)
    if choose=="3":
        date_of_birth1=input("Введите дату рождения друга: ")
        frn=Friend(surname1,adress1,phone_number1,date_of_birth1)
        frn.info
        print()
        spisok.append(date_of_birth1)
        
print("Ваш список: \n")
for i in range (n):
    print("Элемент №", i)
    print(*main[i])


find_surname=input("Введите фамилию для поиска в списке: ")
filter_object = filter(lambda a: find_surname in a, main)
print("Фамилия найдена, информация по объекту: ")
print(list(filter_object))

          
                  



            

        
        
