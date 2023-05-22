class cat :
    species = "Feline"

    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def description(self) :
        return f"{self.name} is {self.age} years old. "
    
    def speak(self, sound):
        return f"{self.name} meows : {sound}"
    
kitten = cat("Felix" , 2)
ginger_kitten = cat("Ginger" , 3)
print(kitten.name)
print(kitten.age)

print(kitten.description())
print(kitten.speak("Hello"))


