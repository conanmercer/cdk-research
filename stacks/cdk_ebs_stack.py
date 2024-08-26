from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

from common.compute.ebs.ebs_factory import EbsFactory


class CdkEbsStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Use the factory to create and initialize the desired EBS volume
        ebs_factory = EbsFactory()
        ebs = ebs_factory.create_ebs(volume_type="io1")  # Choose "gp2", "io1", "sc1", etc.
        ebs.initialize(self, vpc)
