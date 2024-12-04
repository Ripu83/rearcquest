from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_autoscaling as autoscaling,
    aws_iam as iam,
    aws_certificatemanager as acm ,
    aws_elasticloadbalancingv2 as elb,
)

from constructs import Construct

class EcsEc2AlbStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Variables to be replaced
        acm_certificate_arn ='Your ACM ARN'
        docker_image_repo ='ripusudan83/quest:latest'
        ec2_key= 'PEM File Name'

        # VPC
        vpc = ec2.Vpc.from_lookup(self, "MyImportedVPC", is_default=True)

        cluster = ecs.Cluster(
            self, "MyCluster",
            vpc=vpc
        )

        ec2_sg = ec2.SecurityGroup(
            self,
            "Ec2SecurityGroup",
            vpc=vpc,
            description="Allow traffic flow internally in VP",
            allow_all_outbound=True,
        )
        ec2_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),  
            connection=ec2.Port.all_tcp(),   
            description="Allow all inbound traffic for EC2",
        )
        

        ec2_role = iam.Role(self, "EcsInstanceRole", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        ec2_role.add_to_policy(iam.PolicyStatement(
            actions=["ecs:UpdateContainerInstancesState", "ecs:StartTelemetrySession", "ecs:DescribeContainerInstances"],
            resources=["*"]
        ))
        # Define a Launch Template
        launch_template = ec2.LaunchTemplate(
            self, "EcsLaunchTemplate",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ecs.EcsOptimizedImage.amazon_linux2(),
            role=ec2_role,
            security_group=ec2_sg,
            key_name=ec2_key, 
        )

        # Add EC2 Capacity to the ECS Cluster using Launch Template
        auto_scaling_group = autoscaling.AutoScalingGroup(
            self, "EcsAutoScalingGroup",
            vpc=vpc,
            launch_template=launch_template,
            min_capacity=1,
            max_capacity=1, 
        )

         # Create an ASG Capacity Provider
        capacity_provider = ecs.AsgCapacityProvider(
            self, "AsgCapacityProvider",
            auto_scaling_group=auto_scaling_group,
        )

        # Add Capacity Provider to Cluster
        cluster.add_asg_capacity_provider(capacity_provider)

        # ALB ECS Service
        ecs_service = ecs_patterns.ApplicationLoadBalancedEc2Service(
            self, "Ec2ServiceWithALB",
            cluster=cluster,
            memory_limit_mib=512,
            cpu=256,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry(docker_image_repo), 
                container_name='quest',
                container_port=3000,
                environment={
                    "SECRET_WORD": "Hi! I Did It"  # Set your environment variable here
                },
            ),
            public_load_balancer=True  # Expose service to the internet
        )
        

        ecs_service.load_balancer.add_security_group(ec2_sg)


        certificate = acm.Certificate.from_certificate_arn(
            self, "Certificate", acm_certificate_arn
        )
        # Modify the ALB listener to use SSL
        listener = ecs_service.load_balancer.add_listener(
            "HttpsListener",
            port=443,
            protocol=elb.ApplicationProtocol.HTTPS,
            certificates=[certificate], 
            default_target_groups=[ecs_service.target_group],
        )
 

