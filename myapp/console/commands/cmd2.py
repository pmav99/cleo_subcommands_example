from .command import Command


class Cmd2Command(Command):
    """
    Do some cmd2 stuff.

    cmd2
    """

    help = "The <info>cmd2</> command does cmd2 stuff."

    def handle(self):
        self.line("<error>This is cmd2!</error>")
        self.line("")
