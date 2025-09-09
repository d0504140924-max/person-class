class Person:
    def __init__(self, first_name, last_name, now_age, ID_number, phone_number=None,
                 email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.now_age = now_age
        self.ID_number = ID_number
        self.phone_number = phone_number
        self.email = email
    def print_the_ditails(self):
        print(f'''{self.first_name}
{self.last_name}
{self.now_age} 
{self.ID_number}
{self.phone_number}
{self.email}
''')
person1 = Person('david', 'rubnitz', 21,
                 321321321, '0537195856',
                 'd0504140924@gmail.com')
person1.print_the_ditails()

