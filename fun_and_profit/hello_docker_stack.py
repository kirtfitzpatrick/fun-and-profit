from aws_cdk import (
    core,
    aws_ec2,
    aws_ecr,
    aws_ecs
)
import fun_and_profit as fnp


class HelloDockerStack(fnp.FunAndProfitStack):

    def __init__(self, scope: core.Construct, id: str, 
            ecs: aws_ecs.Cluster,
            registry: aws_ecr.Repository,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.task_definition = aws_ecs.Ec2TaskDefinition(self, "TaskDef")
        self.task_definition.add_container(
            "hello-docker",
            image=aws_ecs.ContainerImage.from_ecr_repository(registry),
            memory_limit_mib=128
        )
        
        self.tweet_ingest_service = aws_ecs.Ec2Service(
            self, "Service",
            cluster=ecs,
            task_definition=self.task_definition
        )
