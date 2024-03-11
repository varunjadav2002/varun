#mul inheritance
class Father:
    def heght(self):
        print("height is 5 Foot")

class Mather:
    def color(self):
        print("Color is Brown")

class Child(Father,Mather):
    pass

c=Child()
print("Child's inherited qualities:")
c.heght()
c.color()