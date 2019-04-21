import os.path
from deployer import Deployer
# This script expects that the following environment vars are set:
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret
# AZURE_SUBSCRIPTION_ID: with your target subscription ID

my_subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID', '11111111-1111-1111-1111-111111111111')   # your Azure Subscription Id
msg = "\nInitializing the Deployer class with subscription id: {}\n\n"
msg = msg.format(my_subscription_id)
print(msg)

# Initialize the deployer class
deployer = Deployer(my_subscription_id)

print("Beginning the deployment... \n\n")
# Deploy the template
#deployer.createResourceGroup("MyResourceGroup")
deployer.resource_group="MyResourceGroup"
my_deployment = deployer.deployAtResourceGroupScope("vnets.json")
my_deployment = deployer.deployAtSubscriptionScope('resourcegroups.json')

print("Done deploying!!")

