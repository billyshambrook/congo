""" """
from cached_property import cached_property
import consul


class CongoClient(object):

    """ """

    def __init__(self, host):
        """
        Initialise the class.

        Args:
            host (str): The host that the client will speak to.
        """
        self._host = host

    def register(self, name):
        """
        Register itself as a service.

        Args:
            name (str): Service name.
        """
        return self._client.api.agent.register(name)

    def get(self, path):
        """
        Get path from k/v.

        Args:
            path (str): The key to get.
        """
        return self._client.api.kv.get(path)

    @property
    def host(self):
        """ The host that the client will speak to. """
        return self._host

    @cached_property
    def api(self):
        """ Consul API python library instance. """
        return consul.Consul(self.host)
