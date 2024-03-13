import sys
from datetime import date

from tabuada import Tabuada


class Pydagogue:
    """ An interactive class that prompts the user for input """

    _format = "... "
    _indent = "\t"
    reminder = 0

    last_input = None
    

    def __init__(self, name):
        self.user = name
        return self.welcome()

    def welcome(self):
        """ Welcome the user """
        dt = date.today()
        today = dt.strftime("%B %d, %Y")
        print(f"Pydagogue | {today}\n")
        #print(f"Welcome, {self.user}")

    def menu():
        
        print("\nEscolha uma opção:\n")
        print("A) Tabuada de Adição")
        print("B) Tabuada de Subtração")
        print("C) Tabuada de Multiplicação")
        print("D) Tabuada de Divisão")
        print()

    def help():
        pass


    def prompt():
        """ Prompt the user for input """

        Pydagogue.menu()
        

        current_key = None
        current_mode = None
        current_table = None

        while True:

            try:
                _input = input(Pydagogue._format)
                
                _key = _input.upper() if isinstance(_input, str) else None
                
                _table_of = _input if isinstance(_input, int) else None


            except EOFError:
                pass
            except KeyboardInterrupt:
                sys.exit(0)

            if _key in Tabuada.operations:
                key = Tabuada.operations[_key]
                Tabuada.init(operation=key)

            elif _table_of >= 1 and _table_of <= 10:
                pass

            else:
                Pydagogue.reminder += 1
                
                if Pydagogue.reminder == 5:
                    Pydagogue.reminder = 0
                    Pydagogue.menu()


if __name__ == '__main__':
    Pydagogue(name="JM")
    # TODO: Thinking of passing argv to the prompt method
    Pydagogue.prompt()