from starlette.config import Config

config = Config(".env")

TOKEN = '5073463122:AAGgzRnl4cGYI2buhyJ3ZwUsRshVLq9vpdQ'
DATABASE: str = config("DATABASE")
USER: str = config("USER")
PASSWORD: str = config("PASSWORD")