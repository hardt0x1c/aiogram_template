import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
bot_name = os.getenv('BOT_NAME')
admin_id = int(os.getenv('ADMIN_ID'))
admin_name = os.getenv('ADMIN_NAME')
