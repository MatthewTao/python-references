"""
ntfy.sh is a notification service.
In essense we can send a post or put request to an endpoint,
and it will push notifications to your device that subscribes to that endpoint
"""

import requests
import urllib.request
import urllib.parse


def push_notification(
    url: str, message: str, title: str = None, priority: str = None, tags: str = None
):
    arguments = {"url": url, "data": message.encode(encoding="utf-8")}
    if title or priority or tags:
        # Create the header if this exists
        header = {}
        if title:
            header.update({"Title": title})
        if priority:
            header.update({"Priority": priority})
        if tags:
            header.update({"Tags": tags})

        arguments.update({"headers": header})

    requests.post(**arguments)


class NtfyConnector:
    def __init__(self, topic):
        self.topic = topic
        self.url = f"https://ntfy.sh/{topic}"

    def push_notification(
        self, message: str, title: str = None, priority: str = None, tags: str = None
    ):
        arguments = {"url": self.url, "data": message.encode(encoding="utf-8")}
        if title or priority or tags:
            # Create the header if these exists
            header = {}
            if title:
                header.update({"Title": title})
            if priority:
                header.update({"Priority": priority})
            if tags:
                header.update({"Tags": tags})

            arguments.update({"headers": header})

        requests.post(**arguments)


class NtfyConnectorStd:
    """
    Only uses standard lib
    Sometimes it's just nice to not have any other dependency
    """

    def __init__(self, topic):
        self.topic = topic
        self.url = f"https://ntfy.sh/{topic}"

    def push_notification(
        self, message: str, title: str = "", priority: str = "", tags: str = ""
    ):
        arguments = {
            "url": self.url,
            "data": message.encode(encoding="utf-8"),
            "method": "POST",
        }
        request = urllib.request.Request(**arguments)

        if title or priority or tags:
            # Create the header if these exists
            header = {}
            if title:
                request.add_header("Title", title)
            if priority:
                request.add_header("Priority", priority)
            if tags:
                request.add_header("Tags", tags)

        with urllib.request.urlopen(request) as response:
            # Read the response data
            response_data = response.read()
            print(response_data.decode("utf-8"))


if __name__ == "__main__":
    # The topic has to be globally unique from other users as well.
    topic = "01134theregeneralkenobi"
    print(f"https://ntfy.sh/{topic}")
    message = "what up, testing from python"

    ntfy = NtfyConnectorStd(topic=topic)
    ntfy.push_notification(message=message, title="Testing_title", tags="testing_tag")
