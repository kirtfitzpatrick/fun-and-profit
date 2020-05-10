#!/usr/bin/env python3

import os
from aws_cdk import core
import fun_and_profit as fnp


aws_env = core.Environment(
    region=os.getenv("AWS_REGION"),
    account=os.getenv("AWS_ACCOUNT")
)

app = core.App(stack_traces=False)

# Namespace the org and environment with some generic constructs
fnp_org = fnp.Namespace.create(app, "Org", os.getenv("FNP_ORG"))
fnp_env = fnp.Namespace.create(fnp_org, "Env", os.getenv("FNP_ENV"))

# Org wide stacks first
registry_stack = fnp.RegistryStack(fnp_org, "Registry")

# Env specific stacks
network_stack = fnp.NetworkStack(fnp_env, "Network", env=aws_env)
public_ecs_stack = fnp.PublicEcsStack(
    fnp_env,
    "PublicEcs",
    vpc=network_stack.vpc,
    env=aws_env
)
public_ecs_stack.add_dependency(network_stack)

hello_docker_stack = fnp.HelloDockerStack(
    fnp_env,
    "HelloDocker",
    ecs=public_ecs_stack.ecs,
    registry=registry_stack.hello_docker_repo,
    env=aws_env
)
hello_docker_stack.add_dependency(public_ecs_stack)
hello_docker_stack.add_dependency(registry_stack)

tweet_ingest_stack = fnp.TweetIngestStack(
    fnp_env,
    "TweetIngest",
    ecs=public_ecs_stack.ecs,
    registry=registry_stack.tweet_ingest_repo,
    env=aws_env
)
tweet_ingest_stack.add_dependency(public_ecs_stack)
tweet_ingest_stack.add_dependency(registry_stack)

# --------------------------------------------------------------------------------
# print("")
# print(f"fnp_org.node.unique_id:        {fnp_org.node.unique_id}")
# print(f"registry_stack.node.unique_id: {registry_stack.node.unique_id}")
# print(f"fnp_env.node.unique_id:        {fnp_env.node.unique_id}")
# print(f"network_stack.node.unique_id:  {network_stack.node.unique_id}")
# print("")
# --------------------------------------------------------------------------------

app.synth()
