'''10_1
class Person(object):
    def __init__(self, name):
        self.name = name


    def language(self):
        pass

class Earthling(Person):
    def language(self, language):
        return language

class Groot(Person):
    def language(self, language):
        return "I'm Groot!"

name = ['Gachon', 'Dr.Strange', 'Groot']
country = ['Korea', 'Usa', 'Galaxy']
language = ['Korean', 'English', 'Groot']

for idx, name in enumerate(name):
    if country[idx].upper() !='GALAXY':
        person = Earthling(name)
        print(person.language(language[idx]))

    else:
        groot = Groot(name)
        print(groot.language(language[idx]))
'''

'''10_4
class Marvel(object):
    def __init__(self,name,characteristic):
        self.name=name
        self.characteristic=characteristic
    def __str__(self):
        return "My name is {0} and my weapon is {1}".format(self.name, self.characteristic)

class Villain(Marvel):
        pass


first_villain = Villain("Thanos","infinity gauntlet")
print(first_villain)
'''

'''10_9
class Person:
    def __init__(self, name, age, position):
        self.Name = name
        self.Age = age
        self.Position = position
    def show_info(self):
        print('이름:{}'.format(self.Name))
        print('나이:{}'.format(self.Age))
        print('직위:{}'.format(self.Position))
        print('저는 가천대 연구소 {0} {1} 입니다. 나이는 {2} 입니다.'.format(self.Position, self.Name, self.Age))

class Researcher(Person):
    def __init__(self, name, age, position, degree):
        Person.__init__(self,name,age,position)
        self.Degree = degree
    def show_info(self):
        Person.show_info(self)
        print("저는{}입니다.".format(self.Degree))

if __name__ == '__main__':
    researcher_john = Researcher("John","22","연구원","학사")
    researcher_tedd = Researcher("Tedd", "40", "소장", "박사")
    researcher_john.show_info()
    print("="*50)
    researcher_tedd.show_info()
'''

class IceCream(object):
    def __init__(self,flavor):
        self.flavor = flavor
    def change_flavor(self,new_flavor):
        print('아이스크림을 %s에서 %s로 변경해주세요.'%(self.flavor, new_flavor))
        self.flavor = new_flavor
        print('아이스크림 맛을 %s로 변경해드렸어요.'%self.flavor)

ice_cream=IceCream('레인보우 샤베트')
ice_cream.change_flavor('바람과 함께 사라지다')
