import json
import boto3

client = boto3.client('events')
name = str(input("Please enter your name: "))
lastname = str(input("Please enter last name: "))
company = str(input("Please enter the comapny you work at: "))

event = {'name': f'{name}', 'lastname': f'{lastname}', 'company': f'{company}'}

response = client.put_events(
        Entries=[
            {
            'Source': 'my-event',
            'DetailType': 'Send Event to Registration Service',
            'Detail': json.dumps(event),
            'EventBusName': 'User-Registry',
             },
                ]
)

print(response)