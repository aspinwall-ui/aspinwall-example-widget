# Example Aspinwall widget

This is a simple example project, which can be used as a template/skeleton for creating new widgets.

For more information, see [Creating a new widget](https://github.com/aspinwall-ui/aspinwall/blob/develop/docs/widgets/creating_widgets.md).

## Using this template

> Note: GitHub users can specify this repository as the template for a new repository by clicking the "Use this template" button.

- Replace the widget ID in the `meson.build` file with the ID of your widget.
- Change the metadata in the `widget.py` file to match your widget's metadata.
- Change the widget class name, and update the `_widget_class` variable at the bottom of the file.
- If you're planning to use settings schemas, rename the `.xml` file in the `schemas` directory to match your widget's ID and edit it to set the schema ID to your widget's ID.
  * If you're not planning to use settings schemas, remove the `schemas` folder and remove the `subdir('schemas')` line from the `meson.build` in the project's root.
- Remove the example-specific .pot file from the `po` directory and regenerate the po/translation files by following the steps in the `Generating translation files` section.

## Building and installing the widget

```shell
meson --prefix="/usr" . output
meson compile -C output
sudo meson install -C output
```

Or, if you want to install the widget for the current user:

```shell
meson --prefix="$HOME/.local" . output
meson compile -C output
meson install -C output
```

## Generating translation files

**NOTE**: The following is automated by the `po/update-po` script. **Make sure to edit it to change the widget ID before using it.**

To generate the .pot file (this only needs to be done once, or whenever the widget ID changes):

```shell
meson . output
meson compile <widget id>-pot -C output
```

To update the translations:

```shell
meson . output
meson compile <widget id>-update-po -C output
```

Replace `<widget id>` with your widget's ID (without the brackets).
