# import boto3
import json
import time

def cloudwatch_resources():     #cloudwathc alarm
    cloudwatch = boto3.resource('cloudwatch')
    alarm = cloudwatch.alarms.all()
    return  list(alarm)

def delete_cloudwatch_resources(): 
    cloudwatch = boto3.resource('cloudwatch')
    response = cloudwatch.alarms.delete()
    
def efs_resources():  #efs  target-mount efs
    efs_name = []
    efs = dict()
    Id = []
    i = int(input("你有几个EFS："))
    for f in range(0, i):
        if i == 0 :
            break
        else:
            efs_name.append(input("请输入efs的ID:"))
            Id.append(i)
            efs.update({efs_name[i]:Id[i]})
    return efs

def efs_targetmount_resources():  
    efs_target_name=[]
    efs_target=dict()
    Id=[]
    i = int(input("你有几个EFS的tagert mount:"))
    for f in range(0,i):
        if i == 0:
            break
        else:
            efs_target_name.append(input("请输入efs的挂在目标的ID"))
            Id.append(f)
            efs_target.update({efs_target_name[f]:Id[f]})
    return efs_target

def delete_target(**target):
    client = boto3.client('efs')
    Id = list(target.keys())
    for i in range(0, len(Id)):
        if Id == None:
            break
        else:
            response = client.delete_mount_target(MountTargetId=Id[i])
    
def delete_efs(**name):
    client = boto3.client('efs')
    Id =  list(name.keys())
    for i in range(0, len(Id)):
        if Id == None:
            break
        else:
            response = client.delete_file_system( 
                FileSystemId = Id[i]
    )
    
def ALB_resources():     # alb
    ALB = dict()
    arn = list()
    alb = []
    i = int(input("你有几个ALB："))
    for f in range(0, i):
        if i == 0 :
            break
        else:
            alb.append(input("请输入ARN："))
            arn.append(f)
            ALB.update({alb[f]:arn[f]})
    return ALB

def delte_AlB(**ARN):
    client = boto3.client('elbv2')
    Id=list(alb.keys())
    for i in range(0,len(Id)):
        if Id ==None:
            break
        else:
            response = client.delete_load_balancer(
                LoadBalancerArn = Id[i]
        )
    
def TG_resources():  #Tg
    arn = []
    TG = []
    tg=dict()
    i = int(input("你有几个TG："))
    for f in range(0, i):
        if i == 0:
            break
        else:
            arn.append(input("请输入TG的ARN："))
            TG.append(i)
            tg.update({arn[f]:TG[f]})
    return tg

def delete_TG(**tg):
    client = boto3.client('elbv2')
    Id=list(tg.keys())
    for i in range(0,len(Id)):
        if Id == None:
            break
        else:
            response = client.delete_target_group(
                  TargetGroupArn = Id[i]
        )

def VPC_resources(): # VPC
    VPC = []
    ec2=boto3.resource('ec2')
    for vpc in ec2.vpcs.all():
        VPC.append(vpc.id)
    return VPC

def delete_vpc(*vpc):
    client = boto3.client('ec2')
    for i in range(0,len(vpc)):
        if vpc == None:
            break
        else :
            response = client.delete_vpc(
                VpcId = vpc[i]
        )
    
''''
def image_resource():   #image
    ec2 = boto3.resource('ec2')
    for image in ec2.images.all():
        print(image.id) 
    return list(image.id)
''' 
def instance_resources():   #instance
    instances = []
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print(instance.id)
        instances.append(instance.id)
    return instances

def delete_launch_instance(*instance):
    client = boto3.client('ec2')
    for i in range(0,len(instance)):
        if instance == None:
            break
        else:
            response = client.delete_launch_template(
                LaunchTemplateId = instance[i]
        )
    
    
def internet_gateways_resources():        #IGW
    igw=[]
    ec2 = boto3.resource('ec2')
    for IGW in ec2.internet_gateways.all():
        print(IGW.id)
        igw.append(IGW.id)
    return igw

def delete_internet_gateways(*igw):
    client = boto3.client('ec2')
    for i in range(0, len(igw)):
        if igw == None:
            break
        else:
            response = client.delete_internet_gateway(
                InternetGatewayId = igw[i]
    )
        
def route_table_resources():  #route_table
    route_table=[]
    ec2 = boto3.resource('ec2')
    for route in ec2.route_tables.all():
        print(route.id)
        route_table.append(route.id)
    return route_table

def delete_route_table(*route_table):
    client = boto3.client('ec2')
    for i in range(0, len(route_table)):
        if route_table == None:
            break
        else:
            response = client.delete_route_table(
                RouteTableId = route_table[i]
        )
''''   
def snapshots_resource():   #snapshots
    snapshots=[]
    ec2 = boto3.resource('ec2')
    for snapshot in ec2.snapshots.all():
        print(snapshot.id)
        snapshots.append(snapshot.id)
    return snapshots
'''''

def subnets_resources():   #subnets
    subnets = []
    ec2 = boto3.resource('ec2')
    for subnet in ec2.subnets.all():
        print(subnet.id)
        subnets.append(subnet.id)
    return subnets

def delete_subnets(*subnet):
    client = boto3.client('ec2')
    for i in range(0, len(subnet)):
        if subnet == None:
            break
        else:
            respone = client.delete_subnet(
                SubnetId = subnet[i]
            )

def nat_gateway_resources():
    nats = {}
    nat = []
    value = []
    num = int(input("请输入Nat网关的个数:"))
    for i in range(0, num):
        if num == 0:
            break
        else:
            nat_name = input("请输入Nat网关的id：")
            nat.append(nat_name)
            value.append(i)
            nats.update({nat[i]:value[i]})
    return nats

def delete_nat_gateway(**nats):
    client = boto3.client('ec2')
    Id = list(nats.keys())
    for i in range(0, len(Id)):
        if nats == None:
            break
        else:
            respone = client.delete_nat_gateway(
                NatGatewayId = Id[i]
        )

def EIP_resources(): #EIP
    eip = []
    EIP = {}
    Id = []
    i = int(input("请输入有EIP的个数"))
    for f in range(0, i):
        if i == 0:
            break
        else:
            name = input("请输入EIP的ID：")
            eip.append(name)
            Id.append(f)
            EIP.update({eip[f]:Id[f]})
    return EIP

def delete_EIP(**eip):
    client = boto3.client('ec2')
    Id = list(eip.keys())
    for i in range(0,len(Id)):
        if Id == None:
            break
        else:
            respone = client.release_address(
                AllocationId = Id[i]
            )
            
def ASG_resources():  #auto_scaling
    asg = []
    ASG = {}
    Id = []
    i = int(input("请输入你有几个ASG:"))
    for f in range(0,i):
        if i == 0:
            break
        else :
            name = input("请输入ASG的Id")
            asg.append(name)
            Id.append(i)
            ASG.update({asg[f]:Id[f]})
    return ASG

def delete_ASG(**asg):
    client = boto3.client('autoscaling')
    Id = list(asg.keys())
    for i in range(0,len(Id)):
        if Id == None:
            break
        else:
            respone = client.delete_auto_scaling_group(
                AutoScalingGroupName = Id[i]  )
            
def ASG_configure():    #asg模板
    asg_configure = []
    ASG_configure = {}
    Id = []
    i = int(input("请输入你有几个ASG_configure:"))
    for f in range(0,i):
        if i == 0:
            break
        else :
            name = input("请输入ASG的Id")
            asg_configure.append(name)
            Id.append(i)
            ASG_configure.update({asg_configure[f]:Id[f]})
    return ASG_configure

def delete_ASG_configure(**asg_configure):
    client = boto3.client('autoscaling')
    Id = list(asg_configure.keys())
    for i in range(0,len(Id)):
        if Id == None:
            break
        else:
            respone = client.delete_auto_scaling_group(
                AutoScalingGroupName = Id[i]  )
        
''''    
def network_interfaces_resource():     #nat
    nats = []
    ec2 = boto3.resource('ec2')
    for nat in ec2.network_interfaces.all():
        print(nat.id)
        nats.append(nat.id)
    return nats
'''''

if __name__ == '__main__' :
    delete_cloudwatch_resources() #删除警告
    target = efs_targetmount_resources()#获得efs_target_mount资源
    delete_target(**target) #删除efs_target_mount资源
    name = efs_resources()#获得efs资源
    delete_efs(**name) #删除efs
    asg_configure = ASG_configure() #获得ASG模板
    delete_ASG_configure(**asg_configure) #删除Asg模板
    asg = ASG_resources() #获得ASG资源
    delete_ASG(**asg)  #删除ASG
    nats = nat_gateway_resources() #获得nat资源
    delete_nat_gateway(**nats)   #删除nats
    sleep(10)
    eip = EIP_resources()#获得eip资源
    delete_EIP(**eip)  #删除eip
    ARN = ALB_resources() #获得ALB资源
    delte_AlB(**ARN)         #删除ALB
    sleep(10)
    tg = TG_resources()#获得Tg资源
    delete_TG(**tg) #删除Tg
    subnet = subnets_resources() #获得子网资源
    delete_subnets(*subnet) #删除子网
    route_table = route_table_resources() #获得路由表资源
    delete_route_table(*route_table) #删除路由表
    igw = internet_gateways_resources() #获得igw资源
    delete_internet_gateways(*igw) #删除igw
    instance = instance_resources() #获得Instance资源
    delete_launch_instance(*instance)#删除实例
    vpc = VPC_resources() #获得vpc资源
    delete_vpc(*vpc)#删除vpc资源
    print("nuclear mission complete")
    



