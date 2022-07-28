from box import Box
from restfly.endpoint import APIEndpoint


class GenericObjects(APIEndpoint):
    def get_rulebaseactions(
        self,
    ) -> Box:
        """This method is used to recover generic objects named rule base actions from Checkpoint API

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewall.misc.generic_objects.get_rulebaseactions()

        """
        # Main request parameters
        payload = {"class-name": "com.checkpoint.objects.rulebase.RulebaseAction"}

        return self._post("show-generic-objects", json=payload)
