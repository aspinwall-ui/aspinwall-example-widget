widget_schemas_dir = join_paths(widget_dir, 'schemas')

gnome = import('gnome')

compile_schemas = find_program('glib-compile-schemas', required: true)
run_command(compile_schemas, '.', check: true)

install_data(
  [meson.project_name() + '.gschema.xml', 'gschemas.compiled',],
  install_dir: widget_schemas_dir
)
