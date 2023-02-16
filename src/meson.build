pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
gnome = import('gnome')

gresource = gnome.compile_resources('rcross',
  'rcross.gresource.xml',
  gresource_bundle: true,
)

conf = configuration_data()
conf.set_quoted('VERSION', meson.project_version())
conf.set_quoted('GETTEXT_PACKAGE', 'rcross')
conf.set_quoted('LOCALEDIR', join_paths(get_option('prefix'), get_option('localedir')))
conf.set_quoted('PKGDATADIR', pkgdatadir)

configure_file(
    input: 'config.rs.in',
    output: 'config.rs',
    configuration: conf
)

buildtype = 'native'
if meson.is_cross_build()
  buildtype = 'cross'
endif

if get_option('debug')
  target = 'debug'
else
  target = 'release'
endif

cargo_wrapper = find_program(join_paths(meson.project_source_root(),'build-aux/cargo_wrapper.py'))

rcross = custom_target(
  build_by_default: true,
  build_always_stale: true,
  output: meson.project_name() + exe_suffix,
  console: true,
  install: true,
  install_dir: get_option('bindir'),
  install_tag: 'runtime',
#  depends: gio_dep,
  command: [cargo_wrapper,
  '--build-dir', meson.current_build_dir(),
  '--source-dir', meson.project_source_root(),
  '--root-dir', meson.global_build_root(),
  '--build-type', target,
  '--buildtype', buildtype,
  '--project-name', meson.project_name(),
  '--exe-suffix', exe_suffix
  ])

