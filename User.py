class User:
    def login(self):
        print("login called")
class Business(User):
    def run_add(self):
        print("add called")
b=Business()
b.login()
b.run_add()

