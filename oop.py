"""
structure
---------

#create a class
#init the class
#give a method
"""

class auraaid:
    def __init__(self, devs, workhours):

        self.devs = devs
        self.workhours = workhours
    
    def roles(self):
        return (f"{self.devs} {self.workhours}")
    
auraaid1 = auraaid("jcrown", 8)
auraaid.roles()