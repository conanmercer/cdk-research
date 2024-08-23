from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2, Size
from constructs import Construct
from abc import ABC, abstractmethod


class EBSStorage(ABC):
    @abstractmethod
    def initialize(self, scope: Construct, vpc: ec2.Vpc):
        pass


class ProductEbs(EBSStorage):
    def __init__(self, value: str):
        super().__init__()
        print(value)

    def initialize(self, scope: Construct, vpc: ec2.Vpc):
        # General Purpose SSD (gp2)
        ec2.Volume(
            scope,
            "MyEbsVolume",
            availability_zone=vpc.availability_zones[0],
            size=Size.gibibytes(10),
            volume_type=ec2.EbsDeviceVolumeType.GP2,
        )


class IopsEbs(EBSStorage):
    def __init__(self, value: str):
        super().__init__()
        print(value)

    def initialize(self, scope: Construct, vpc: ec2.Vpc):
        # Provisioned IOPS SSD (io1)
        ec2.Volume(
            scope,
            "MyIopsEbsVolume",
            availability_zone=vpc.availability_zones[0],
            size=Size.gibibytes(20),
            volume_type=ec2.EbsDeviceVolumeType.IO1,
            iops=1000,  # Set IOPS for IO1 volumes
        )


class ColdHddEbs(EBSStorage):
    def __init__(self, value: str):
        super().__init__()
        print(value)

    def initialize(self, scope: Construct, vpc: ec2.Vpc):
        # Cold HDD (sc1)
        ec2.Volume(
            scope,
            "MyColdHddEbsVolume",
            availability_zone=vpc.availability_zones[0],
            size=Size.gibibytes(500),
            volume_type=ec2.EbsDeviceVolumeType.SC1,
        )


class AbstractFactory(ABC):
    @abstractmethod
    def create_ebs(self, volume_type: str) -> EBSStorage:
        pass


class EbsFactory(AbstractFactory):
    def create_ebs(self, volume_type: str) -> EBSStorage:
        if volume_type == "gp2":
            return ProductEbs("General Purpose EBS Created.")
        elif volume_type == "io1":
            return IopsEbs("Provisioned IOPS EBS Created.")
        elif volume_type == "sc1":
            return ColdHddEbs("Cold HDD EBS Created.")
        else:
            raise ValueError(f"Unknown volume type: {volume_type}")


class CdkEbsStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Use the factory to create and initialize the desired EBS volume
        ebs_factory = EbsFactory()
        ebs = ebs_factory.create_ebs(volume_type="io1")  # Choose "gp2", "io1", "sc1", etc.
        ebs.initialize(self, vpc)
