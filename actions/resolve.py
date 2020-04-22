# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket
from st2common.runners.base_action import Action


class Resolve(Action):
    def run(self, request, reverse=False):
        """
        Check if item is in container
        :param request: DNS to request
        :param reverse: Should we request the reverse
        :return: List[str]
        """

        if reverse:
            return [socket.gethostbyaddr(request)[0]]
        else:
            return socket.gethostbyname_ex(request)[2]




