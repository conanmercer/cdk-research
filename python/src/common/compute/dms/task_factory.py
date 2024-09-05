from aws_cdk import Stack
from aws_cdk import aws_dms as dms
from constructs import Construct
from abc import ABC, abstractmethod


class DMSTask(ABC):
    @abstractmethod
    def create_task(self, scope: Construct) -> dms.CfnReplicationTask:
        pass


class CDCTask(DMSTask):
    def __init__(
        self,
        shared_cdc_start_position,
        replication_instance_arn,
        source_endpoint_arn,
        target_endpoint_arn,
        table_mappings,
        task_settings,
    ):
        self.shared_cdc_start_position = shared_cdc_start_position
        self.replication_instance_arn = replication_instance_arn
        self.source_endpoint_arn = source_endpoint_arn
        self.target_endpoint_arn = target_endpoint_arn
        self.table_mappings = table_mappings
        self.task_settings = task_settings

    def create_task(self, scope: Construct) -> dms.CfnReplicationTask:
        return dms.CfnReplicationTask(
            scope,
            f"{scope.stack_name}-CDC-Task",
            migration_type="cdc",
            cdc_start_position=self.shared_cdc_start_position,
            replication_instance_arn=self.replication_instance_arn,
            source_endpoint_arn=self.source_endpoint_arn,
            target_endpoint_arn=self.target_endpoint_arn,
            table_mappings=self.table_mappings,
            replication_task_settings=self.task_settings,
        )


class FullLoadTask(DMSTask):
    def __init__(
        self,
        replication_instance_arn,
        source_endpoint_arn,
        target_endpoint_arn,
        table_mappings,
        task_settings,
    ):
        self.replication_instance_arn = replication_instance_arn
        self.source_endpoint_arn = source_endpoint_arn
        self.target_endpoint_arn = target_endpoint_arn
        self.table_mappings = table_mappings
        self.task_settings = task_settings

    def create_task(self, scope: Construct) -> dms.CfnReplicationTask:
        return dms.CfnReplicationTask(
            scope,
            f"{scope.stack_name}-FullLoad-Task",
            migration_type="full-load",
            replication_instance_arn=self.replication_instance_arn,
            source_endpoint_arn=self.source_endpoint_arn,
            target_endpoint_arn=self.target_endpoint_arn,
            table_mappings=self.table_mappings,
            replication_task_settings=self.task_settings,
        )


class FullLoadAndCDCTask(DMSTask):
    def __init__(
        self,
        replication_instance_arn,
        source_endpoint_arn,
        target_endpoint_arn,
        table_mappings,
        task_settings,
    ):
        self.replication_instance_arn = replication_instance_arn
        self.source_endpoint_arn = source_endpoint_arn
        self.target_endpoint_arn = target_endpoint_arn
        self.table_mappings = table_mappings
        self.task_settings = task_settings

    def create_task(self, scope: Construct) -> dms.CfnReplicationTask:
        return dms.CfnReplicationTask(
            scope,
            f"{scope.stack_name}-FullLoadAndCDC-Task",
            migration_type="full-load-and-cdc",
            replication_instance_arn=self.replication_instance_arn,
            source_endpoint_arn=self.source_endpoint_arn,
            target_endpoint_arn=self.target_endpoint_arn,
            table_mappings=self.table_mappings,
            replication_task_settings=self.task_settings,
        )


class DMSTaskFactory(ABC):
    @abstractmethod
    def create_task(self, task_type: str) -> DMSTask:
        pass


class ConcreteDMSTaskFactory(DMSTaskFactory):
    def create_task(self, task_type: str, **kwargs) -> DMSTask:
        if task_type == "cdc":
            return CDCTask(**kwargs)
        elif task_type == "full-load":
            return FullLoadTask(**kwargs)
        elif task_type == "full-load-and-cdc":
            return FullLoadAndCDCTask(**kwargs)
        else:
            raise ValueError(f"Unknown task type: {task_type}")
