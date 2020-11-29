import boto3

def ecr():
    repository = []
    client = boto3.client('ecr')
    response = client.describe_repositories()
    for i in range(0, len(response['repositories'])):
        repository.append(response['repositories'][i]['repositoryName'])
    for j in range(0, len(repository)):
        answer = client.delete_repository(
            repositoryName = repository[j],
            force = True
        )

ecr()
    

