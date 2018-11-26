import boto3
ec2=boto3.resource('ec2')
for instance in in ec2.instances.all():
    print (instance)

for instance in  ec2.instances.filter(Filters=[{'Name': 'availability-zone','Values': ['us-east-id']}]):
    print (instance.instance_id, instance.instance_type)