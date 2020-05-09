from aws_cdk import (
    core,
    aws_cloudtrail,
    aws_ecr
)
from fun_and_profit.fun_and_profit import FunAndProfitStack


class RegistryStack(FunAndProfitStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cloud_trail = aws_cloudtrail.Trail(self, "Trail")
        self.registry = aws_ecr.Repository(
            self, "Repository",
            repository_name="tweet-ingest",
            lifecycle_rules=[aws_ecr.LifecycleRule(max_image_count=10)],
            removal_policy=core.RemovalPolicy.DESTROY
        )
        self.registry.on_cloud_trail_image_pushed("ImagePushed")
