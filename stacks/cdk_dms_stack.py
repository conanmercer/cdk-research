from aws_cdk import Stack
from constructs import Construct

from common.compute.dms.task_factory import ConcreteDMSTaskFactory


class CdkDmsStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define shared values
        shared_cdc_start_position = "2023-01-01T00:00:00Z"
        replication_instance_arn = "arn:aws:dms:us-west-2:123456789012:rep:ABCDEFGHIJKL"
        source_endpoint_arn = "arn:aws:dms:us-west-2:123456789012:endpoint:SOURCE"
        target_endpoint_arn = "arn:aws:dms:us-west-2:123456789012:endpoint:TARGET"
        table_mappings = '{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"schema-name": "source_schema", "table-name": "%"}, "rule-action": "include"}]}'
        task_settings = '{"TargetMetadata": {"TargetSchema": "target_schema"}}'

        # Create a factory instance
        factory = ConcreteDMSTaskFactory()

        # Create the desired DMS task
        dms_task = factory.create_task(
            task_type="cdc",  # Choose "cdc", "full-load", "full-load-and-cdc", etc.
            shared_cdc_start_position=shared_cdc_start_position,
            replication_instance_arn=replication_instance_arn,
            source_endpoint_arn=source_endpoint_arn,
            target_endpoint_arn=target_endpoint_arn,
            table_mappings=table_mappings,
            task_settings=task_settings,
        )

        # Use the task to create the actual replication task in the CDK stack
        dms_task.create_task(self)
