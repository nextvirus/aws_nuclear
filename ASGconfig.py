import boto3

client  = boto3.client('autoscaling')

for config in client.describe_launch_configurations()['LaunchConfigurations']:
    print(config)