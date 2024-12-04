#!/usr/bin/env python3
import os

import aws_cdk as cdk
from rearc_cdk.quest_ecs_ec2 import EcsEc2AlbStack

app = cdk.App()
# RearcCdkStack(app, "RearcCdkStack"
EcsEc2AlbStack(app, "QuestCdkStack",
    env=cdk.Environment(account='123456789', region='us-east-1'),
    )

app.synth()
