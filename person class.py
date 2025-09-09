from datetime import date
class Person:
    def __init__(self, id, first_name, last_name, age,
                 birthday, phone_number=None,email=None):
        assert isinstance(id, str)
        assert isinstance(first_name, str)
        assert isinstance(last_name, str)
        assert isinstance(age, int)
        assert isinstance(birthday, dict)
        assert all( i in birthday for i in ['year', 'month', 'day'])
        if phone_number is not None:
            assert isinstance(phone_number, str)
        if email is not None:
            assert isinstance(email, str)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday
        self.p_id = id
        self.phone_number = phone_number
        self.email = email

    @property
    def id(self):
        return self.id
    @id.setter
    def id(self, new_id):
        self.id = new_id


    @property
    def first_name(self):
        return self.first_name
    @first_name.setter
    def first_name(self, new_name):
        self.first_name = new_name


    @property
    def last_name(self):
        return self.last_name
    @last_name.setter
    def last_name(self, new_last_name):
        self.last_name = new_last_name


    @property
    def age(self):
        return self.age
    @age.setter
    def age(self, new_age):
        self.age = new_age

    @property
    def all_birthday(self):
        return (f"{self.birthday['day']:02d}-{self.birthday['month']:02d}-{self.birthday['year']:02d}")
    @all_birthday.setter
    def all_birthday(self, new_birthday):
        self.all_birthday = new_birthday


    @property
    def phone_number(self):
        return self.phone_number
    @phone_number.setter
    def phone_number(self, new_number):
        self.phone_number = new_number


    @property
    def email(self):
        return self.email
    @email.setter
    def email(self, new_email):
        self.email = new_email



    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    @property
    def contact_information(self):
        return f'{self.phone_number} {self.email}'



    def all_ditail(self):
        return f'''{self.first_name}
{self.last_name}
{self.age} 
{self.p_id}
{self.phone_number}
{self.email}
'''


