import boto3

def CDN():
    client = boto3.client('cloudfront')
    CDN = []
    response = client.list_distributions()
    for i in range(0,len(response['DistributionList']['Items'])):
        CDN.append(response['DistributionList']['Items'][i]['Id'])

    for j in range(0, len(CDN)):
        answer = client.delete_distribution(
            Id = CDN[j]
        )

CDN()