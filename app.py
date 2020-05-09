#!/usr/bin/env python3

import os
from aws_cdk import core
import fun_and_profit.fun_and_profit as fnp
from fun_and_profit.registry_stack import RegistryStack
from fun_and_profit.network_stack import NetworkStack
from fun_and_profit.tweet_ingest_stack import TweetIngestStack


aws_env = core.Environment(
    region=os.getenv("AWS_REGION"),
    account=os.getenv("AWS_ACCOUNT")
)

app = core.App()

# Namespace the org and environment with some generic constructs
fnp_org = fnp.Namespace.create(app, "Org", os.getenv("FNP_ORG"))
fnp_env = fnp.Namespace.create(fnp_org, "Env", os.getenv("FNP_ENV"))

# Org wide stacks first
registry_stack = RegistryStack(fnp_org, "Registry")

# Env specific stacks
network_stack      = NetworkStack(fnp_env, "Network", env=aws_env)
tweet_ingest_stack = TweetIngestStack(
    fnp_env,
    "TweetIngest",
    vpc=network_stack.vpc,
    registry=registry_stack.registry,
    env=aws_env
)
tweet_ingest_stack.add_dependency(network_stack)
tweet_ingest_stack.add_dependency(registry_stack)

# --------------------------------------------------------------------------------
print("")
print(f"fnp_org.node.unique_id:        {fnp_org.node.unique_id}")
print(f"registry_stack.node.unique_id: {registry_stack.node.unique_id}")
print(f"fnp_env.node.unique_id:        {fnp_env.node.unique_id}")
print(f"network_stack.node.unique_id:  {network_stack.node.unique_id}")
print("")
# --------------------------------------------------------------------------------

app.synth()
