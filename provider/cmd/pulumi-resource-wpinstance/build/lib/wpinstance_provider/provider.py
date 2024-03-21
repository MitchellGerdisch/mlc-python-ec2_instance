#  Copyright 2016-2021, Pulumi Corporation.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Optional

from pulumi import Inputs, ResourceOptions
from pulumi.provider import ConstructResult
import pulumi.provider as provider

import wpinstance_provider
from wpinstance_provider.wpinstance import WpInstanceArgs, WpInstance


class Provider(provider.Provider):

    def __init__(self) -> None:
        super().__init__(wpinstance_provider.__version__, wpinstance_provider.__schema__)

    def construct(self,
                  name: str,
                  resource_type: str,
                  inputs: Inputs,
                  options: Optional[ResourceOptions] = None) -> ConstructResult:

        if resource_type == 'wpinstance:mlc:WpInstance':
            return _deploy_wpinstance(name, inputs, options)

        raise Exception(f'Unknown resource type {resource_type}')


def _deploy_wpinstance(name: str,
                           inputs: Inputs,
                           options: Optional[ResourceOptions] = None) -> ConstructResult:

    # Create the component resource.
    wpinstance = WpInstance(name, WpInstanceArgs.from_inputs(inputs), dict(inputs), options)

    # Return the component resource's URN and outputs as its state.
    return provider.ConstructResult(
        urn=wpinstance.urn,
        state={
            'wpinstanceIp': wpinstance.wpinstance_ip,
            'secruleId': wpinstance.secrule_id,
        })
