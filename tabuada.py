import sys
from copy import copy
from random import choice, randint


class Tabuada:
    """ A class that handles math tables operations and user input """

    mode = None
    table_of  = 0
    operator = None
    operation = None
    operators = ["+", "-", "*", "/"]
    operations = { "A": "+", "B": "-", "C": "*", "D": "/" }
    terms = []
    digits = None
    term_one = None
    term_two = None
    start = None
    stop = None
    last_term = None 
    exp_eval = None
    attempts = 0
    modes = ["easy", "medium", "hard"]


    def __init__(self, operation=None, table_of=None, mode=None):
        """ Runs the game with the given arguments """

        if operation is not None:
            self.operation = operation
        else:
            self.operation = choice(self.operators)

        if table_of is not None:
            self.table_of = table_of
        else:
            self.table_of = randint(1, 10)

        if mode is not None:
            self.mode = mode
        else:   
            self.mode = 'easy'

        self.build_arithmetic_expression()


    # build_arithmetic_expression should be renamed to something else
    def build_arithmetic_expression(self):
        """ Sets a couple of values that will be used to construct a random expression """
        
        start = None
        stop  = None

        if self.operation == "/":
            start = self.table_of
            stop  = start * 10
            self.terms  = [x * self.table_of for x in range(1, 11)]
            self.digits = copy(self.terms) 
            return self.run_arithmetic_expression()
                   
        elif self.operation == "-":
            start = self.table_of + 1
            stop  = start + 10
        else:
            start = 1
            stop  = 11
        
        self.terms = [n for n in range(start, stop)]
        self.digits = copy(self.terms)

        return self.run_arithmetic_expression()


    def select_digit(self, digit, mode):
        """ Selects a digit based on the current mode """

        difficulty = mode.lower()

        if difficulty == "easy":
            Tabuada.attempts += 1
            return min(digit)
        elif difficulty == "hard":
            Tabuada.attempts = 3
        elif difficulty == "Extreme":
            Tabuada.attempts = 0

        return choice(digit)

    def current_expression(self):
        """ Returns a valid python expression ready for evaluation """

        if self.operation == "-" or self.operation == "/":
            # This is probably redundant code since an option to set table_of is given earlier
            # As for now, I will kept just because some randomness will be implemented 
            self.term_two = self.table_of if self.table_of else randint(1, 11)
            self.term_one = self.select_digit(self.digits, self.mode)
            self.last_term = copy(self.term_one)
        else:
            self.term_one = self.table_of if self.table_of else randint(1, 11)
            self.term_two = self.select_digit(self.digits, self.mode)
            self.last_term = copy(self.term_two)
        
        return f"{self.term_one} {self.operation} {self.term_two}"


    def current_expression_template(self):
        """ Returns a expression with unicode sign for division and multiplication """
        
        if self.operation == "/":
            self.operator = chr(247)
        elif self.operation == "*":
            self.operator = chr(215)
        else:
            self.operator = self.operation
            
        return f"{self.term_one} {self.operator} {self.term_two}"


    def eval_expression(self, expression, user_input):
        """ Safely evaluates user input """

        try:
            code = compile(user_input, "<string>", "eval")

            if not code.co_names:
                if eval(expression) == eval(code, { "__builtins__": {} }, {}):
                    return True
                else:
                    return False

        except SyntaxError:
            pass


    def pop_last_question(self):
        """ Pops the last digit used to prompt the user with a question """
        return self.digits.pop( self.digits.index(self.last_term) )

    def run_arithmetic_expression(self):
        """ Promps the user with a question """

        while len(self.digits):
            expression = self.current_expression()
            question = self.current_expression_template()

            print(f"{question} = ")

            try:
                answer = input("... ")
                if self.eval_expression(expression, answer):
                    self.pop_last_question()
                else:
                    pass
                #if len(Tabuada.digits) == 0:
                    #print("Would you like to keep playing?")

            except EOFError:
                pass

            except KeyboardInterrupt:
                sys.exit(0)
            