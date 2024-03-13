import sys
from copy import copy
from random import choice, randint


class Tabuada:

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


    
    def select_digit(digit, mode):

        difficulty = mode.lower()

        if difficulty == "easy":
            Tabuada.attempts += 1
            return min(digit)
        
        elif difficulty == "hard":
            Tabuada.attempts = 3
        elif difficulty == "Extreme":
            Tabuada.attempts = 0

        return choice(digit)
    
    def current_expression_template():
        """ Returns a expression with unicode sign for division and multiplication """
        
        if Tabuada.operation == "/":
            Tabuada.operator = chr(247)
        elif Tabuada.operation == "*":
            Tabuada.operator = chr(215)
        else:
            Tabuada.operator = Tabuada.operation
            

        return f"{Tabuada.term_one} {Tabuada.operator} {Tabuada.term_two}"

    def current_expression():
        """ Returns a valid python expression ready for evaluation """

        if Tabuada.operation == "-" or Tabuada.operation == "/":
            # This is probably redundant code since an option to set table_of is given earlier
            # As for now, I will kept just because some randomness will be implemented 
            Tabuada.term_two = Tabuada.table_of if Tabuada.table_of else randint(1, 11)
            Tabuada.term_one = Tabuada.select_digit(Tabuada.digits, Tabuada.mode)
            Tabuada.last_term = copy(Tabuada.term_one)
        else:
            Tabuada.term_one = Tabuada.table_of if Tabuada.table_of else randint(1, 11)
            Tabuada.term_two = Tabuada.select_digit(Tabuada.digits, Tabuada.mode)
            Tabuada.last_term = copy(Tabuada.term_two)
        


        return f"{Tabuada.term_one} {Tabuada.operation} {Tabuada.term_two}"


    def run_arithmetic_expression():
        
        while len(Tabuada.digits):
            expression = Tabuada.current_expression()
            question = Tabuada.current_expression_template()

            # The variable question should instead be renamed to expression
            # and the variable expression to question

            print(f"{question} = ")

            try:
                answer = input("... ")
                
                if Tabuada.eval_expression(expression, answer):
                    Tabuada.pop_last_question()
                else:
                    pass

            except EOFError:
                pass

            except KeyboardInterrupt:
                sys.exit(0)
            

    def pop_last_question():
        return Tabuada.digits.pop( Tabuada.digits.index(Tabuada.last_term) )


    def eval_input(user_input):
        code = compile(user_input, "<string>", "eval")

        if not code.co_names:
            return True
        return False
    

    def eval_expression(expression, user_input):

        try:
            code = compile(user_input, "<string>", "eval")

            if not code.co_names:
                if eval(expression) == eval(code, { "__builtins__": {} }, {}):
                    return True
                else:
                    return False

        except SyntaxError:
            pass


    # build_arithmetic_expression should be renamed to something else
    def build_arithmetic_expression(): 
        """ Sets a couple of values that will be used to construct a random expression """
        
        start = None
        stop  = None

        if Tabuada.operation == "/":
            start = Tabuada.table_of
            stop  = start * 10
            Tabuada.terms  = [x * Tabuada.table_of for x in range(1, 11)]
            Tabuada.digits = copy(Tabuada.terms) 
            return Tabuada.run_arithmetic_expression()
                   
        elif Tabuada.operation == "-":
            start = Tabuada.table_of + 1
            stop  = start + 10
        else:
            start = 1
            stop  = 11
        
        Tabuada.terms = [n for n in range(start, stop)]
        Tabuada.digits = copy(Tabuada.terms)

        return Tabuada.run_arithmetic_expression()
        
    def init(operation=None, table_of=None, mode=None):
        """ Runs the game with the given arguments """

        print()

        if operation is not None:
            Tabuada.operation = operation


        if table_of is not None:
            Tabuada.table_of = table_of
        else:
            Tabuada.table_of = randint(1, 10)

        if mode != None:
            Tabuada.mode = mode
        else:            
            Tabuada.mode = 'easy'

        return Tabuada.build_arithmetic_expression()