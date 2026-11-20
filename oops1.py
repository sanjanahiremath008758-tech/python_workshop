


class Bank:
    bname = "SBI"
    bloc = "Mumbai"

    def __init__(self, name, phnno, eid):
        self.name = name
        self.phnno = phnno
        self.eid = eid

    def display(self):
        print("Bank Name:", self.bname)
        print("Bank Location:", self.bloc)
        print("Name:", self.name)
        print("Phone Number:", self.phnno)
        print("Email ID:", self.eid)


class Bank_details(Bank):
    founder = "Ram"

    def __init__(self, name, phno, eid, add, pan):
        super().__init__(name, phno, eid)
        self.add = add
        self.pan = pan

    def display(self):
        super().display()
        print("Founder:", self.founder)
        print("Address:", self.add)
        print("PAN Number:", self.pan)


C1 = Bank_details("Saniya", 987654321, "s@gmail.com", "Bangalore", "ABCDE1234F")

C1.display()