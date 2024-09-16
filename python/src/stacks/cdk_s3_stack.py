from aws_cdk import Stack, Duration
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

        # L3 construct - A highly configured S3 bucket (using lifecycle rules, encryption, logging)
        l3_bucket = s3.Bucket(
            self,
            "MyL3Bucket",
            bucket_name="my-l3-bucket",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,  # Enable S3-managed encryption
            lifecycle_rules=[
                s3.LifecycleRule(
                    id="MoveToInfrequentAccess",
                    transitions=[
                        s3.Transition(
                            storage_class=s3.StorageClass.INFREQUENT_ACCESS,
                            transition_after=Duration.days(30),
                        ),
                    ],
                    expiration=Duration.days(365),
                )
            ],
            server_access_logs_bucket=l2_bucket,  # Enable access logging to another bucket
        )
