import typer
from xtensible_cli.utils import commands as default_commands
from xtensible_cli.utils import commands as config_commands
from xtensible_cli import plugins, consts

app = typer.Typer()
app.add_typer(default_commands.app)
app.add_typer(config_commands.app)
plugins.load_plugins(consts.PLUGIN_PREFIX, app)

if __name__ == '__main__':
    app()
