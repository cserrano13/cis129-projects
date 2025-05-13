# Module-12_Lab-12
# author - cesar
# date - 2025-05-13

"""
OOP Practice - Pet Class
"""

def main():
    # Declare input variables
    inputName = "temp"
    inputType = "temp"
    inputAge = 0
    
    # Declare new Pet class object
    animal1 = Pet()

    # Prompt user for pet details
    inputName = input("Enter your pet's name: ")
    inputType = input("Enter your pet's type: ")
    inputAge = input("Enter your pet's age: ")

    # Set input values to Pet object
    animal1.setName(inputName)
    animal1.setType(inputType)
    animal1.setAge(inputAge)

    # Display animal1 details to user
    print(f"The pet name is {animal1.getName()}")
    print(f"The pet type is {animal1.getType()}")
    print(f"The pet age is {animal1.getAge()}")

class Pet():
    def __init__(self):
        self._name = ""
        self._type = ""
        self._age = 0
    def setName(self, inputName):
        self._name = inputName
    def setType(self, inputType):
        self._type = inputType
    def setAge(self, inputAge):
        self._age = inputAge
    def getName(self):
        return self._name
    def getType(self):
        return self._type
    def getAge(self):
        return self._age

main()
