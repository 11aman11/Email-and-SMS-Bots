from twilio.rest import Client

account_sid = 'AC04e74998f43d802bb0d9af9556d82d4f'
auth_token = '811d4ffe371443c0ebeabc9801643e15'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              messaging_service_sid='MG0d77cd91a15b8eaac3736c48c642a049',
                              body='hey wassup! I hope to receive a txt msg.',
                              to='+14384084778'
                          )

print(message.sid)