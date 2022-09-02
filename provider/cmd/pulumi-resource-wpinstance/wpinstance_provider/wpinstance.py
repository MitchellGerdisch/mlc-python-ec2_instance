# Copyright 2016-2021, Pulumi Corporation.
#
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

import json
from typing import Optional

from pulumi import Inputs, ResourceOptions
from pulumi_aws import ec2
import pulumi

class WpInstanceArgs:

    public_key: pulumi.Input[str]
    """The public key for accessing the instance."""
    instance_type: pulumi.Input[str]
    """The instance size."""
    vpc_id: pulumi.Input[str]
    """The VPC ID in which to deploy the instance."""
    subnet_id: pulumi.Input[str]
    """The Subnet ID in which to deploy the instance."""

    @staticmethod
    def from_inputs(inputs: Inputs) -> 'WpInstanceArgs':
        return WpInstanceArgs(
            instance_type=inputs['instanceType'],
            public_key=inputs['publicKey'],
            vpc_id=inputs['vpcId'],
            subnet_id=inputs['subnetId']
        )

    def __init__(self,
                 # name the arguments and their types (e.g. str, bool, etc)
                 public_key: str,
                 instance_type: str,
                 vpc_id: pulumi.Input[str],
                 subnet_id: pulumi.Input[str]) -> None:

        # Set the class args
        self.public_key = public_key
        self.instance_type = instance_type
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id

class WpInstance(pulumi.ComponentResource):
    wpinstance_ip: pulumi.Output[str]
    secrule_id: pulumi.Output[str]

    def __init__(self,
                 name: str,
                 args: WpInstanceArgs, 
                 props: Optional[dict] = None,
                 opts: Optional[ResourceOptions] = None) -> None:

        super().__init__('wpinstance:mlc:WpInstance', name, props, opts)

        public_key = args.public_key
        instance_type = args.instance_type
        vpc_id = args.vpc_id
        subnet_id = args.subnet_id

        # Dynamically query for the Amazon Linux 2 AMI in this region.
        aws_linux_ami = ec2.get_ami(owners=["amazon"],
            filters=[ec2.GetAmiFilterArgs(
                name="name",
                values=["amzn2-ami-hvm-*-x86_64-ebs"],
            )],
            most_recent=True)

        # Security group for EC2:
        ec2_allow_rule = ec2.SecurityGroup("ec2-allow-rule",
            vpc_id=vpc_id,
            ingress=[
                ec2.SecurityGroupIngressArgs(
                    description="HTTPS",
                    from_port=443,
                    to_port=443,
                    protocol="tcp",
                    cidr_blocks=["0.0.0.0/0"],
                ),
                ec2.SecurityGroupIngressArgs(
                    description="HTTP",
                    from_port=80,
                    to_port=80,
                    protocol="tcp",
                    cidr_blocks=["0.0.0.0/0"],
                ),
                ec2.SecurityGroupIngressArgs(
                    description="SSH",
                    from_port=22,
                    to_port=22,
                    protocol="tcp",
                    cidr_blocks=["0.0.0.0/0"],
                ),
            ],
            egress=[ec2.SecurityGroupEgressArgs(
                from_port=0,
                to_port=0,
                protocol="-1",
                cidr_blocks=["0.0.0.0/0"],
            )],
            tags={
                "Name": "allow ssh,http,https",
            })

        # Create a keypair to access the EC2 instance:
        wordpress_keypair = ec2.KeyPair("wordpress-keypair", public_key=public_key)

        # Create an EC2 instance to run Wordpress (after RDS is ready).
        wordpress_instance = ec2.Instance("wordpress-instance",
            ami=aws_linux_ami.id,
            instance_type=instance_type,
            subnet_id=subnet_id,
            vpc_security_group_ids=[ec2_allow_rule.id],
            key_name=wordpress_keypair.id,
            tags={
                "Name": "Wordpress.web",
            })

        # Give our EC2 instance an elastic IP address.
        wordpress_eip = ec2.Eip("wordpress-eip", instance=wordpress_instance.id)

        self.wpinstance_ip = wordpress_eip.public_ip
        self.secrule_id = ec2_allow_rule.id
                   
        self.register_outputs({
            'wpinstance_ip': self.wpinstance_ip,
            'secrule_id': self.secrule_id,
        })
