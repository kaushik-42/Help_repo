from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient
from datetime import datetime, timedelta

# Set up Azure credentials
credential = DefaultAzureCredential()

# Define subscription ID (replace with your actual subscription ID)
subscription_id = 'your-subscription-id'

# Initialize the client
client = CostManagementClient(credential)

# Define time period (e.g., for the last 30 days)
time_period = {
    "timeframe": "Custom",
    "time_period": {
        "from": (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d"),
        "to": datetime.today().strftime("%Y-%m-%d")
    }
}

# Request cost analysis
response = client.query.usage(
    scope=f"/subscriptions/{subscription_id}",
    parameters={
        "type": "Usage",
        "timeframe": "Custom",
        "time_period": time_period,
        "dataset": {
            "granularity": "Daily",
            "aggregation": {
                "totalCost": {"name": "PreTaxCost", "function": "Sum"}
            },
            "grouping": [{"type": "Dimension", "name": "ResourceId"}]
        }
    }
)

# Print the results
for row in response['rows']:
    print(f"Resource: {row[0]}, Cost: {row[1]}")
