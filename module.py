
import global_module


class A():

    def __init__(self):
        self.letter = "A"
    
    def get_global(self):
        return global_module.GLOBAL

    def set_global(self, value):
        print("GLOBAL was: ", global_module.GLOBAL)
        global_module.GLOBAL = value
        print("GLOBAL is now: ", global_module.GLOBAL)
