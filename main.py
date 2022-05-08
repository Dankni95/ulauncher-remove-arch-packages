import RM
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from KeywordQueryEventListener import KeywordQueryEventListener
from ItemEnterEventListener import ItemEnterEventListener
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem


class RemovePackageMain(Extension):
    def __init__(self):
        super(RemovePackageMain, self).__init__()
        self.logger.info("Inializing Extension")
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

    def render_main_page(self, action):

        repos = self.preferences["repo"]
        packageNames = RM.list(repos)

        items = []

        for package in packageNames:
            items.append(
                ExtensionSmallResultItem(
                    icon="images/remove.png",
                    name=package,
                    description="Skip current song and go to the next song",
                    on_enter=ExtensionCustomAction(
                        {"action": "remove", "package": package}, keep_app_open=True
                    ),
                )
            )

        return RenderResultListAction(items)


if __name__ == "__main__":
    RemovePackageMain().run()
