class abc:
    n = 10
    print(n) 

    def status(self,emp_name,emp_id):

        self.emp_id = emp_id
        self.emp_name = emp_name

        print("Employee id is :- ",self.emp_id)
        print("Employee name is :- ",self.emp_name)

a = abc()
a.status("Manmeet" , "E01") 