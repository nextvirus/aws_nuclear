import boto3
def deleteasg():
    asg=[]
    groups=[]
    client = boto3.client('autoscaling')
    response = client.describe_launch_configurations()
    group = client.describe_auto_scaling_groups()
    for i in response['LaunchConfigurations']:
        asg.append(i['LaunchConfigurationName'])
    for j in group['AutoScalingGroups']:
        groups.append(j['AutoScalingGroupName'])
    for k in groups:
        client.delete_auto_scaling_group(
            AutoScalingGroupName=k,
            ForceDelete=True
    )
    for l in asg:
        response = client.delete_launch_configuration(
        LaunchConfigurationName=l
    )