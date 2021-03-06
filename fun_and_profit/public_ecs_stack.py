from aws_cdk import (
    core,
    aws_ec2,
    aws_ecs
)
import fun_and_profit as fnp


class PublicEcsStack(fnp.FunAndProfitStack):

    def __init__(self, scope: core.Construct, id: str, 
            vpc: aws_ec2.Vpc,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.ecs = aws_ecs.Cluster(
            self, "EcsCluster",
            vpc=vpc
        )
        self.ecs.add_capacity(
            "Capacity",
            instance_type=aws_ec2.InstanceType("t2.micro"),
            desired_capacity=2
        )