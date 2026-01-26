class student:
  def __init__(self, name, roll):
    self.name = name
    self.roll = roll

  def display(self):
    print("student's name is: " ,self.name)
    print("studnet roll no is: ", self.roll)

p1 = student("xyz", 25)
p1.display()