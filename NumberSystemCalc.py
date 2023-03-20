'''
Number system calculator

Decimal number to binary
Octal number to decimal
Hexa value to decimal
'''


class NumberSystemCalculator:
    def __init__(self):
        self.number = 0
        self.decimal_number = 0

    def calculate_decimal_into_binary_system(self, decimal_number):
        self.number = decimal_number

        binary_numbers = []

        while self.number != 0:
            binary_numbers.append(self.number % 2)  # if number % 2 == 1 or 0 then add to a list
            self.number = self.number // 2  # reminder of the number

        binary_numbers = int(''.join(map(str, reversed(binary_numbers))))
        print(f'\nThe selected decimal number in binary system: {binary_numbers}')
        return binary_numbers

    def calculate_octal_to_decimal(self, octal_number):
        self.number = octal_number
        list_of_digits = list(map(int, str(self.number)))  # digits of the value in list

        decimal_number = 0

        for index, value in enumerate(reversed(list_of_digits)):  # for loop over the reversed list of digits
            decimal_number = decimal_number + value * 8 ** index

        print(f'\nThe selected octal number in decimal: {decimal_number}')
        return decimal_number

    def calculate_hexa_to_decimal(self, hexa_value):
        self.number = hexa_value

        list_of_hexa_values = [i for i in self.number]  # elements of the value in list
        formatted_list_of_hexa_values = []

        for item in list_of_hexa_values:
            if item.isdigit():
                formatted_list_of_hexa_values.append(int(item))  # add the digits of the value to list
            else:
                formatted_list_of_hexa_values.append(item.upper())  # add the string letter of the value to list

        hexa_numbers = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

        for index, value in enumerate(reversed(formatted_list_of_hexa_values)):  # loop over the formatted list
            if type(value) == int:
                self.decimal_number = self.decimal_number + value * 16 ** index
            self.value_equals_to_one_of_key_in_hexa_numbers_dict(hexa_numbers, index, value)

        print(f'\nThe selected hexa value in decimal: {self.decimal_number}')
        return self.decimal_number

    def value_equals_to_one_of_key_in_hexa_numbers_dict(self, hexa_numbers, index, value):  # if any item in list is a letter
        for key, item in hexa_numbers.items():
            if value == key:
                self.decimal_number = self.decimal_number + item * 16 ** index


number = NumberSystemCalculator()

if __name__ == "__main__":
    number.calculate_decimal_into_binary_system(27)
    number.calculate_octal_to_decimal(2034)
    number.calculate_hexa_to_decimal("a5f")
