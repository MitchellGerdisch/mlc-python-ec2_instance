// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Wpinstance.Mlc
{
    [WpinstanceResourceType("wpinstance:mlc:WpInstance")]
    public partial class WpInstance : Pulumi.ComponentResource
    {
        /// <summary>
        /// The wordpress instance IP address.
        /// </summary>
        [Output("wpinstanceIp")]
        public Output<string> WpinstanceIp { get; private set; } = null!;


        /// <summary>
        /// Create a WpInstance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public WpInstance(string name, WpInstanceArgs args, ComponentResourceOptions? options = null)
            : base("wpinstance:mlc:WpInstance", name, args ?? new WpInstanceArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class WpInstanceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Instance type to use for wordpress instance.
        /// </summary>
        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        /// <summary>
        /// SSH public key for accessing wordpress instance.
        /// </summary>
        [Input("publicKey", required: true)]
        public Input<string> PublicKey { get; set; } = null!;

        /// <summary>
        /// Subnet in which to deploy.
        /// </summary>
        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        /// <summary>
        /// VPC in which to deploy.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public WpInstanceArgs()
        {
        }
    }
}