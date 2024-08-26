subnet_group_properties = {
    "SubnetIds": ["subnet-0032f8ad5a588e756", "subnet-00931b66f976091c4", "subnet-0f49847974d429095"],
}

replication_instance_properties = {
    "AllocatedStorage": 50,
    "EngineVersion": "3.5.2",
    "MultiAZ": True,
    "PubliclyAccessible": False,
    "ReplicationInstanceClass": "dms.t3.micro",
    "ReplicationInstanceIdentifier": "cluster-replication-instance-cdk",
}

source_dms_endpoint_properties = {
    "EndpointType": "source",
    "EngineName": "aurora",
    "Port": 3306,
}