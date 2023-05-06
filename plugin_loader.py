import importlib
import json

def load_plugin_config():
    with open('plugin_config.json', 'r') as f:
        return json.load(f)

PLUGIN_CONFIG = load_plugin_config()

def load_plugin(plugin_name: str) -> 'MessagePlugin':
    try:
        plugin_info = PLUGIN_CONFIG[plugin_name]
        plugin_module = importlib.import_module(plugin_info['module'])
        plugin_class = getattr(plugin_module, plugin_info['class'])
    except (KeyError, AttributeError, ModuleNotFoundError):
        raise Exception(f"Plugin {plugin_name} not found")
    
    return plugin_class()