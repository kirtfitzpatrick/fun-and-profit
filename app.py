#!/usr/bin/env python3

from aws_cdk import core

from fun_and_profit.fun_and_profit_stack import FunAndProfitStack


app = core.App()
FunAndProfitStack(app, "fun-and-profit")

app.synth()
