from __future__ import absolute_import
from .lib import format_query_params


class Automations(object):
    # Automations base API uri
    base_api_url = "api/automations"

    def __init__(self, api_client):
        """
        Class constructor

        :param api_client: object
        """
        self.api_client = api_client

    def list(self, **kwargs):
        """
        Lists all automations on account
        Ref: https://developers.mailerlite.com/docs/automations.html#list-all-automations

        :param **kwargs: You can pass additional arguments - page, limit or to filter by status, name and group
        :return: JSON array
        :rtype: dict
        """

        available_params = ["filter", "page", "limit"]
        query_params = format_query_params(available_params, **kwargs)

        print(query_params)
        return self.api_client.request("GET", self.base_api_url, query_params).json()

    def get(self, automation_id):
        """
        Returns information about single automation
        Ref: https://developers.mailerlite.com/docs/automations.html#get-an-automation

        :param: automation_id: Automation ID
        :return: JSON dict
        """

        return self.api_client.request(
            "GET", f"{self.base_api_url}/{automation_id}"
        ).json()

    def activity(self, automation_id, **kwargs):
        """
        Get the subscriber activity for an automation
        Ref: https://developers.mailerlite.com/docs/automations.html#get-the-subscriber-activity-for-an-automation

        :param: automation_id: Automation ID
        :param: kwargs: You can pass additional arguments - page, limit or to filter by status, date_from, date_to
        :raises: :class: `TypeError` : Got an unknown argument
        :return: JSON dict
        """

        available_params = ["filter", "page", "limit"]
        query_params = format_query_params(available_params, **kwargs)

        return self.api_client.request(
            "GET",
            f"{self.base_api_url}/{automation_id}/activity",
            query_params,
        ).json()
