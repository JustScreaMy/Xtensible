import typer

from xtensible_cli import consts
from xtensible_cli.plugins import loaded_plugins

app = typer.Typer(name="utils")


@app.command(name="version", short_help="Shows the current version of this application")
def _version():
    print(f"Current version is {consts.VERSION}")


@app.command(name="plugins", short_help="Get list of all installed plugin")
def _get_plugins():
    if not loaded_plugins:
        print("No plugins has been loaded yet :(")
        raise typer.Exit()
    for plugin in loaded_plugins:
        print(f"Plugin name {plugin.name}@{plugin.version}")


@app.command(
    name="confdir", short_help="Print directory xtensible uses for storing config files"
)
def _get_confdir():
    print(f"Config dir is located at\n{consts.CONFIG_DIR}")
