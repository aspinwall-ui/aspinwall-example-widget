# coding: utf-8
"""
Example widget template.
"""
from aspinwall.widgets import Widget
from gi.repository import Gtk
translatable = lambda message: message

class MyWidget(Widget):
    metadata = {
        "name": translatable("CHANGEME"),
        "icon": 'preferences-syste,-symbolic',
        "description": translatable("CHANGEME"),
        "id": "org.dithernet.aspinwall.widgets.example",
        "tags": translatable('CHANGEME')
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
