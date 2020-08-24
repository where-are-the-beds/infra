from os import path
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs, 
    core,
)

class WhereAreTheBedsStack(core.Stack):
    def __init__(self, scope, name, **kwargs):
        super().__init__(scope, name, **kwargs)
        vpc = ec2.Vpc(self, 'WhereAreTheBedsStack-vpc')
        cluster = ecs.Cluster(self, 'WhereAreTheBedsStack-cluster', vpc=vpc)
        api_task_definition = ecs.FargateTaskDefinition(self, 'WhereAreTheBedsStack-api-tak', cpu=256, memory_limit_mib=512)
        api_task_definition.add_container('api', image=ecs.ContainerImage.from_asset(path.join(path.dirname(__file__), 'api')))

app = core.App()
WhereAreTheBedsStack(app, 'WhereAreTheBeds')
app.synth()