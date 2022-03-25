project('org.dithernet.aspinwall.widgets.example',
          version: '0.1.0',
    meson_version: '>= 0.50.0',
  default_options: [ 'warning_level=2',
                   ],
)
#'org.dithernet.aspinwall.widgets.example'
i18n = import('i18n')

widget_dir = join_paths(get_option('prefix'), get_option('datadir'), 'aspinwall', 'widgets', meson.project_name())
widget_sources = [
	'widget.py'
]
install_data(widget_sources, install_dir: widget_dir)

subdir('po')
subdir('schemas') # Remove this and the schemas directory if you're not planning to use schemas
