import sys
from datetime import date

from tabuada import Tabuada


class Pydagogue:
    """ An interactive class that prompts the user for input """

    _format = "... "
    _indent = "\t"
    reminder = 0

    last_input = None


    def __init__(self, operation, tableof, mode):
        self.operation = operation
        self.tableof = tableof
        self.mode = mode

        self.prompt()

    def welcome(self):
        """ Welcome the user """
        dt = date.today()
        today = dt.strftime("%B %d, %Y")
        print(f"Pydagogue | {today}\n")
        #print(f"Welcome, {self.user}")

    def menu(self):
        """_summary_
        """
        print("\nEscolha uma opção:\n")
        print("A) Tabuada de Adição")
        print("B) Tabuada de Subtração")
        print("C) Tabuada de Multiplicação")
        print("D) Tabuada de Divisão")
        print()


    def parse_user_input(self, user_input):
        """ Parses user input """

        for option in user_input:
            # Alternatively, the if block could be at the end of the for loop
            # That way, the try block is possibly not necessary at all
            try:
                if isinstance(int(option), int):
                    tableof = int(option) if int(option) in range(1, 11) else None
                    if tableof is not None:
                        if tableof >= 11:
                            # print("Pick a smaller number!")
                            pass

                        self.tableof = tableof

            except ValueError:
                pass

            if option in Tabuada.operators:
                self.operation = option

            if option in Tabuada.modes:
                self.mode = option


    def prompt(self):
        """ Prompt the user for basic input to get everything started """
        
        self.menu()
        
        while True:
            try:
                user_input = input(Pydagogue._format)

                self.parse_user_input(user_input)
                Tabuada.init(self.operation, self.tableof, self.mode)


                if len(user_input) > 1:
                    _input = user_input.split(" ")
                else:
                    if user_input.upper() in Tabuada.operations:
                        key = Tabuada.operations[ user_input.upper() ]
                        Tabuada.init(operation=key)
                    else:
                        Pydagogue.reminder += 1
                        if Pydagogue.reminder == 5:
                            Pydagogue.reminder = 0
                            self.menu()


            except EOFError:
                pass
            except KeyboardInterrupt:
                sys.exit(0)


if __name__ == '__main__':
    Pydagogue(None, None, 'EASY')
