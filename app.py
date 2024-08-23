#!/usr/bin/env python3

import os
from aws_cdk import App, Tags, Environment

from stacks.cdk_ebs_stack import CdkEbsStack
from stacks.cdk_vpc_stack import CdkVpcStack

app = App()

# Pull the account from Github env var
account = os.getenv("DEPLOY_ACCOUNT")
deploy_environment = "dev"
region = "af-south-1"

env = Environment(account=account, region=region)

vpc_stack = CdkVpcStack(app, "dev-vpc-stack")
ebs_stack = CdkEbsStack(app, f"{deploy_environment}-ebs", vpc=vpc_stack.vpc)

# add tags to the entire app (all resources created by this app)
Tags.of(app).add("Application", "Dev")
Tags.of(app).add("Environment", deploy_environment)
Tags.of(app).add("Owner", "Conan")

app.synth()
