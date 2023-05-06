class MessagePlugin:
    def process(self, message:str) -> str:
        raise NotImplementedError("Plugin must be implemented")
    