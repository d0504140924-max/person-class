from datetime import date
class Person:
    def __init__(self, p_id, first_name, last_name, age,
                 birthday, phone_number=None,email=None):
        assert isinstance(p_id, str)
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
        self.p_id = p_id
        self.phone_number = phone_number
        self.email = email


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    @property
    def contact_information(self):
        return f'{self.phone_number} {self.email}'
    @property
    def all_birthday(self):
        return (f"{self.birthday['day']:02d}-{self.birthday['month']:02d}-{self.birthday['year']:02d}")



    def all_ditail(self):
        return f'''{self.first_name}
{self.last_name}
{self.age} 
{self.p_id}
{self.phone_number}
{self.email}
'''


