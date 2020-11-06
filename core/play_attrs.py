import attr
import datetime


# @attr.s(auto_attribs=True)
# class Person(object):
#     name: str
#     family_name: str
#     birth_date: datetime.datetime
#
#     @property
#     def age(self) -> int:
#         return (datetime.datetime.today() - self.birth_date).days // 365

@attr.s
class Person2:
    name = attr.ib(default='Bruce')
    family_name = attr.ib(default='Banner')
    birth_date = attr.ib(default=datetime.datetime.today())

    @property
    def age(self):
        return (datetime.datetime.today() - self.birth_date).days // 365

if __name__ == '__main__':
    p = Person2('John', 'Doe', datetime.datetime(1990, 8, 16))
    print(p)
    print(p.age)
    p = Person2()
    print(p)
    print(p.age)
