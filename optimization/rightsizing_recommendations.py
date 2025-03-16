import boto3

# Initialize AWS Compute Optimizer client
optimizer = boto3.client("compute-optimizer")

# Get EC2 rightsizing recommendations
recommendations = optimizer.get_ec2_instance_recommendations()

# Process recommendations
for rec in recommendations["instanceRecommendations"]:
    print(f"Instance: {rec['instanceArn']} - Recommended Action: {rec['recommendationOptions'][0]['instanceType']}")

print("✅ Automated Rightsizing Recommendations script executed successfully.")
