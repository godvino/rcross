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

target = 'release'
if get_option('debug')
  target = 'debug'
endif

cargo_wrapper = find_program(join_paths(meson.project_source_root(),'build-aux/cargo_wrapper.py'))


devenv = environment()
devenv.set('CARGO_HOME', meson.global_build_root() / 'cargo-home')
devenv.set('CARGO_TARGET_DIR', meson.global_build_root() / 'target')
devenv.set('CONFIG_IN', meson.current_build_dir() / 'config.rs')
devenv.set('GRESOURCE_IN', meson.current_build_dir() / 'rcross.gresource')
devenv.append('PKG_CONFIG_PATH', meson.global_build_root() / 'meson-uninstalled')
if meson.is_cross_build()
  devenv.set('PKG_CONFIG_ALLOW_CROSS', '1')
endif

meson.add_devenv(devenv)

rcross = custom_target(
  build_by_default: true,
  build_always_stale: true,
  output: meson.project_name() + exe_suffix,
  console: true,
  install: true,
  install_dir: get_option('bindir'),
  install_tag: 'runtime',
  env: devenv,
  command: [cargo_wrapper,
  '--build-dir', meson.current_build_dir(),
  '--source-dir', meson.project_source_root(),
  '--root-dir', meson.global_build_root(),
  '--build-type', target,
  '--project-name', meson.project_name(),
  '--exe-suffix', exe_suffix
  ])