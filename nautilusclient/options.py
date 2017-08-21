# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click
import functools


def os_params(func):
    @click.option('--os-identity-api-version',
                  help='Identity API Version',
                  envvar='OS_IDENTITY_API_VERSION')
    @click.option('--os-auth-url',
                  help='Authentication URL with password',
                  envvar='OS_AUTH_URL')
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
