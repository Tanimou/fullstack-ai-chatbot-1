from rejson import Path


class Cache:
    def __init__(self, json_client):
        self.json_client = json_client

    async def get_chat_history(self, token: str):
        return self.json_client.jsonget(token, Path.rootPath())

    async def add_message_to_cache(self, token: str, source: str, message_data: dict):
        if source == "bot":
            message_data['msg'] = "Bot: " + (message_data['msg'])

        elif source == "human":
            message_data['msg'] = "Human: " + (message_data['msg'])
        self.json_client.jsonarrappend(token, Path('.messages'), message_data)
