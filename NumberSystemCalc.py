
import os
import re
import sys
import json
from datetime import datetime

"""
 author:            Bányász Tamás
    since:          2024.05.01
    created_to:     Dr. Faragó Csaba
    product_name:   Number System Calculator
    version:        1.0
    file_name:      number_system_calculator
"""

"""
    *About the code*:
    
        With this application we can calculate different positive values into different number system:
    
            decimal -> binary
            octal -> decimal
            hexa -> decimal
        
        Every try of inputs will be saving into a structured JSON file abd every received calculated value will be 
        saving into TXT file.
        In our case we will getting 3 different TXT file and 1 JSON file.
    
        Got a class to calculating processes.       (Line 45.)
        Got a class to the Match/Case processes.    (line 107.)
        Got a class to files handling processes.    (Line 127.)
        Got a class to the user inputs.             (Line 178.)
    
        Conclusions:
            - The inputs could be only positive.
            - The Calculator class is in the Match/Case class.
            - The files handling class is in the userInputhandler class.
            - We can modify whether the user would like to saving the final values into TXT files or not.
            - Where would like the user to store the files. (File path)
            - Code maded by 'sphagetti-way' manner.

"""


class NumberSystemCalculator:
    def __init__(self):
        self.hexa_numbers = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        self.octal_in_decimal_number = 0
        self.hexa_in_decimal_number = 0

    @staticmethod
    def calculate_decimal_into_binary(decimal_number):
        number_ = abs(decimal_number)

        binary_numbers = []

        while number_ != 0:
            binary_numbers.append(number_ % 2)  # if number % 2 == 1 or 0 then add to a list
            number_ = number_ // 2  # remainder of the number

        binary_numbers = int(''.join(map(str, reversed(binary_numbers))))
        print(f'\nThe selected decimal number in binary system: {binary_numbers}')
        return binary_numbers, 'decimal_to_binary'

    def calculate_octal_to_decimal(self, octal_number):

        list_of_sliced_octal_number = list(map(int, str(abs(octal_number))))  # digits of the value in list

        for index, value in enumerate(reversed(list_of_sliced_octal_number)):
            # convert to decimal
            self.octal_in_decimal_number = self.octal_in_decimal_number + value * 8 ** index

        print(f'\nThe selected octal number in decimal: {self.octal_in_decimal_number}')
        return self.octal_in_decimal_number, 'octal_to_decimal'

    def calculate_hexa_to_decimal(self, hexa_value):

        list_of_sliced_hexa_value = [i for i in hexa_value]  # parts of the hexa value in list by slicing

        formatted_list_of_sliced_hexa_value = []

        # if the received value contains lowercase alphabet, then make it uppercase
        for item in list_of_sliced_hexa_value:
            if item.isdigit():
                formatted_list_of_sliced_hexa_value.append(int(item))  # add the digits of the value to list
            else:
                formatted_list_of_sliced_hexa_value.append(
                    item.upper())  # add the alphabet character of the received value to list

        for index, value in enumerate(reversed(formatted_list_of_sliced_hexa_value)):
            # loop over the formatted list and convert to hexa
            if type(value) == int:
                self.hexa_in_decimal_number = self.hexa_in_decimal_number + value * 16 ** index
            self.value_equals_to_one_of_key_in_the_hexa_numbers_dict(self.hexa_numbers, index, value)

        print(f'\nThe selected hexa value in decimal: {self.hexa_in_decimal_number}')

        return self.hexa_in_decimal_number, 'hexa_to_decimal'

    def value_equals_to_one_of_key_in_the_hexa_numbers_dict(self, hexa_numbers, index, value):
        # if any item in list is a letter
        for key, item in hexa_numbers.items():
            if value == key:
                self.hexa_in_decimal_number = self.hexa_in_decimal_number + item * 16 ** index


class MatchCaseUnit:
    def __init__(self):
        self.numb_system_calc = NumberSystemCalculator()

    def choose_convert_process(self, user_input, value):

        match user_input:
            case 1:
                return self.numb_system_calc.calculate_decimal_into_binary(value)

            case 2:
                return self.numb_system_calc.calculate_octal_to_decimal(value)

            case 3:
                return self.numb_system_calc.calculate_hexa_to_decimal(value)

            case _:
                ...


class FileHandler:
    def __init__(self, json_file_name):
        self.json_file_name = json_file_name
        self.create_empty_json()
        self.write_to_txt = True
        self.loaded_json = self.load_from_json()

    def get_loaded_json(self):
        return self.loaded_json

    def set_write_to_txt(self, value):
        self.write_to_txt = value

    def can_write_to_txt(self):
        return self.write_to_txt

    def create_empty_json(self):
        if not os.path.isfile(self.json_file_name + ".json"):
            with open("elozmeny.json",  'w', encoding='utf-8') as file:
                file.write(json.dumps({'elozmeny': []}, ensure_ascii=False, indent=4))

            print("Json file created.")

    def load_from_json(self):
        if os.path.isfile(self.json_file_name + ".json"):
            with open(self.json_file_name + ".json", 'r', encoding='utf-8') as file:
                return json.load(file)

    def write_into_json(self, date, time, value):

        self.loaded_json['elozmeny'].append({date: {'time': time, 'input_was': value}})

        with open(self.json_file_name + ".json", 'w',  encoding='utf-8') as f:
            f.write(json.dumps(self.loaded_json, ensure_ascii=False, indent=4))

        print("Datas has been wroten into Json file.")

    @staticmethod
    def write_into_txt_file(txt_file_name, user_value):

        if not os.path.isfile(txt_file_name):
            with open(txt_file_name, 'w') as file:
                file.write(str(user_value) + "\n")
            print('File does not exist. TXT file has been created.')

        else:
            with open(txt_file_name, 'a') as file:
                file.write(str(user_value) + "\n")
            print('TXT file already exists for this process. Value appened into the file.')


class UserInputHandler:
    def __init__(self, file_handler_obj):
        self.file_handling = file_handler_obj
        self.selecting_value = None
        self.user_input = None
        self.user_value = None

    def get_user_input(self):
        return self.user_input

    def get_user_value(self):
        return self.user_value

    def select_convert_option(self):

        user_input = None

        while not user_input:

            try:
                print("\n 1: Decimal to binary\n 2: Octal to decimal\n 3: Hexa to decimal\n 4: Log data\n")
                selecting = int(input("Choose an option 1-4: "))
                if 0 < selecting <= 4:
                    user_input = selecting
                else:
                    print("Invalid input")

            except ValueError:
                print("Wrong type!")
            except KeyboardInterrupt:
                print("\nInput has been interrupted.")
                sys.exit(0)

        self.user_input = user_input

    def get_value_from_user_input(self, selected_option):

        """
            Whatever will happening while the user try to give any value the input will be saving into a json file.
            It's look alike such a log data.
            Thats happen in the part of 'finally' at the input processes.
        """

        user_value = None

        while not user_value:

            if selected_option == 1 or selected_option == 2:
                try:
                    self.selecting_value = input("Add value: ")
                    if not isinstance(int(self.selecting_value), int):
                        break
                    else:
                        user_value = int(self.selecting_value)

                except ValueError:
                    print("Wrong type!")
                except KeyboardInterrupt:
                    self.selecting_value = "Interrupted"
                    print("\nInput has been interrupted.")
                    sys.exit(0)
                finally:
                    self.file_handling.write_into_json(datetime.now().strftime("%Y/%m/%d"),
                                                       datetime.now().strftime("%H:%M:%S"),
                                                       self.selecting_value)

            if selected_option == 3:
                try:
                    self.selecting_value = str(input("Add value (For example: 'f4a'): "))

                    if re.search(r'^[A-Fa-f0-9]+$', self.selecting_value):
                        user_value = self.selecting_value
                    else:
                        print("Not okay to correct form.")
                except ValueError:
                    print("Wrong type!")
                except KeyboardInterrupt:
                    self.selecting_value = "Interrupted"
                    print("\nInput has been interrupted.")
                    sys.exit(0)
                finally:
                    self.file_handling.write_into_json(datetime.now().strftime("%Y/%m/%d"),
                                                       datetime.now().strftime("%H:%M:%S"),
                                                       self.selecting_value)

            if selected_option == 4:
                data = self.file_handling.get_loaded_json()

                for i in data["elozmeny"]:
                    print(i)
                print("Something to do after this ...")

                file_handler.set_write_to_txt(False)
                break

        self.user_value = user_value


print("\nWELCOME TO NUMBER SYSTEM CALCULATOR APPLICATION!")

file_handler = FileHandler("elozmeny")
match_handler = MatchCaseUnit()
user_input_handler = UserInputHandler(file_handler)

while True:

    user_input_handler.select_convert_option()
    user_input_handler.get_value_from_user_input(user_input_handler.get_user_input())

    returned_value = match_handler.choose_convert_process(user_input_handler.get_user_input(),
                                                          user_input_handler.get_user_value())

    if file_handler.can_write_to_txt():
        file_handler.write_into_txt_file(returned_value[1], returned_value[0])
