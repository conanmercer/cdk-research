import pytest
from aws_cdk import App, Stack
from aws_cdk.assertions import Template
from aws_cdk import aws_ec2 as ec2
from cdk_ebs_stack import CdkEbsStack


@pytest.fixture
def template():
    # Create the CDK app and stack
    app = App()
    stack = Stack(app, "TestStack")

    # Create a VPC within the stack
    vpc = ec2.Vpc(stack, "TestVpc", max_azs=2)

    # Create the CDK stack that uses the VPC
    cdk_stack = CdkEbsStack(stack, "EbsStack", vpc=vpc)

    # Generate the CloudFormation template
    return Template.from_stack(cdk_stack)


def test_ebs_volume_created(template):
    # Check if the EBS volume of type IO1 is created with the correct properties
    template.has_resource_properties(
        "AWS::EC2::Volume",
        {
            "AvailabilityZone": {"Fn::Select": [0, {"Fn::GetAZs": ""}]},
            "Size": 20,  # In GiB
            "VolumeType": "io1",
            "Iops": 1000,
        },
    )
    template.resource_count_is("AWS::EC2::Volume", 1)


def test_invalid_volume_type():
    from cdk_ebs_stack import EbsFactory

    factory = EbsFactory()
    with pytest.raises(ValueError, match="Unknown volume type"):
        factory.create_ebs("invalid-type")
