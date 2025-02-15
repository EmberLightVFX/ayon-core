# -*- coding: utf-8 -*-
"""Collect default Deadline server."""
import pyblish.api


class CollectDefaultDeadlineServer(pyblish.api.ContextPlugin):
    """Collect default Deadline Webservice URL.

    DL webservice addresses must be configured first in System Settings for
    project settings enum to work.

    Default webservice could be overriden by
    `project_settings/deadline/deadline_servers`. Currently only single url
    is expected.

    This url could be overriden by some hosts directly on instances with
    `CollectDeadlineServerFromInstance`.
    """

    # Run before collect_deadline_server_instance.
    order = pyblish.api.CollectorOrder + 0.0025
    label = "Default Deadline Webservice"

    pass_mongo_url = False

    def process(self, context):
        try:
            deadline_module = context.data["ayonAddonsManager"]["deadline"]
        except AttributeError:
            self.log.error("Cannot get AYON Deadline addon.")
            raise AssertionError("AYON Deadline addon not found.")

        deadline_settings = context.data["project_settings"]["deadline"]
        deadline_server_name = deadline_settings["deadline_server"]

        deadline_webservice = None
        if deadline_server_name:
            deadline_webservice = deadline_module.deadline_urls.get(
                deadline_server_name)

        default_deadline_webservice = deadline_module.deadline_urls["default"]
        deadline_webservice = (
            deadline_webservice
            or default_deadline_webservice
        )

        context.data["defaultDeadline"] = deadline_webservice.strip().rstrip("/")  # noqa
