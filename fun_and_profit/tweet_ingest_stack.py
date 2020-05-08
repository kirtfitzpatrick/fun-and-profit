from aws_cdk import (
    core,
    aws_cloudtrail,
    aws_ec2,
    aws_ecr,
    aws_ecs,
    aws_iam
)
from fun_and_profit.fun_and_profit import FunAndProfitStack


class TweetIngestStack(FunAndProfitStack):

    def __init__(self, scope: core.Construct, id: str, vpc: aws_ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cloud_trail = aws_cloudtrail.Trail(self, "Trail")
        self.ecr_repo = aws_ecr.Repository(
            self, "Repository",
            repository_name="tweet-ingest",
            lifecycle_rules=[aws_ecr.LifecycleRule(max_image_count=10)],
            removal_policy=core.RemovalPolicy.DESTROY
        )
        self.ecr_repo.on_cloud_trail_image_pushed("ImagePushed")

        self.ecs = aws_ecs.Cluster(
            self, "EcsCluster",
            vpc=vpc
        )
        self.ecs.add_capacity(
            "DefaultAutoScalingGroupCapacity",
            instance_type=aws_ec2.InstanceType("t2.micro"),
            desired_capacity=1
        )

        self.task_definition = aws_ecs.Ec2TaskDefinition(self, "TaskDef")
        self.task_definition.add_container(
            "tweet-ingest",
            image=aws_ecs.ContainerImage.from_ecr_repository(self.ecr_repo),
            memory_limit_mib=128
        )
        
        self.tweet_ingest_service = aws_ecs.Ec2Service(
            self, "Service",
            cluster=self.ecs,
            task_definition=self.task_definition
        )
