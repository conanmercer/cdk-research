from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_s3 as s3


class Cdks3Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # L1 construct - CfnBucket
        cfn_bucket = s3.CfnBucket(
            self,
            "MyL1Bucket",
            bucket_name="my-l1-bucket",
            versioning_configuration={"status": "Enabled"},
        )

        # L2 construct - Bucket
        l2_bucket = s3.Bucket(
            self,
            "MyL2Bucket",
            bucket_name="my-l2-bucket",
            versioned=True,  # L2 bucket makes enabling versioning simple
        )
