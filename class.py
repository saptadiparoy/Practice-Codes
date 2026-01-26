class class1 :
    def __intit__(self, rip, x):
        self.rip = rip
        self.x = 21 + rip
y = class1(67)
print (y.x)

class person :
    def __init__ (self, name, place):
        self.name = name 
        self.place = place
smth = person("abc", "xyz")
print (smth.place)
print (smth.name)


class student:
  def __init__(self, name, roll):
    self.name = name
    self.roll = roll

  def display(self):
    print("student's name is: " + self.name)

p1 = student("Emil", 25)
p1.greet()