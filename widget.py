# coding: utf-8
"""
Example widget template.
"""
from aspinwall.widgets import Widget
from gi.repository import Gtk, Adw
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

        example_label = Gtk.Label(
            label=_('Replace me with the widget content!')
        )

        self.content.append(example_label)

_widget_class = MyWidget
