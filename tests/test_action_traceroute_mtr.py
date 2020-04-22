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

from networking_utils_base_test_case import NetworkingUtilsBaseActionTestCase

from traceroute_mtr import TracerouteMTR

__all__ = [
    'TracerouteMTRTestCase'
]


class TracerouteMTRTestCase(NetworkingUtilsBaseActionTestCase):
    __test__ = True
    action_cls = TracerouteMTR

    def test_traceroute_mtr_localhost(self):
        action = self.get_action_instance()

        result = action.run("127.0.0.1")

        self.assertTrue(len(result["report"]["hubs"]) > 0)
