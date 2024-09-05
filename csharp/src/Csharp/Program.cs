using Amazon.CDK;

namespace Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            var app = new App();
            
            var account = "123456789";
            var deployEnvironment = "dev";
            var region = "af-south-1";

            var env = new Amazon.CDK.Environment
            {
                Account = account,
                Region = region
            };

            var vpcStack = new VpcStack(app, "dev-vpc-stack", new StackProps { Env = env });
            var ebsStack = new EbsStack(app, $"{deployEnvironment}-ebs", vpcStack.Vpc, new StackProps { Env = env});

            // Add tags to the entire app (all resources created by this app)
            Tags.Of(app).Add("Application", "Dev");
            Tags.Of(app).Add("Environment", deployEnvironment);
            Tags.Of(app).Add("Owner", "Conan");

            app.Synth();
        }
    }
}
