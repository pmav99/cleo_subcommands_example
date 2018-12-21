from ..command import Command


class Sub1Command(Command):
    """
    Display information about the Subcommand 1

    sub1
        {--p|path : Only display the environment's path}
    """

    def handle(self):
        self.line("Sub1!")
