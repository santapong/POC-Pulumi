import pulumi
import pulumi_aws as aws

# Reference to existing Security Group
security_group_id = "sg-0c1234567890abcdef"  # Replace with your existing Security Group ID

# Create an S3 bucket
bucket = aws.s3.Bucket("my-bucket")

# Use the latest Amazon Linux 2 AMI for the specified region
ami = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[{"name": "name", "values": ["amzn2-ami-hvm-*-x86_64-gp2"]}]
).id

# Create an EC2 instance
instance = aws.ec2.Instance(
    "my-instance",
    instance_type="t2.micro",
    ami=ami,
    vpc_security_group_ids=[security_group_id],
    tags={"Name": "MyInstance"},
)

# Export the bucket name and instance ID
pulumi.export("bucket_name", bucket.id)
pulumi.export("instance_id", instance.id)