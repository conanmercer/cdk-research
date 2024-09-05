using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Constructs;
using System;

namespace Csharp.common
{
    // Abstract base class for EBS storage
    public abstract class EbsStorage
    {
        public abstract void Initialize(Construct scope, Vpc vpc);
    }

    // General Purpose EBS (gp2) implementation
    public class GeneralPurposeEbs : EbsStorage
    {
        public GeneralPurposeEbs(string value)
        {
            Console.WriteLine(value);
        }

        public override void Initialize(Construct scope, Vpc vpc)
        {
            new Volume(scope, "MyEbsVolume", new VolumeProps
            {
                AvailabilityZone = vpc.AvailabilityZones[0],
                Size = Size.Gibibytes(10),
                VolumeType = EbsDeviceVolumeType.GP2
            });
        }
    }

    // Provisioned IOPS EBS (io1) implementation
    public class IopsEbs : EbsStorage
    {
        public IopsEbs(string value)
        {
            Console.WriteLine(value);
        }

        public override void Initialize(Construct scope, Vpc vpc)
        {
            new Volume(scope, "MyIopsEbsVolume", new VolumeProps
            {
                AvailabilityZone = vpc.AvailabilityZones[0],
                Size = Size.Gibibytes(20),
                VolumeType = EbsDeviceVolumeType.IO1,
                Iops = 1000  // Set IOPS for IO1 volumes
            });
        }
    }

    // Cold HDD EBS (sc1) implementation
    public class ColdHddEbs : EbsStorage
    {
        public ColdHddEbs(string value)
        {
            Console.WriteLine(value);
        }

        public override void Initialize(Construct scope, Vpc vpc)
        {
            new Volume(scope, "MyColdHddEbsVolume", new VolumeProps
            {
                AvailabilityZone = vpc.AvailabilityZones[0],
                Size = Size.Gibibytes(500),
                VolumeType = EbsDeviceVolumeType.SC1
            });
        }
    }

    // Abstract Factory for creating EBS storage
    public abstract class AbstractFactory
    {
        public abstract EbsStorage CreateEbs(string volumeType);
    }

    // Concrete EBS Factory implementation
    public class EbsFactory : AbstractFactory
    {
        public override EbsStorage CreateEbs(string volumeType)
        {
            switch (volumeType)
            {
                case "gp2":
                    return new GeneralPurposeEbs("General Purpose EBS Created.");
                case "io1":
                    return new IopsEbs("Provisioned IOPS EBS Created.");
                case "sc1":
                    return new ColdHddEbs("Cold HDD EBS Created.");
                default:
                    throw new ArgumentException($"Unknown volume type: {volumeType}");
            }
        }
    }
}
