using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Constructs;

namespace Csharp
{
    public class VpcStack : Stack
    {
        public Vpc Vpc { get; private set; }

        public VpcStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Create VPC
            Vpc = new Vpc(this, "VPC", new VpcProps
            {
                MaxAzs = 3,
                Cidr = "10.0.0.0/16"
            });

            new CfnOutput(this, "Output", new CfnOutputProps
            {
                Value = Vpc.VpcId
            });
        }
    }
}
