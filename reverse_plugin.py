from plugin_interface import MessagePlugin

class ReversePlugin(MessagePlugin):
    def process(self, message: str) -> str:
        return message[::-1]
    
                    