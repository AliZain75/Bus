class Reverse:
    def __init__(self, s=""):
        self.s = s  
    def get_reversed(self):
        return self.s[::-1] 
user_input = input("Enter a word: ")
rev_obj = Reverse(user_input)
print("Reversed string:", rev_obj.get_reversed())