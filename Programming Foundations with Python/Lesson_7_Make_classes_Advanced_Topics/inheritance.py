# Definition of class Parent
class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")  # tells us each time it's called
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called") # tells us each time it's called
        # Initializes the variables from class Parent
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    # Overrides the method of the parent class
    def show_info(self):
        print("Number of toys - " + str(self.number_of_toys))

# Instances creation (normally on a separate file)
billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
print()
miley_cyrus = Child("Cyrus", "blue", "99")
miley_cyrus.show_info()