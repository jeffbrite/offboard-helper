from cement.core.interface import Interface
from cement.core.handler import Handler

class GYBInterface(Interface):
    class Meta:
        interface = 'gyb'
    
    def actions(self, action=None, email=None, **kwargs):
        # Valid Actions: backup,backup-chat,restore,restore-group,restore-mbox,count,purge,purge-labels,print-labels,estimate,quota,reindex,revoke,split-mbox,create-project,delete-projects,check-service-account,create-label
        pass
    
    def check_service_account(self, email, config_folder=None):
        pass
    
    def estimat(self, email, config_folder=None, memory_limit=None, local_folder=None):
        pass
    
    def backup(self, email, config_folder=None, memory_limit=None, local_folder=None):
        pass

    def restore(self, email, config_folder=None, memory_limit=None, local_folder=None):
        pass
    
    def restore_group(self, email, config_folder=None, memory_limit=None, local_folder=None):
        pass

class GYBHandler(GYBInterface, Handler):

    """
    GYB handler implementation.

    """

    pass  # pragma: nocover