# create an animal class

class Animal:
    def __init__(self, name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound

    def speak(self):
        print(f'hello am a {self.pet} and I make sound of {self.sound}')

    def pet_info(self):
        print(f"my name is {self.name}")
        print(f"I am a {self.pet}")
        print(f"I make sound of {self.sound}")


dog = Animal('peter','dog','wof wof')
cat = Animal('catto','cat','meo meo')
dog.speak()
dog.pet_info()
cat.speak()
cat.pet_info()

