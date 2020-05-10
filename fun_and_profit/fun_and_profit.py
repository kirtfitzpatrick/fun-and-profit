from aws_cdk import core
import os


def getenv(key: str, default=None):
    value = os.getenv(key, default)

    if value == None:
        raise KeyError(f"Environment config {key} is not set.")
    elif value == "":
        raise ValueError(f"Environment config {key} is blank.")
    else:
        return value


class Namespace(core.Construct):

    def __init__(self, scope: core.Construct, id: str, level_name: str) -> None:
        id = self._format_name(id)
        super().__init__(scope, id)
        level_name = self._format_name(level_name)
        core.Tag.add(self, key=level_name, value=id)

    def _format_name(self, name: str):
        return "".join(list(map(lambda c: c.capitalize(), name.split("_"))))


class FunAndProfitStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # default_child = self.node.default_child
        # default_child.override_logical_id(self.simple_name)

    @property
    def simple_name(self) -> str:
        scope_strings = list(map(lambda s: s.node.id, self.node.scopes))
        scope_strings.pop(0)
        
        return "".join(scope_strings)