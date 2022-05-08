import RM
from ulauncher.api.client.EventListener import EventListener


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):

        data = event.get_data()
        extension.logger.debug(str(data))

        if data["action"] == "remove":
            package = data["package"]
            RM.remove(package)
            return extension.render_main_page(None)
