class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)

isinstance(miles, Dog)
print(type(miles))