from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
import RM
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):

        args = event.get_argument()

        repos = extension.preferences["repo"]
        packageNames = RM.list(repos)
        items = []

        if args is not None:
            try:
                args = int(args)
            except ValueError:
                pass

            if isinstance(args, int) and args is not None:

                packageAfter = packageNames[args - 1 :]
                for package in packageAfter:

                    items.append(
                        ExtensionSmallResultItem(
                            icon="images/remove.png",
                            name=package,
                            on_enter=ExtensionCustomAction(
                                {"action": "remove", "package": package},
                                keep_app_open=True,
                            ),
                        )
                    )

                return RenderResultListAction(items)

            else:
                for package in packageNames:
                    if (
                        package.lower().startswith(args.lower())
                        or args.lower() in package.lower()
                    ):
                        items.append(
                            ExtensionSmallResultItem(
                                icon="images/remove.png",
                                name=package,
                                on_enter=ExtensionCustomAction(
                                    {"action": "remove", "package": package},
                                    keep_app_open=True,
                                ),
                            )
                        )

                return RenderResultListAction(items)

        return extension.render_main_page(None)
