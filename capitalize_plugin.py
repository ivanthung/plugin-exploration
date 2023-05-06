from plugin_interface import MessagePlugin

class CapitalizePlugin(MessagePlugin):
    def process(self, message: str) -> str:
        return message.upper()