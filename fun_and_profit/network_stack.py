from aws_cdk import (
    core,
    aws_ec2
)
from fun_and_profit.fun_and_profit import FunAndProfitStack


class NetworkStack(FunAndProfitStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self._vpc = aws_ec2.Vpc(
            self, "Vpc",
            cidr                 = "10.0.0.0/16",
            max_azs              = 1,
            subnet_configuration = [
                aws_ec2.SubnetConfiguration(
                    name        = "Public",
                    subnet_type = aws_ec2.SubnetType.PUBLIC,
                    cidr_mask   = 20
                )
            ]
        )

        core.CfnOutput(
            self,
            id="VpcId",
            value=self._vpc.vpc_id
        )

    @property
    def vpc(self) -> aws_ec2.IVpc:
        return self._vpc
