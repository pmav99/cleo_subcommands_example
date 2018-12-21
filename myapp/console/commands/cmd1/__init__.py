from ..command import Command

from .sub1 import Sub1Command
from .sub2 import Sub2Command


class Cmd1Command(Command):
    """
    A command that has some subcommands.

    cmd1
    """

    commands = [Sub1Command(), Sub2Command()]

    def handle(self):  # type: () -> int
        return self.call("help", self._config.name)
