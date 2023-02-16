#!/usr/bin/env python3

import hashlib
import glob
import os
import shutil
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path as P

PARSER = ArgumentParser()
PARSER.add_argument('--build-dir', type=P)
PARSER.add_argument('--source-dir', type=P)
PARSER.add_argument('--root-dir', type=P)
PARSER.add_argument('--build-type', choices=['release', 'debug'])
PARSER.add_argument('--extra-env-vars', nargs='*', default=[])
PARSER.add_argument('--buildtype')
PARSER.add_argument('--project-name')
PARSER.add_argument('--exe-suffix')

if __name__ == "__main__":
    opts = PARSER.parse_args()

    logfile = open(opts.root_dir / 'meson-logs' / f'{opts.project_name}-cargo-wrapper.log', mode='w', buffering=1)

    print(opts, file=logfile)
    cargo_target_dir = opts.root_dir / 'target'

    env = os.environ.copy()
    env['INCLUDE_DIR'] = str(f'{opts.build_dir}{os.sep}')
    env['CARGO_TARGET_DIR'] = str(cargo_target_dir)

    pkg_config_path = env.get('PKG_CONFIG_PATH', '').split(':')
    pkg_config_path.append(str(opts.root_dir / 'meson-uninstalled'))
    env['PKG_CONFIG_PATH'] = ':'.join(pkg_config_path)

    env['CARGO_HOME'] = str(opts.root_dir / 'cargo-home')

    for e in opts.extra_env_vars:
        k, v = e.split(':')
        env[k] = v

    if  opts.buildtype == 'cross':
        env['PKG_CONFIG_ALLOW_CROSS'] = '1'

    cargo_cmd = ['cargo', 'build']
    if opts.build_type == 'release':
        cargo_cmd.append('--release')

    cargo_cmd.extend(['--manifest-path', opts.source_dir / 'Cargo.toml'])

    def run(cargo_cmd, env):
        try:
            subprocess.run(cargo_cmd, env=env, check=True)
        except subprocess.SubprocessError:
            sys.exit(1)

    run(cargo_cmd, env)

    target_dir = cargo_target_dir / '**' / opts.build_type

    # Copy so files to build dir
    for f in glob.glob(str(target_dir / opts.project_name) + opts.exe_suffix, recursive=True):
        libfile = P(f)
        shutil.copy(f, opts.build_dir)
        os.remove(f)