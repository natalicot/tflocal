# resource "aws_vpc" "example" {
#   cidr_block = "10.0.0.0/16"
# }

# resource "aws_subnet" "example1" {
#   vpc_id     = aws_vpc.example.id
#   cidr_block = "10.0.1.0/24"
# }

# resource "aws_subnet" "example2" {
#   vpc_id     = aws_vpc.example.id
#   cidr_block = "10.0.2.0/24"
# }

# module "eks" {
#   source          = "terraform-aws-modules/eks/aws"
#   version         = "17.1.0"
#   cluster_name    = "my-cluster"
#   cluster_version = "1.20"
#   subnets         = [aws_subnet.example1.id, aws_subnet.example2.id]
#   vpc_id          = aws_vpc.example.id

#   node_groups = {
#     eks_nodes = {
#       desired_capacity = 2
#       max_capacity     = 10
#       min_capacity     = 1
#       instance_type    = "m5.large"
#     }
#   }
# }