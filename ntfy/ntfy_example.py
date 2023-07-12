"""
ntfy.sh is a notification service.
In essense we can send a post or put request to an endpoint,
and it will push notifications to your device that subscribes to that endpoint
"""
import requests


# The topic has to be globally unique from other users as well.
topic = '01134theregeneralkenobi'
message = 'what up, testing from python'
arguments = {
    "url": f"https://ntfy.sh/{topic}",
    "headers": {
        "Title": "Oh no a notification",
        "Priority": "default",  # urgent, high, default, low, min
        "Tags": "warning"
    },
    "data": message.encode(encoding='utf-8')
}
requests.post(**arguments)

def push_notification(url:str, message:str, title:str=None, priority:str=None, tags:str=None):
    arguments = {
        "url": url,
        "data": message.encode(encoding='utf-8')
    }
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


push_notification(
    url=f"https://ntfy.sh/{topic}",
    message="2nd test of notification",
    title='nothing much',
    tags='warning'
)


class NtfyConnector:
    def __init__(self, topic):
        self.topic = topic
        self.url = f"https://ntfy.sh/{topic}"
    
    def push_notification(self, message:str, title:str=None, priority:str=None, tags:str=None):
        arguments = {
            "url": self.url,
            "data": message.encode(encoding='utf-8')
        }
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
