from os import environ as env

class Telegram:
    API_ID = int(env.get("API_ID", "23336308"))
    API_HASH = env.get("API_HASH", "884c5a2f4583f875d9d021b222e1d752")
    BOT_TOKEN = env.get("BOT_TOKEN", "")
    BOT_USERNAME = env.get("BOT_USERNAME", "")
    EMOJIS = [
        "👍", "🥰", "❤", "🍌",
        "🔥", "❤️",
    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
