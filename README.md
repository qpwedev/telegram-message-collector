# Telegram Message Collector
This python project allows you to collect all incoming messages in a dedicated Telegram channel. It runs on Python 3 and uses the Pyrogram library.

## Configuration
The project uses a config.json file with the following data:

```
{
    "API_ID": "<YOUR_VALUE>",
    "API_HASH": "<YOUR_VALUE>",
    "CHAT_ID": "<YOUR_VALUE>"
}
```
To get the `API_ID` and `API_HASH` for your Telegram application, follow these steps:

1. Go to the [Telegram API Portal](https://my.telegram.org/auth).
2. Login with your phone number.
3. Click on the API development tools link.
4. Click on the Create New Application button.
5. Fill in the required fields and click on the Create button.
6. Your `API_ID` and `API_HASH` will be displayed on the next page.


To get the `CHAT_ID` of a channel in Telegram, you can use the `@username_to_id_bot`. Follow these steps:

1. Forward a message from the channel you want to get the `CHAT_ID` for to the `@username_to_id_bot`.
2. The bot will send you a message with the `CHAT_ID` of the channel.

## Usage

To use this project, clone the repository and install the required dependencies:

1. Copy code
``` git clone https://github.com/<your_username>/telegram-channel-collector.git
cd telegram-channel-collector
pip install -r requirements.txt 
```

2. Then, edit the `config.json` file with your `API_ID`, `API_HASH`, and `CHAT_ID`.

Finally, run the script:

1. Copy code
```
python3 ./src/run.py
```
