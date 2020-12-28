import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1403433166:AAGhZGRVZ01JwLr7oWKIikwj7IVRo8_dkpk")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 2531583))
    API_HASH = os.environ.get("API_HASH", "f74a2df1e1eb698c65c22302d78512a0")
    OWNER_ID = int(os.environ.get("OWNER_ID", 971853202))
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001418440230").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 4096))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 6000))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    R_CLONE_CONF_URI = os.environ.get("R_CLONE_CONF_URI", None)
    # Destination folder for the rclone
    R_CLONE_DEST = os.environ.get("R_CLONE_DEST", "/PublicLeech")
    # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = os.environ.get("SHOULD_USE_BUTTONS", False)
    #
    LOG_FILE_ZZGEVC = os.environ.get("LOG_FILE_ZZGEVC", "PublicLeech.log")
    #
    SP_LIT_ALGO_RITH_M = os.environ.get(
        "SP_LIT_ALGO_RITH_M",
        "hjs"
    )
    #
    DIS_ABLE_ST_GFC_COMMAND_I = os.environ.get(
        "DIS_ABLE_ST_GFC_COMMAND_I",
        False
    )
