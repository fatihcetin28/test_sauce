class Human:
    name='Fatih'
    lastName = 'Çetin'
    fullName =''
    # constructor, initialize
    def __init__(self,name, lastName):
        self.name = name
        self.lastName = lastName
        self.fullName = name + ' ' + lastName
        print('Bir human instance ı  üretildi')
    
    def __str__(self) -> str:
        return f'str fonkundan dönen değer: {self.fullName}'

    def talk(self,sentence):
        print(f'{self.name}: {sentence}')
    def walk(self):
        isim='Hasan'
        print(f'{isim}: Human is walking')
        self.talk('Walktan çağırdık')
    def fullName1(self):
        return self.name + ' ' + self.lastName

# Human.talk()
# Human.walk()

human1 = Human('Kamil','Faik') #instance oluşturma
# print(human1.name)
# print(human1.fullName)
# print(human1.fullName1())

print(human1)

# print(human1.fullName1())
# human1.talk('Naber')
# human1.walk()