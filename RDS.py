import boto3
import time
def deleterds():
    client = boto3.client('rds')
    dbinstance = []
    cluster = []
    response = client.describe_db_instances()
    clusters = client.describe_db_clusters()
    for i in response['DBInstances']:
        dbinstance.append(i['DBInstanceIdentifier'])
    for j in clusters['DBClusters']:
        cluster.append(j['DBClusterIdentifier'])
    # for j in dbinstance:
    #     modify = response = client.modify_db_instance(
    #         DBInstanceIdentifier=j,
    #         DeletionProtection=False
    #     )
    for k in cluster:
        if k != True:
            client.modify_db_cluster(
                DBClusterIdentifier=k,
                DeletionProtection=False
            )
        else :
            for l in dbinstance:
                client.modify_db_instance(
                DBInstanceIdentifier=l,
                DeletionProtection=False
            )
    try:
        for m in dbinstance:
            client.delete_db_instance(
                DBInstanceIdentifier=m,
                SkipFinalSnapshot=True,
                DeleteAutomatedBackups=True
            )
    except :
        for l in dbinstance:
                client.modify_db_instance(
                DBInstanceIdentifier=l,
                DeletionProtection=False
            )
        for m in dbinstance:
            client.delete_db_instance(
                DBInstanceIdentifier=m,
                SkipFinalSnapshot=True,
                DeleteAutomatedBackups=True
            )


    for n in cluster:
        client.delete_db_cluster(
        DBClusterIdentifier=n,
        SkipFinalSnapshot=True
    )