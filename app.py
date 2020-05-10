#!/usr/bin/env python3

from aws_cdk import core
import fun_and_profit as fnp


# Force some decent error messages
fnp.getenv("AWS_ACCESS_KEY_ID")
fnp.getenv("AWS_SECRET_ACCESS_KEY")

aws_env = core.Environment(
    region=fnp.getenv("AWS_REGION"),
    account=fnp.getenv("AWS_ACCOUNT")
)

app = core.App(stack_traces=False)

# Namespace the org and environment with some generic constructs
fnp_org = fnp.Namespace(app, fnp.getenv("FNP_ORG"), "Org")
fnp_env = fnp.Namespace(fnp_org, fnp.getenv("FNP_ENV"), "Env")

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
