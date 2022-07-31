from rejson import Path


class Cache:
    def __init__(self, json_client):
        self.json_client = json_client

    async def get_chat_history(self, token: str):
        return self.json_client.jsonget(token, Path.rootPath())
