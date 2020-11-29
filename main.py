import MongoDB
import EC2
import ALB
import vpc
import ECR
import ECS 

def login():
    ACCESS_KEY=input("请输入AK：")
    SECRET_KEY=input("请输入SK：")
    SESSION_TOKEN=input("请输入token：")
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN
)

if __name__ == "__main__":
    print("请输入在cmd中输入'aws sts get-ssesion-token'获取需要的信息")
    #login()
    EC2.list_instance()
    print("ec2清理完成")
    ALB.ALB()
    print("ALB清理完成")
    ALB.TG()
    print("TG清理完成")
    #ECS.ecs_cluster()
   # print("ecs cluster 清除完成")
    ECR.ecr()
    print("ECR 清理完成")
    #MongoDB.docdb_instances()
    #MongoDB.docdb_cluster()
    #MongoDB.docdb_subnet_groups()
    print("DocumentDB清理完成")
    vpcs=vpc.VPC_resources()
    vpc.list_endpoints()
    vpc.list_igw()
    vpc.list_security_groups()
    vpc.list_route_tables()
    vpc.list_subnets()
    vpc.list_vpc(*vpcs)
    print("VPC清理完成")
    print("mission complete")
    



