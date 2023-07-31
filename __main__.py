"""A Python Pulumi program"""

import pulumi
import pulumi_digitalocean as digitalocean

# Create a new Web Droplet in the nyc2 region
web = digitalocean.Droplet(
    "web", image="ubuntu-18-04-x64", region="nyc3", size="s-1vcpu-1gb"
)
