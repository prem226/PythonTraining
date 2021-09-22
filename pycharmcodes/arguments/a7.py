import argparse

class Employee:
    def __init__(self, no_of_employees):
        self.no_of_employees = no_of_employees
        print("no. of employees: ",no_of_employees)

    def add(self, a, b):
        print(a+b)

    def mul(self, x, y):
        print(x*y)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('no_of_employees', help="Employee", type=int )
    parser.add_argument('a', help="Employee", type=int)
    parser.add_argument('b', help="Employee", type=int)
    parser.add_argument('x', help="Employee", type=int)
    parser.add_argument('y', help="Employee", type=int)
    args = parser.parse_args()

    res = Employee(args.no_of_employees)
    res.add(args.a, args.b)
    res.mul(args.x, args.y)