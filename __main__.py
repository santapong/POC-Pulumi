import pulumi
import pulumi_aws as aws

# Reference to existing Security Group
security_group_id = "sg-0c1234567890abcdef"  # Replace with your existing Security Group ID

# Create an S3 bucket
bucket = aws.s3.Bucket("my-bucket")

# # Use the latest Amazon Linux 2 AMI for the specified region
# ami = aws.ec2.get_ami(
#     most_recent=True,
#     owners=["amazon"],
#     filters=[{"name": "name", "values": ["amzn2-ami-hvm-*-x86_64-gp2"]}]
# ).id

# # Create an EC2 instance
# instance = aws.ec2.Instance(
#     "my-instance",
#     instance_type="t2.micro",
#     ami=ami,
#     vpc_security_group_ids=[security_group_id],
#     tags={"Name": "MyInstance"},
# )

# # Create an ECS cluster
# cluster = aws.ecs.Cluster("my-cluster")

# # Create an ECS task definition
# task_definition = aws.ecs.TaskDefinition(
#     "my-task",
#     family="my-task-family",
#     cpu="256",
#     memory="512",
#     network_mode="awsvpc",
#     requires_compatibilities=["FARGATE"],
#     execution_role_arn=aws.iam.Role("ecsTaskExecutionRole", assume_role_policy="""{
#         "Version": "2012-10-17",
#         "Statement": [
#             {
#                 "Action": "sts:AssumeRole",
#                 "Principal": {
#                     "Service": "ecs-tasks.amazonaws.com"
#                 },
#                 "Effect": "Allow",
#                 "Sid": ""
#             }
#         ]
#     }""").arn,
#     container_definitions="""[{
#         "name": "my-container",
#         "image": "amazon/amazon-ecs-sample",
#         "portMappings": [{
#             "containerPort": 80,
#             "hostPort": 80,
#             "protocol": "tcp"
#         }]
#     }]"""
# )

# # Create an ECS service
# service = aws.ecs.Service(
#     "my-service",
#     cluster=cluster.arn,
#     task_definition=task_definition.arn,
#     desired_count=1,
#     launch_type="FARGATE",
#     network_configuration={
#         "assignPublicIp": "ENABLED",
#         "subnets": ["subnet-12345678"],  # Replace with your subnet ID
#         "security_groups": [security_group_id]
#     }
# )

# # Export the bucket name and instance ID
pulumi.export("bucket_name", bucket.id)
# pulumi.export("instance_id", instance.id)

# # Export the ECS cluster name and service name
# pulumi.export("cluster_name", cluster.name)
# pulumi.export("service_name", service.name)