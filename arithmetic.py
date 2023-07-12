import random


class ArithmeticExam:
    intro = """
    Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29
    """

    def __init__(self):
        self.level = None
        self.level_description = None
        self.mark = None

    def addition(self, value1, value2):
        return value1 + value2

    def subtraction(self, value1, value2):
        return value1 - value2

    def multiplication(self, value1, value2):
        return value1 * value2

    def perform_operation(self, value1, value2, operator):
        if operator == "+":
            return self.addition(value1, value2)
        elif operator == "-":
            return self.subtraction(value1, value2)
        elif operator == "*":
            return self.multiplication(value1, value2)

    def random_pickup(self):
        value1 = random.randint(2, 9)
        value2 = random.randint(2, 9)
        operator_list = ["+", "-", "*"]
        operator = random.choice(operator_list)
        value = random.randint(11, 29)
        return value1, value2, operator, value

    def display_question(self, value1, operator, value2):
        print(f"{value1} {operator} {value2}")

    def display_number(self, value):
        print(value)

    def squares_operation(self, value):
        return value ** 2

    def perform_simple_operation(self, level):
        n = 0
        for _ in range(5):
            value1, value2, operator, value = self.random_pickup()
            if level == 1:
                self.display_question(value1, operator, value2)
            elif level == 2:
                self.display_number(value)
            try:
                user_answer = int(input())
                if user_answer == self.perform_operation(value1, value2, operator):
                    print("Right!")
                    n += 1
                else:
                    print("Wrong!")
            except ValueError:
                print("Incorrect format.")

        self.mark = f"{n}/5"
        self.result = f"Your mark is {self.mark}. Would you like to save the result? Enter yes or no."
        print(self.result)

    def save_result(self):
        answer = input().lower()
        if answer in ("yes", "y"):
            print("What is your name?")
            name = input()
            with open("results.txt", "a") as note:
                note.write(f"{name}: {self.mark} in level {self.level} ({self.level_description}).")
            print('The results are saved in "results.txt".')
        else:
            pass

    def calculation(self):
        print(self.intro)
        self.level = int(input())
        if self.level == 1:
            self.level_description = "simple operations with numbers 2-9"
        elif self.level == 2:
            self.level_description = "integral squares of 11-29"
        self.perform_simple_operation(self.level)
        self.save_result()


arithmetic_exam = ArithmeticExam()
arithmetic_exam.calculation()
