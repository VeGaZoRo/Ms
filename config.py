from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","19525325"))
API_HASH = getenv("API_HASH","ddc123dd015945669f20498bd0a50409")

BOT_TOKEN = getenv("BOT_TOKEN","6733899123:AAHIOd2Bg_BH8LQGrztzwRkO3D60t_-I_qE")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mohamedhelal:mohamedhelal@cluster0.qhhuj2p.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6909581339))
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VeGaOne")
