from .plugin import Plugin
import importlib
import importlib.metadata
import pkgutil
import types

import typer

from .. import consts

DiscoveredPlugins = dict[str, types.ModuleType]
loaded_plugins: list[Plugin] | None = []


def discover_plugins(prefix: str) -> DiscoveredPlugins:
    return {
        name: importlib.import_module(name)
        for finder, name, _
        in pkgutil.iter_modules()
        if name.startswith(prefix)
    }


def load_plugin(app: typer.Typer, module: types.ModuleType, package_name: str) -> None:
    plugin_name: str | None = module.PLUGIN_NAME.removeprefix(consts.PLUGIN_PREFIX)
    plugin_app: typer.Typer | None = module.app
    try:
        plugin_version: str = importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        plugin_version: str = 'unknown'
    if plugin_name and plugin_app:
        app.add_typer(plugin_app, name=plugin_name.lower())
        loaded_plugins.append(Plugin(plugin_name, plugin_version))


def load_plugins(prefix: str, app: typer.Typer) -> None:
    available_plugins = discover_plugins(prefix)
    for name, plugin in available_plugins.items():
        load_plugin(app, plugin, name)
