from aws_cdk import core
import types



class Org(core.Construct):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        core.Tag.add(self, key="Organization", value=id)


class Env(core.Construct):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        core.Tag.add(self, key="Environment", value=id)

class OrgEnvFactory():

    @staticmethod
    def try_create_org(scope:core.Construct, default=None) -> Org:
        org_name = scope.node.try_get_context("organization")

        if type(org_name) == str:
            return Org(scope, OrgEnvFactory.format_name(org_name))
        elif type(default) == str:
            return Org(scope, OrgEnvFactory.format_name(default))
        else:
            return None

    @staticmethod
    def try_create_env(scope:core.Construct, default=None) -> Env:
        env_name = scope.node.try_get_context("environment")

        if type(env_name) == str:
            return Env(scope, OrgEnvFactory.format_name(env_name))
        elif type(default) == str:
            return Env(scope, OrgEnvFactory.format_name(default))
        else:
            return None
    
    @staticmethod
    def format_name(name:str):
        # components = list(map(lambda c: c.capitalize(), name.split("_")))
        # return "".join(components)
        return "".join(list(map(lambda c: c.capitalize(), name.split("_"))))


# class FnpConstructNode(core.ConstructNode):
#     def unique_id(self) -> str:
#         return "It Works!"

class FunAndProfitStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # core.Tag.add(self, key="Name", value=self.simple_name)
        # self.stack_id = self.simple_name

    @property
    def simple_name(self) -> str:
        scope_strings = list(map(lambda s: s.node.id, self.node.scopes))
        scope_strings.pop(0)
        
        return "".join(scope_strings)

    # @property
    # def node(self) -> FnpConstructNode:
    #     return FnpConstructNode(self, scope, id)
