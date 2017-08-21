# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
import logging
import os
import sys
import pkgutil

import click
import json

LOG = logging.getLogger(__name__)

CMD_FOLDER = 'commands'
plugin_folder = os.path.join(os.path.dirname(__file__), CMD_FOLDER)

VALID_OUTPUT_FORMATS = ['json', 'yaml']


class Context(object):

    def __init__(self):
        self.home = os.getcwd()

    def log(sel, msg, *args):
        self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)


class NautilusCLI(click.MultiCommand):

    @property
    def command_folder(self):
        return os.path.abspath(os.path.join(
            os.path.dirname(__file__), CMD_FOLDER))

    def list_commands(self, ctx):
        rv = list()
        for _, pkg_name, _ in pkgutil.iter_modules([self.command_folder]):
            rv.append(pkg_name)
        else:
            return sorted(rv)

    def get_command(self, ctx, name):
        for _, pkg_name, _ in pkgutil.iter_modules([self.command_folder]):
            if pkg_name == name:
                mod = importlib.import_module(
                    'nautilusclient.commands.{}'.format(name)
                )
                return getattr(mod, 'cli')
        else:
            raise SystemExit('Command module "{}" not found.'.format(name))


@click.command(cls=NautilusCLI)
@pass_context
def cli(*args, **kwargs):
    """Command-Line Interface main class"""
    try:
        args[0].verbose = kwargs.get('verbose', False)
    except IndexError:
        pass


if __name__ == '__main__':
    cli()
