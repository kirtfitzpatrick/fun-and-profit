from aws_cdk import (
    core,
    aws_s3,
    aws_iam
)
from fun_and_profit.fun_and_profit import FunAndProfitStack


class S3Stack(FunAndProfitStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        self.group     = aws_iam.Group(self, "Group")
        self.s3_bucket = aws_s3.Bucket(self, "Bucket")
        self.s3_bucket.grant_read_write(group)
