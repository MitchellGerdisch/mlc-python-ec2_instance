# Pulumi Multi-Language Component: Wordpress EC2 Instance

Python-based MLC that creates an EC2 instance along with some other bits to set it up to be a host for Wordpress.
See https://github.com/MitchellGerdisch/pulumi-work/tree/master/py-yaml-mlc-ansible-wordpress for a Python and YAML project that uses this MLC.

This MLC is based on: https://github.com/pulumi/pulumi-component-provider-py-boilerplate


## Build and Test

```bash

# Regenerate SDKs
make generate

# Build and install the provider and SDKs
make build
make install

### NOTE: After `make install` and before `make dist` edit sdk/python/bin/setup.py to match the VERSION you set in the MAKEFILE

make dist

ls dist/
pulumi-resource-wpinstance-vVERSION-darwin-amd64.tar.gz
pulumi-resource-wpinstance-vVERSION-windows-amd64.tar.gz
pulumi-resource-wpinstance-vVERSION-linux-amd64.tar.gz

pulumi plugin install resource wpinstance VERSION --file dist/pulumi-resource-wpinstance-vVERSION-darwin-amd64.tar.gz
### Where VERSION is the version (without the leading "v").
```
