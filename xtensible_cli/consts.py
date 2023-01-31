import importlib.metadata
import typer

APP_NAME = 'xtensible'

PLUGIN_PREFIX = 'xtensible_'
VERSION = importlib.metadata.version(APP_NAME)
CONFIG_DIR = typer.get_app_dir(APP_NAME)
