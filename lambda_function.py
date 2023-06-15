import json
import urllib3
import requests


def send_slack_message(event):
    http = urllib3.PoolManager()
    slack_text = f"{event}"
    print(slack_text)
    data = {"text": slack_text}
    request = http.request("POST",
                           "https://hooks.slack.com/services/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",
                           body=json.dumps(data),
                           headers={"Content-Type": "application/json"})

def send_whatsapp_message(event, number):
    url = "https://api.ultramsg.com/instance50806/messages/chat"
    payload = f"token=vi9d9iw5e07ez32c&to={number}&body={event}"
    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

def lambda_handler(event, context):
    # TODO implement
    phone_number = "+972584164863"
    send_slack_message(event)
    send_whatsapp_message(event, phone_number)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
