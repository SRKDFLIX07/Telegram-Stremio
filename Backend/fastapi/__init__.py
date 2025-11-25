import uvicorn
from Backend.config import Telegram


Port = Telegram.PORT
config = uvicorn.Config(app=app, host='0.0.0.0', port=Port)
server = uvicorn.Server(config)
