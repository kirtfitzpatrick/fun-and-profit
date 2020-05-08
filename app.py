#!/usr/bin/env python3

import os
from aws_cdk import core
import fun_and_profit.fun_and_profit as fnp
from fun_and_profit.network_stack import NetworkStack
from fun_and_profit.tweet_ingest_stack import TweetIngestStack

env = core.Environment(region=os.getenv("AWS_REGION"),
                       account=os.getenv("AWS_ACCOUNT"))

app                = core.App()
organization       = fnp.OrgEnvFactory.try_create_org(app, "FunAndProfit")
environment        = fnp.OrgEnvFactory.try_create_env(organization, "DeleteMe")
network_stack      = NetworkStack(environment, "Network", env=env)
tweet_ingest_stack = TweetIngestStack(
    environment,
    "TweetIngest",
    vpc=network_stack.vpc,
    env=env
)
tweet_ingest_stack.add_dependency(network_stack)

# --------------------------------------------------------------------------------
print("")
print(f"organization.node.unique_id:  {organization.node.unique_id}")
print(f"environment.node.unique_id:   {environment.node.unique_id}")
print(f"network_stack.node.unique_id: {network_stack.node.unique_id}")
print("")
# --------------------------------------------------------------------------------

app.synth()
