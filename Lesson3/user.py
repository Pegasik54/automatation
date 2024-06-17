class User:
    
    def __init__(self, first_name, last_name):
       print("Привет")
       self.first_name = first_name
       self.last_name = last_name

    def print_first_name(self):
        print("Меня зовут:", (self.first_name))

    def print_last_name(self):
        print("Моя фамилия:", (self.last_name))

    def print_full_name(self):
        print("Имя и фамилия:", self.first_name, self.last_name)



