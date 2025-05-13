class Person:
    def __init__(self, name,surname,age,email):
        self.__name=name
        try:
            self.__name = self.__name.lower()
            ascii_range = range(97 ,123, 1)

            for item in range(0 , len(self.__name)):
                if ord(self.__name[item]) not in ascii_range:
                    raise ValueError(" Name coudn't contain non-letter symbols")
        except:
            print(("Name coudn't contain non-letter symbols"))
        self.__surname=surname
        try:
            self.__surname = self.__surname.lower()
            ascii_range = range(97 ,123, 1)

            for item in range(0 , len(self.__surname)):
                if ord(self.__surname[item]) not in ascii_range:
                    raise ValueError(" Surname coudn't contain non-letter symbols")
        except:
            print(("Surname coudn't contain non-letter symbols"))
        try:

            if age < 0:
                raise ValueError("Age couldn't be negative")
            elif age > 120:
                raise ValueError("Age couldn't be more than 120")
            else:
                self.__age=age
        except ValueError as e:
            print(e)
        self.__email=email
        try:
            if '@' not in self.__email:
                raise ValueError('You enterned not email adress')
            d = self.__email.split('@')
            if len(d) != 2:
                raise ValueError('You enterned not email adress')
            if '.' not in d[1]:
                raise ValueError('You enterned not email adress')
            try:
                e = d[1].split('.')
                check = len(e[0]) / len(e[1])
                check = len(e[1]) / len(e[0])
            except:
                raise ValueError('You enterned not email adress')
        except:
            print(("You enterned not email adress"))
    def change_age(self, new_age):
        try:
            if new_age < 0:
                raise ValueError("Возраст не может быть отрицательным")
            elif new_age > 120:
                raise ValueError("Возраст не может быть больше 120 лет")
            else:
                self.__age = new_age
                print(f"Возраст изменён на {self.__age}")
        except ValueError as e:
            print(e)
    def __str__(self):
        return f"Имя: {self.__name}, Фамилия: {self.__surname}, Возраст: {self.__age}, Email: {self.__email}"
a = Person('sad','b', 33,'sada@mail.ru')
a.change_age(30)
print(a)