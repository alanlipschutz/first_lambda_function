import json
import urllib3
import requests


def lambda_handler(event, context):
    # TODO implement
    http = urllib3.PoolManager()

    slack_text = f"{event['Records']}"

    print(slack_text)

    data = {"text": slack_text}

    request = http.request("POST",
                           "https://hooks.slack.com/services/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",
                           body=json.dumps(data),
                           headers={"Content-Type": "application/json"})

    url = "https://api.ultramsg.com/instance50806/messages/chat"

    payload = f"token=vi9d9iw5e07ez32c&to=+972584164863&body={event['Records']}"
    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
