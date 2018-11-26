import boto3
ec2=boto3.resource('ec2')
ec2.instances.filter(Filters=[{'Name': 'availability-zone','Values': ['us-east-id']}]).stop()