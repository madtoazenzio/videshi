import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "7236453"))
  API_HASH = os.environ.get("API_HASH", "33010a70e94f80e55145980072cce969")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7944481456:AAGlfvhDrUiNsqaz3KO38lw9oBxTup-DbBU")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "zooiwestbot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002319985549"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "gplinks.co")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "e89896f9832eba6d9c5cef8212e0d465b8adc241")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6891428437"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://madtoazenzio:f9oDLc4c6H5zdP44@devutty.pk5so.mongodb.net/?retryWrites=true&w=majority&appName=devutty")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002231278815")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002319985549"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [Mᴇ](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 Sᴏᴍᴇᴡʜᴇʀᴇ Iɴ Eᴀʀᴛʜ!
"""
  HOME_TEXT = """
𝙃𝙚𝙡𝙡𝙤, [{}](tg://user?id={})\n\n𝙏𝙝𝙞𝙨 𝙗𝙤𝙩 𝙗𝙮 シ︎.

ಠ_ಠ

📢 𝖧𝗈𝗌𝗍𝖾𝖽𝖮𝗇 :-𝖮𝗄𝗍𝖾𝗍𝗈¡.

⚠️ 𝗪𝗮𝗿𝗻:𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝗂𝗌 𝗈𝖿𝖿𝗂𝖼𝗂𝖺𝗅𝗒 𝗐𝗈𝗋𝗄𝗂𝗇𝗀 𝖿𝗈𝗋 𝖹𝗈𝗈𝗂𝖲𝗍𝗈𝗋𝖾 𝖲𝗈 𝖽𝗈𝗇'𝗍 𝖲𝖾𝗇𝖽 𝖥𝗂𝗅𝖾𝗌 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗅𝗂𝗇𝗄 𝗁𝖾𝗋𝖾! 𝗈𝗍𝗁𝖾𝗋𝗐𝗂𝗌𝖾 𝗒𝗈𝗎 𝗐𝗂𝗅𝗅 𝗀𝖾𝗍 𝖻𝖺𝗇.
"""
