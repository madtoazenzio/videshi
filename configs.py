import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
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
