from .command import Command


class Cmd3Command(Command):
    """
    Do some cmd3 stuff.

    cmd3
    """

    help = "The <info>cmd3</> command does cmd3 stuff."

    def handle(self):
        self.line("<warning>This is cmd3!</warning>")
        self.line("")
