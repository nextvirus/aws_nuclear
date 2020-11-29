import boto3

def ALB():
    ALB = []
    client = boto3.client('elbv2')
    response = client.describe_load_balancers()
    for i in range(0,len(response['LoadBalancers'])):
        ALB.append(response['LoadBalancers'][i]['LoadBalancerArn'])

    for a in range(0, len(ALB)):
        question = client.describe_listeners(
            LoadBalancerArn=ALB[a]
        )
        for listener in question['Listeners']:
            client.delete_listener(
                ListenerArn = listener['ListenerArn']
            )

    for j in range(0,len(ALB)):
        answer = client.delete_load_balancer(
            LoadBalancerArn = ALB[j]
        )

def TG():
    TG = []
    client = boto3.client('elbv2')
    respone = client.describe_target_groups()
    for i in range(0, len(respone['TargetGroups'])):
        TG.append(respone['TargetGroups'][i]['TargetGroupArn'])
    
    for j in range(0, len(TG)):
        answer = client.delete_target_group(
            TargetGroupArn = TG[j]
        )
ALB()

