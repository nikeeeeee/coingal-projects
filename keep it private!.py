# Class creation
class myClass:
    # private variable
    _privateVar = 27;
    # private method
    def _privMeth(self):
            print("i'm inside class myclass")
    # Function to print value of private variable
    def hello(self):
            print("Private Variable value: ",myClass._privateVar)
# Object creation and method call
foo = myClass()
foo.hello()