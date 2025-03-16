import boto3

ec2 = boto3.client("ec2")

# Request Spot Instances
response = ec2.request_spot_instances(
    InstanceCount=1,
    Type="one-time",
    LaunchSpecification={
        "ImageId": "ami-12345678",
        "InstanceType": "t3.medium"
    }
)

# Print request details
print("✅ Spot Instance Requested:", response)
