# Import necessary Modules
from abc to import ABC, abstractmethod
# Create base class
class Absclass(ABC):
        # Function to print a value
    def print(self, x):
        print("Passed value: ", x)
        # Abstract method
     @abstractmethod
     def task(self):
        print ("We are inside Absclass task")
    # Create sub class
    class test_class(Absclass):
       def task(self):
          