if host_machine.system() not in ['windows', 'darwin']

desktop_file = i18n.merge_file(
  input: 'org.gnome.Example.desktop.in',
  output: 'org.gnome.Example.desktop',
  type: 'desktop',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)

desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils,
    args: [desktop_file]
  )
endif

appstream_file = i18n.merge_file(
  input: 'org.gnome.Example.appdata.xml.in',
  output: 'org.gnome.Example.appdata.xml',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'appdata')
)

appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', appstream_file]
  )
endif

endif

install_data('org.gnome.Example.gschema.xml',
  install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas'),
  install_tag: 'runtime'
)

gnome.compile_schemas(build_by_default: true)


subdir('icons')
