project('rcross', 'c', 
          version: '0.1.0',
    meson_version: '>= 0.60.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

exe_suffix = ''
if host_machine.system() == 'windows'
  exe_suffix = '.exe'
endif

i18n = import('i18n')
gnome = import('gnome')

cargo = find_program('cargo', version:'>=1.40')
rustc = find_program('rustc', version:'>=1.52')

gtk_dep = dependency('gtk4')
adwaitaa_dep = dependency('libadwaita-1')

subdir('data')
subdir('src')
subdir('po')

gnome.post_install(
     glib_compile_schemas: true,
     gtk_update_icon_cache: true,
    update_desktop_database: host_machine.system() not in ['darwin', 'windows'],
)
