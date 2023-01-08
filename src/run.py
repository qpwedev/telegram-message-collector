from pyrogram import Client, filters
from pyrogram import Client
import json


def read_config():
    with open("./config.json") as f:
        config = json.load(f)
        return config["API_ID"], config["API_HASH"], config["CHAT_ID"]


API_ID, API_HASH, CHAT_ID = read_config()

if "<YOUR_VALUE>" in [API_ID, API_HASH, CHAT_ID]:
    print("Please enter your API ID, CHAT_ID and API HASH in the config.json file.")
    exit(1)

app = Client("my_account", int(API_ID), API_HASH)

# More about filters at https://docs.pyrogram.org/topics/use-filters
@app.on_message(filters.private | filters.me | filters.channel | filters.group)
async def messsage_forwarder(client, message):
    await message.forward(CHAT_ID, message.chat.id)


if __name__ == "__main__":
    app.run()
