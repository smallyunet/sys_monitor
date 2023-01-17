import requests
import config as cfg

apiUrl = f'api.telegram.org'


def send_text(message):
    global apiUrl
    if not cfg.telegram_enable:
        return
    if cfg.telegram_api_url != "":
        apiUrl = cfg.telegram_api_url

    url = f'https://{apiUrl}/bot{cfg.telegram_api_token}/sendMessage'
    try:
        response = requests.post(
            url, json={
                'chat_id': cfg.telegram_chat_id,
                'caption': 'Catch exception',
                'text': message
            }
        )
    except Exception as e:
        print(e)


def send_md(message):
    global apiUrl
    if not cfg.telegram_enable:
        return
    if cfg.telegram_api_url != "":
        apiUrl = cfg.telegram_api_url

    url = f'https://{apiUrl}/bot{cfg.telegram_api_token}/sendMessage'
    try:
        response = requests.post(
            url, json={
                'chat_id': cfg.telegram_chat_id,
                'caption': 'Catch exception',
                'text': message,
                'parse_mode': 'MarkdownV2'
            }
        )
    except Exception as e:
        print(e)
