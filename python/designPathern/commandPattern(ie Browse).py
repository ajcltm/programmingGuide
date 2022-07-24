"""
Encapsulate a request as an object, thereby letting you parameterize
clients with different requests, queue or log requests, and support
undoable operations.
"""

import abc


class Invoker:
    """
    The invoker accepts a command object and handles it generically like a CLI
    """

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

    def history(self):
        for command in self._commands:
            command.outputname()

class Command(metaclass=abc.ABCMeta):
    """
    This is the interface for handling an operation
    """

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def outputname(self):
        pass


class ConcreteCommand(Command):
    """
    This defines the binding betwen the Receiver object and an operation.
    The command Execution invokes the corresponding the operation on the Receiver
    """

    def execute(self):
        self._receiver.browse()

    def outputname(self):
        self._receiver.outputname();

class Goat:
    """
    The goat knows how to browse. This is a receiver for a command from the invoker.
    """

    def browse(self):
        print("delicious twigs and foliage!")

    def outputname(self):
        print("goat")

class Shopper:
    """
    The shopper also knows how to browse. This is a receiver for a command from the invoker.
    """

    def browse(self):
        print("look at the fine array of goods!")

    def outputname(self):
        print('shopper')

class Browser:
    """
    Know what else knows how to browse?
    An internet browser!
    This is a receiver for a command from the invoker.
    """
    descriptor = 'Browser browses web pages'
    def browse(self):
        print("serving up the next web page")

    def outputname(self):
        print("browser")

def main():
    receiver = Goat()
    receiver2 = Shopper()
    receiver3 = Browser()

    concrete_command = ConcreteCommand(receiver)
    concrete_command2 = ConcreteCommand(receiver2)
    concrete_command3 = ConcreteCommand(receiver3)
    invoker = Invoker()
    invoker.store_command(concrete_command)
    invoker.store_command(concrete_command2)
    invoker.store_command(concrete_command3)
    invoker.history()
    invoker.execute_commands()

if __name__ == "__main__":
    main()