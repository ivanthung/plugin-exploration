from plugin_interface import MessagePlugin

class EricPlugin(MessagePlugin):
    def process(self, message: str) -> str:
        return f' "{message}" .... seriously? Fuck off Eric!'