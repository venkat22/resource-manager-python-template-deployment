"""A deployer class to deploy a template on Azure"""
import os.path
import json
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.resource.resources.models import DeploymentMode


class Deployer(object):
    """ Initialize the deployer class with subscription, resource group and public key.

    :raises IOError: If the public key path cannot be read (access or not exists)
    :raises KeyError: If AZURE_CLIENT_ID, AZURE_CLIENT_SECRET or AZURE_TENANT_ID env
        variables or not defined
    """

    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.credentials = ServicePrincipalCredentials(
            client_id=os.environ['AZURE_CLIENT_ID'],
            secret=os.environ['AZURE_CLIENT_SECRET'],
            tenant=os.environ['AZURE_TENANT_ID']
        )
        self.client = ResourceManagementClient(self.credentials, self.subscription_id)
        self.subclient = SubscriptionClient(self.credentials)

    def deployAtResourceGroupScope(self, template):
        """Deploy the template to a resource group."""
        template_path = os.path.join(os.path.dirname(__file__), 'templates', template)
        with open(template_path, 'r') as template_file_fd:
            template = json.load(template_file_fd)

        parameters = {
        }
        parameters = {k: {'value': v} for k, v in parameters.items()}

        deployment_properties = {
            'mode': DeploymentMode.complete,
            'template': template,
            'parameters': parameters
        }


        deployment_async_operation = self.client.deployments.create_or_update(
            self.resource_group,
            'azure-sample',
            deployment_properties
        )
        deployment_async_operation.wait()





    def deployAtSubscriptionScope(self, template):
        template_path = os.path.join(os.path.dirname(__file__), 'templates', template)
        with open(template_path, 'r') as template_file_fd:
            template = json.load(template_file_fd)
        parameters = {
        }
        parameters = {k: {'value': v} for k, v in parameters.items()}
        deployment_properties = {
            'mode': DeploymentMode.incremental,
            'template': template

        }
        self.client.deployments.create_or_update_at_subscription_scope(
            'azuresample',
            deployment_properties,
            location="eastus"
        )


    def destroy(self):
        """Destroy the given resource group"""
        self.client.resource_groups.delete(self.resource_group)
