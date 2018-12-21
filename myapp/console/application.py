from cleo import Application as BaseApplication

from .commands import Cmd1Command
from .commands import Cmd2Command
from .commands import Cmd3Command

from .. import __version__


class Application(BaseApplication):

    def __init__(self):
        super(Application, self).__init__("myapp", __version__)

        for command in self.get_default_commands():
            self.add(command)

    def get_default_commands(self) -> list:
        commands = [
            Cmd1Command(),
            Cmd2Command(),
            Cmd3Command(),
        ]
        return commands
