class converter():
    def __init__(self):
        self.roman_numbers = {
                '0':'',
                '1':'I',
                '2':'II',
                '3':'III',
                '4':'IV',
                '5':'V',
                '6':'VI',
                '7':'VII',
                '8':'VIII',
                '9':'IX',
                '10':'X',
                '40':'XL',
                '50':'L',
                '90':'XC',
                '100':'C',
                '400':'CD',
                '500':'D',
                '900':'CM',
                '1000':'M'
        }
        
        self.result = ""
    
    def convert(self, decimal_number):
        if int(decimal_number) > 3999 or int(decimal_number) == 0:
            self.result = 'Number must be greater than 0 and less than 4000'
        else:
            if len(decimal_number) == 4:
                self.first_digit = int(int(decimal_number)/1000)
                for i in range(int(self.first_digit)):
                    self.result += self.roman_numbers['1000']
                decimal_number = str(int(decimal_number) % 1000)

            if len(decimal_number) == 3:
                self.first_digit = int(int(decimal_number)/100)
                if self.first_digit >= 1 and self.first_digit <=3:
                    for i in range(self.first_digit):
                        self.result += self.roman_numbers['100']
                    decimal_number = str(int(decimal_number) % 100)

                if self.first_digit == 4:
                    self.result += self.roman_numbers['400']
                    decimal_number = str(int(decimal_number) % 100)

                if self.first_digit == 5:
                    self.result += self.roman_numbers['500']
                    decimal_number = str(int(decimal_number) % 100)
                
                if self.first_digit >=6 and self.first_digit <=8:
                    self.result += self.roman_numbers['500']
                    self.first_digit = int((int(decimal_number) - 500) / 100)
                    for i in range(self.first_digit):
                        self.result += self.roman_numbers['100']
                    decimal_number = str(int(decimal_number) % 100)
                
                if self.first_digit == 9:
                    self.result += self.roman_numbers['900']
                    decimal_number = str(int(decimal_number) % 100)

            if len(decimal_number) == 2:
                self.first_digit = int(int(decimal_number) / 10)
                if self.first_digit >= 1 and self.first_digit <=3:
                    for i in range(self.first_digit):
                        self.result += self.roman_numbers['10']
                    decimal_number = str(int(decimal_number) % 10)
                if self.first_digit == 4:
                    self.result += self.roman_numbers['40']
                    decimal_number = str(int(decimal_number) % 10)
                if self.first_digit == 5:
                    self.result += self.roman_numbers['50']
                    decimal_number = str(int(decimal_number) % 10)
                if self.first_digit >= 6 and self.first_digit <=8:
                    self.result += self.roman_numbers['50']
                    self.first_digit = int((int(decimal_number) - 50) / 10)
                    for i in range(self.first_digit):
                        self.result += self.roman_numbers['10']
                    decimal_number = str(int(decimal_number) % 10)
                if self.first_digit == 9:
                    self.result += self.roman_numbers['90']
                    decimal_number = str(int(decimal_number) % 10)

            if len(decimal_number) == 1:
                self.result += self.roman_numbers[decimal_number]
        return self.result   




