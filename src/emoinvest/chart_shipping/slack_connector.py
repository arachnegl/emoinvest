from emoinvest.configurations.config_reader import get_config_reader

from slacker import Slacker

configuration_reader = get_config_reader()

slack = Slacker(configuration_reader.get('settings', 'slack_key'))


def _get_image_url(file_name):
    return 'https://s3.eu-central-1.amazonaws.com/emoinvest/' + str(file_name)


def send_chart(message, title, chart_name):
    image_url = _get_image_url(chart_name)

    attachement = {
        "color": "#2eb886",
        "author_name": "Code Monkey",
        "title": title,
        "title_link": image_url,
        "image_url": image_url,
        "fields": [
            {
                "short": False,
            }
        ],
    }

    slack.chat.post_message('#bot_test', text=message, attachments=[attachement])
    return True
