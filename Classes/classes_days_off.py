class Employer:
#name, surname, year of birth, degree, number of vacation days
    def __init__(self, employer_name, employer_surname, employer_year_of_birth):
        self.name = employer_name
        self.surname = employer_surname
        self.year_of_birth = employer_year_of_birth
        self.degree = 1
        self.number_of_vacation_days = 26

    def __str__(self):
        info = f'This is {self.name} and has {self.number_of_vacation_days} days off.' #born in {self.year_of_birth}'
        return info

    def leave(self, number_of_days):
        if self.number_of_vacation_days < number_of_days:
            print('You cannot take a leave.')
        else:
            self.number_of_vacation_days -= number_of_days


p1 = Employer('Lena', 'Rose', 95)
p2 = Employer('Andrzej', 'Faja', 77)
p3 = Employer('Sara', 'Kania', 88)

print(p1.surname)
print(p3.year_of_birth)
p2.year_of_birth = 74
print(p2.year_of_birth)
print(p2)
p2.leave(21)
print(p2)
