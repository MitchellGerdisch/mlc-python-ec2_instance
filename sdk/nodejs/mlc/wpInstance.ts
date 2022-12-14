// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class WpInstance extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'wpinstance:mlc:WpInstance';

    /**
     * Returns true if the given object is an instance of WpInstance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WpInstance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WpInstance.__pulumiType;
    }

    /**
     * Id for instance security group rule.
     */
    public /*out*/ readonly secruleId!: pulumi.Output<string>;
    /**
     * The wordpress instance IP address.
     */
    public /*out*/ readonly wpinstanceIp!: pulumi.Output<string>;

    /**
     * Create a WpInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WpInstanceArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceType'");
            }
            if ((!args || args.publicKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'publicKey'");
            }
            if ((!args || args.subnetId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetId'");
            }
            if ((!args || args.vpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcId'");
            }
            resourceInputs["instanceType"] = args ? args.instanceType : undefined;
            resourceInputs["publicKey"] = args ? args.publicKey : undefined;
            resourceInputs["subnetId"] = args ? args.subnetId : undefined;
            resourceInputs["vpcId"] = args ? args.vpcId : undefined;
            resourceInputs["secruleId"] = undefined /*out*/;
            resourceInputs["wpinstanceIp"] = undefined /*out*/;
        } else {
            resourceInputs["secruleId"] = undefined /*out*/;
            resourceInputs["wpinstanceIp"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(WpInstance.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a WpInstance resource.
 */
export interface WpInstanceArgs {
    /**
     * Instance type to use for wordpress instance.
     */
    instanceType: pulumi.Input<string>;
    /**
     * SSH public key for accessing wordpress instance.
     */
    publicKey: pulumi.Input<string>;
    /**
     * Subnet in which to deploy.
     */
    subnetId: pulumi.Input<string>;
    /**
     * VPC in which to deploy.
     */
    vpcId: pulumi.Input<string>;
}
