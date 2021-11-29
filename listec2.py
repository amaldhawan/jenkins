import boto3
import sys

client = boto3.client('ec2', region_name = Region, aws_access_key_id= Accesskey, aws_secret_access_key = Secretkey)

mohanec2 = client.describe_instances()
for mohan1 in mohanec2['Reservations']:
	for mohan2 in mohan1['Instances']:
		for mohan3 in mohan2['Tags']:
			print(mohan2['InstanceId'])
			print(mohan2['InstanceType'])
			print(mohan2['LaunchTime'])
			print(mohan2['State']['Name'])
			print(mohan3['Value'])
    
