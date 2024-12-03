import aws_cdk as core
import aws_cdk.assertions as assertions

from rearc_cdk.rearc_cdk_stack import RearcCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in rearc_cdk/rearc_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RearcCdkStack(app, "rearc-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
