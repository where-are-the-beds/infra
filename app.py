from os import path
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs, 
    aws_ecs_patterns as ecs_patterns,
    core,
)

class WhereAreTheBedsStack(core.Stack):
    def __init__(self, scope, name, **kwargs):
        super().__init__(scope, name, **kwargs)
        
        vpc = ec2.Vpc(self, 'WhereAreTheBedsStack-vpc')
        cluster = ecs.Cluster(self, 'WhereAreTheBedsStack-cluster', vpc=vpc)
        fargate = ecs_patterns.ApplicationLoadBalancedFargateService(self, 'WhereAreTheBedsStack-fargate',cluster=cluster,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_asset(path.join(path.dirname(__file__), 'api'))),
                # image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")),
            public_load_balancer=True)

app = core.App()
WhereAreTheBedsStack(app, 'WhereAreTheBeds')
app.synth()