import asyncio
import os
import sys
import types


def _as_int(name: str, default: int = 0) -> int:
    value = os.getenv(name)
    if value is None or value == "":
        return default
    try:
        return int(value)
    except ValueError as exc:
        raise RuntimeError(f"Environment variable {name} must be an integer") from exc


required = ["API_ID", "API_HASH", "BOT_TOKEN"]
missing = [name for name in required if not os.getenv(name)]
if missing:
    raise RuntimeError(
        "Missing required environment variables: " + ", ".join(missing)
    )

config = types.ModuleType("config")
config.API_ID = _as_int("API_ID")
config.API_HASH = os.getenv("API_HASH", "")
config.BOT_TOKEN = os.getenv("BOT_TOKEN", "")
config.UPDATE_CHANNEL_URL = os.getenv("UPDATE_CHANNEL_URL", "t.me/abirxdhackz")
config.COMMAND_PREFIXES = [p.strip() for p in os.getenv("COMMAND_PREFIXES", "/,!,.,,,$,#").split(",") if p.strip()]
config.OWNER_ID = _as_int("OWNER_ID", 123456789)
config.DEVELOPER_USER_ID = _as_int("DEVELOPER_USER_ID", config.OWNER_ID)
config.LOG_CHANNEL_ID = _as_int("LOG_CHANNEL_ID", -1001234567890)
config.VIDEO_QUALITY_OPTIONS = {
    "1080p": {"label": "1080p Full HD", "height": 1080},
    "720p": {"label": "720p HD", "height": 720},
    "480p": {"label": "480p SD", "height": 480},
    "360p": {"label": "360p Low", "height": 360},
    "144p": {"label": "144p Very Low", "height": 144},
}
config.AUDIO_QUALITY_OPTIONS = {
    "320kbps": {"label": "320kbps Best", "bitrate": "320"},
    "256kbps": {"label": "256kbps High", "bitrate": "256"},
    "128kbps": {"label": "128kbps Medium", "bitrate": "128"},
    "64kbps": {"label": "64kbps Low", "bitrate": "64"},
}

sys.modules["config"] = config

from main import main


if __name__ == "__main__":
    asyncio.run(main())
