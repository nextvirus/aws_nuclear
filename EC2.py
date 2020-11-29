import boto3

def list_instance():
    ec2 = boto3.resource('ec2')
    instances=[]
    for instance in ec2.instances.all():
        instances.append(instance.id)
    
    for j in range(0, len(instances)):
        instance = ec2.Instance(instances[j])
        response = instance.terminate(
            DryRun = False
        )
