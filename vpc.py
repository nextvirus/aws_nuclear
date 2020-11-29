import boto3

def VPC_resources(): # VPC
    VPC = []
    ec2=boto3.resource('ec2')
    for vpc in ec2.vpcs.all():
        VPC.append(vpc.id)
    return VPC

def list_vpc(*vpcs):
    cidr=[]
    client=boto3.client('ec2')
    for i in range(0 , len(vpcs)):
        response = client.describe_vpcs()
        if response['Vpcs'][i]['CidrBlock']=='172.31.0.0/16':
            continue
        else:
            cidr.append(response['Vpcs'][i]['VpcId'])
    
    for j in range(0, len(cidr)):
        answer = client.delete_vpc(
            VpcId = cidr[j],
            DryRun = False
        )

def list_subnets():
    subnets = []
    client = boto3.client('ec2')
    response = client.describe_subnets()
    for i in range(0, len(response['Subnets'])):
        if len(response['Subnets'][i]['VpcId'])>12:
            subnets.append(response['Subnets'][i]['SubnetId'])
        else:
            continue
    
    for j in range(0,len(subnets)):
        answer = client.delete_subnet(
            SubnetId = subnets[j],
            DryRun = False
        )

def list_route_tables():
    route_table=[]
    client = boto3.client('ec2')
    response = client.describe_route_tables()
    for i in range(0, len(response['RouteTables'])):
        if len(response['RouteTables'][i]['VpcId']) >12 :
            if len(response['RouteTables'][i]['Associations']) == 1:
                continue
            else:
                route_table.append(response['RouteTables'][i]['RouteTableId'])          
        else:
          continue

    for j in range(0, len(route_table)):
        answer = client.delete_route_table(
            DryRun = False,
            RouteTableId = route_table[j]
        )

def list_igw():
    client = boto3.client('ec2')
    igw=[]
    response = client.describe_internet_gateways()
    for i in range(0, len(response['InternetGateways'])):
        if len(response['InternetGateways'][i]['Attachments'][0]['VpcId'])>12:
                igw.append(response['InternetGateways'][i]['InternetGatewayId'])
                a = client.detach_internet_gateway(
                DryRun = False,
                VpcId = response['InternetGateways'][i]['Attachments'][0]['VpcId'],
                InternetGatewayId = igw[i]
            )

    for j in range(0, len(igw)):
        answer = client.delete_internet_gateway(
            DryRun = False,
            InternetGatewayId = igw[j]
        )

def list_endpoints():
    client = boto3.client('ec2')
    endpoints = []
    response = client.describe_vpc_endpoints()
    for i in range(0, len(response['VpcEndpoints'])):
        endpoints.append(response['VpcEndpoints'][i]['VpcEndpointId'])

    for j in range(0, len(endpoints)):
        response = client.delete_vpc_endpoints(
            DryRun = False,
            VpcEndpointIds = [
                endpoints[j]
             ]
        )

def list_security_groups():
    client = boto3.client('ec2')
    security_groups=[]
    response = client.describe_security_groups()
    for i in range(0, len(response['SecurityGroups'])):
        security_groups.append(response['SecurityGroups'][i]['GroupId'])

    for  j in range(len(security_groups)-1,-1,-1):
        if response['SecurityGroups'][j]['GroupName'] == 'default':
            continue
        else:
            answer = client.delete_security_group(
                GroupId = security_groups[j],
                DryRun = False
            )








