#@Multimeterv3 

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", ))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 5546958418)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
