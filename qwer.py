class Person:
    def __init__(self, name, surname, age, email):

        try:
            if age > 0 and age < 130:
                raise ValueError("Это невозможно")
            else:
                    self.age = int(age)
        except:
            print("Введите нормальный возраст")

        try:
             self.proverka(name)
             self.name = name
        except:
             print("Введите нормальное имя")

        try:
             self.proverka(surname)
             self.surname = surname   
        except:    
            print("Введите нормальную фамилию")
        
        try:
            if '@' in email and '.' in email:
                if email[email.find('@') + 1] in range(97, 123) or email[email.find('@') + 1] in range(48, 58):
                     if email[email[(email.find('@')):].find('.')] in range(97, 123):
                        self.email = email
                else:
                    raise ValueError
            else:
                 raise ValueError
        except:
             print('Это не email')
    def proverka(self, name):
         asc = [ord(char) for char in name]
         for i in asc:
              if i not in range(97, 123) and i != 45:
                   raise ValueError
    
    def __del__(self):
         print('Удалено')

cv = Person('asdfa-asd', 'qwe', 12, 'weqwe@1.fg')
        

