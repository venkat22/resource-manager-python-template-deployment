import os.path
from deployer import Deployer


# This script expects that the following environment vars are set:
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret

my_subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID', '11111111-1111-1111-1111-111111111111')   # your Azure Subscription Id
           # the resource group for deployment

msg = "\nInitializing the Deployer class with subscription id: {}" \
    "\n\n"
msg = msg.format(my_subscription_id)
print(msg)

# Initialize the deployer class
deployer = Deployer(my_subscription_id)

print("Beginning the deployment... \n\n")
# Deploy the template
deployer.createRG("MyResourceGroup")
my_deployment = deployer.deploy('subnets.json')

print("Done deploying!!")

