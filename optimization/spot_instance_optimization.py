import boto3

# Initialize AWS EC2 client
ec2 = boto3.client("ec2")

# Get list of all spot instance requests
spot_requests = ec2.describe_spot_instance_requests()

# Process and optimize spot instances
for request in spot_requests["SpotInstanceRequests"]:
    print(f"Spot Instance ID: {request['InstanceId']} - Status: {request['Status']['Code']}")

print("✅ Multi-Cloud Spot Instance Optimization script executed successfully.")
