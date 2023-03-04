# coding: utf-8
"""
Example widget template.
"""
from aspinwall_launcher.widgets import Widget
from gi.repository import Gtk
translatable = lambda message: message

class MyWidget(Widget):
    metadata = {
        "id": "org.dithernet.aspinwall.widgets.example",
        "version": '0.1.0',
        "name": translatable("Example widget"),
        "author": "Your name here",
        "icon": "preferences-system-symbolic",
        "description": translatable("Widget template used as a base for development"),
        "tags": translatable("tag1,tag2,tag3"),

        # Optional metadata
        "url": "https://github.com/CHANGEME/CHANGEME",
        "issue_tracker": "https://github.com/CHANGEME/CHANGEME/issues"
    }

    def __init__(self, instance=0):
        super().__init__(instance)
        _ = self.l

        self.content = Gtk.Box(hexpand=True, orientation=Gtk.Orientation.VERTICAL)

        example_label = Gtk.Label(
            label=_('Replace me with the widget content!')
        )

        self.content.append(example_label)

        self.set_child(self.content)

_widget_class = MyWidget
