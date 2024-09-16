#!/usr/bin/env python3

import os
from aws_cdk import App, Tags, Environment

from stacks.cdk_ebs_stack import CdkEbsStack
from stacks.cdk_vpc_stack import CdkVpcStack
from stacks.cdk_dms_stack import CdkDmsStack
from stacks.cdk_s3_stack import Cdks3Stack

app = App()

# Pull the account from Github env var
account = os.getenv("DEPLOY_ACCOUNT")
deploy_environment = "dev"
region = "af-south-1"

env = Environment(account=account, region=region)

vpc_stack = CdkVpcStack(app, "dev-vpc-stack")
ebs_stack = CdkEbsStack(app, f"{deploy_environment}-ebs", vpc=vpc_stack.vpc)
s3_stack = Cdks3Stack(app, f"{deploy_environment}-s3")
#dms_stack = CdkDmsStack(app, f"{deploy_environment}-dms")

# add tags to the entire app (all resources created by this app)
Tags.of(app).add("Application", "Dev")
Tags.of(app).add("Environment", deploy_environment)
Tags.of(app).add("Owner", "Conan")

app.synth()
