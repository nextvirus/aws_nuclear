import boto3

def ecs_cluster():
    cluster = []
    service = []
    client = boto3.client('ecs')
    response = client.list_clusters()
    for i in range(0, len(response['clusterArns'])):
        if len(response['clusterArns']) == 0:
            break
        else:
            cluster.append(response['clusterArns'][i])
    
    for j in range(0, len(cluster)):
        question = client.list_services(
             cluster = cluster[j]
        )
        if len(question['serviceArns'][j])==0:
            break
        else:
            service.append(question['serviceArns'][j])
    
    for a in range(0, len(service)):
        if len(service) == 0:
            break
        else:
            client.delete_service(
                cluster = cluster[a],
                service = service[a],
                force = True
            )

    for b in range(0, len(cluster)):
        if len(cluster) == 0:
            break
        else:
            client.delete_cluster(
                cluster = cluster[b]
            )

