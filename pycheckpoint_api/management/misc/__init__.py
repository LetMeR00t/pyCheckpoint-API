from restfly.endpoint import APIEndpoint

from .generic_objects import GenericObjects


class MISC(APIEndpoint):
    @property
    def generic_objects(self) -> GenericObjects:
        """The interface object for the objects type "Generic Objects" Management.
        This is not referenced within the official Checkpoint API documentation

        Returns:
            GenericObjects: a Generic Objects instance

        Examples:
            >>> firewall.misc.generic_objects

        """
        return GenericObjects(self)
