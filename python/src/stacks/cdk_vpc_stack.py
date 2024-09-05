from aws_cdk import CfnOutput, Stack
import aws_cdk.aws_ec2 as ec2
from constructs import Construct


class CdkVpcStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create VPC
        self.vpc = ec2.Vpc(self, "VPC", max_azs=3, cidr="10.0.0.0/16")
        CfnOutput(self, "Output", value=self.vpc.vpc_id)
