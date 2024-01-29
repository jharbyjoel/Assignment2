import socket

class Assignment2:
    
    def __init__(self, year):
        self.year = year
        
    def tellAge(self, currentYear):
        birth_year = currentYear - self.year
        print("Your current age is", birth_year)
    
    def listAnniversaries(self):
        year = 2024
        anverse_years = [i for i in range(10, year - self.year + 1, 10)]
        return anverse_years
    
    def modifyYear(self, n):
        year_str = str(self.year)
        first_characters = year_str[:2]
        odd_characters = year_str[2::2]
        
        year = ''.join([first_characters, odd_characters] * n)
        return year
    
    @staticmethod
    def checkGoodString(string):
        
        if len(string) >= 9:
            if string[0].isalpha() and string[0].islower():
                digits_counter = sum(1 for char in string if char.isdigit())
                if digits_counter == 1:
                    return True
                
        return False
    
    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((host,port))
                s.close()
                
            return True
        
        except (socket.error, socket.timeout):
            return False

