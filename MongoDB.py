import boto3

def docdb_instances():
    db=[]
    client = boto3.client('docdb')
    response = client.describe_db_instances()
    for i in range(0, len(response['DBInstances'])):
        db.append(response['DBInstances'][i]['DBInstanceIdentifier'])
        
    for j in range(0, len(db)):
        answer = client.delete_db_instance(
            DBInstanceIdentifier = db[j]
        )

def docdb_cluster():
    cluster = []
    client = boto3.client('docdb')
    response = client.describe_db_clusters()
    for i in range(0, len(response['DBClusters'])):
        cluster.append(response['DBClusters'][i]['DBClusterIdentifier'])
    
    for j in range(0,len(cluster)):
        question = client.modify_db_cluster(
            DBClusterIdentifier = cluster[j],
            DeletionProtection = False
        )
        answer = client.delete_db_cluster(
            DBClusterIdentifier = cluster[j],
            SkipFinalSnapshot = True 
        )

def docdb_subnet_groups():
    groups = []
    client = boto3.client('docdb')
    response = client.describe_db_subnet_groups()
    for i in range(0, len(response['DBSubnetGroups'])):
        groups.append(response['DBSubnetGroups'][i]['DBSubnetGroupName'])
    
    for j in range(0, len(groups)):
        answer = client.delete_db_subnet_group(
            DBSubnetGroupName = groups[j]
        )


