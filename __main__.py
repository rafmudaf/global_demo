from module import A
from module2 import B
import global_module

def main():
    print("1 - Global variable is:", global_module.GLOBAL)

    global_module.GLOBAL = "GLOBAL"
    print("2 - Global variable is:", global_module.GLOBAL)

    a = A()
    print("3 - Global variable from A is:", a.get_global())

    print("    Resetting to A from A()")
    a.set_global("A")

    b = B()
    print("4 - Global variable from B is:", b.get_global())

    print("    Resetting to B from B()")
    b.set_global("B")

    print("5 - Global variable from A is:", a.get_global())

if __name__=="__main__":
    main()