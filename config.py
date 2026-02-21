from os import getenv

class Config:
    def __init__(self):
        # Hardcoded credentials
        self.API_ID = 20500696
        self.API_HASH = "4a088ffb8ec5377f9dcfcdb011062699"
        self.BOT_TOKEN = "8231185581:AAGNBj-AwopeqInCS9QbOwhfIa2e73-cxgg"
        self.MONGO_URL = "mongodb+srv://mvstream:Kp883249943@mvstreaming.kcun0lr.mongodb.net/?appName=MvStreaming"
        self.OWNER_ID = 6158106622
        self.LOGGER_ID = -1003787292420
        self.SESSION1 = "BQE40NgAiJ-4IfUFEoPI0YUfdhjCTDiakRuMjphGyhOWZUeJC1l6g8XIPLpPJlTSiv8Frb9uq_RxV5br_wqjMQ2BST07NyfrvOIPsmwLwSrKd9Bzi6__uCiQX8_4YA9_nrIDtu5rw-vVE2XKk79nigHJ17jIUTfGMX9pxWsIVwBllOBgF9-QhQsms2AAIL3LYsnQEXKPEdX3w5e0MELlGdm7I1S2Mx9_TK6fT1JP9nU03ZUyXPNoFsQYLLLVg8wf8Lvbf8y6JMmW0w1mZKnqeMK9fAA-x5So7kgSzVxgtVsp08D1kl07c8KzM1knTi6NlajPFJLN6nuLfni7lOxHQa-0gDGyFgAAAAFYxdxhAA"

        # Other configurations
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)
        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AljonChannel")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Aljon_Family")
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"
        self.LANG_CODE = getenv("LANG_CODE", "en")
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
