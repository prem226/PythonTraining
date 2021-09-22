class Person:
    name = []
    firstname = []
    lastname = []

    def set_name(self,user_name):
        self.name.append(user_name)
        return len(self.name)

    def get_name(self,user_id):
        if user_id >= len(self.name):
            return 'there is no such user'
        else:
            return self.name[user_id]

    def first_name(self,fname):
        self.firstname.append(fname)
        return len(self.firstname)

    def last_name(self,lname):
        self.lastname.append(lname)
        return len(self.lastname)



if __name__ == '__main__':
    person = Person()
    print("User andre is been added with id ", person.set_name('andre'))
    print("User associated with id 0 is ", person.get_name(0))
    print("First name id", person.first_name("Prem"))
    print("Last name id", person.last_name("Parakhi"))