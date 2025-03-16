import boto3

client = boto3.client("ce")

# Fetch rightsizing recommendations
response = client.get_rightsizing_recommendation(
    Service="AmazonEC2"
)

# Save recommendations
with open("output/rightsizing_recommendations.json", "w") as f:
    f.write(str(response))

print("✅ Rightsizing Recommendations Generated. Results saved to output/rightsizing_recommendations.json.")
