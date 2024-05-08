import boto3
import json

payload = json.dumps(
{
  "message": "From Downlinker"
})

client = boto3.client('iot-data', region_name='us-east-1')

response = client.publish(
    topic='QTBin_sub/',
    qos=1,
    payload=payload
)

print(response)