using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Constructs;
using Csharp.common;

namespace Csharp
{
    public class EbsStack : Stack
    {
        internal EbsStack(Construct scope, string id, Vpc vpc, IStackProps props = null) : base(scope, id, props)
        {
            var ebsFactory = new EbsFactory();
            var ebs = ebsFactory.CreateEbs("io1");
            ebs.Initialize(this, vpc);
        }
    }
}
