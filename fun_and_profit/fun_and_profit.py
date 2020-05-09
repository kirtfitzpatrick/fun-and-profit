from aws_cdk import core
import types


class Namespace():

    @staticmethod
    def create(scope: core.Construct, namespace: str, id: str) -> core.Construct:
        id        = Namespace._format_name(id)
        namespace = Namespace._format_name(namespace)
        construct = core.Construct(scope, id)
        core.Tag.add(construct, key=namespace, value=id)

        return construct

    @staticmethod
    def _format_name(name: str):
        return "".join(list(map(lambda c: c.capitalize(), name.split("_"))))


class FunAndProfitStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self._stack_name = self.simple_name
        core.Tag.add(self, key="Name", value=self.simple_name)

    @property
    def simple_name(self) -> str:
        scope_strings = list(map(lambda s: s.node.id, self.node.scopes))
        scope_strings.pop(0)
        
        return "".join(scope_strings)