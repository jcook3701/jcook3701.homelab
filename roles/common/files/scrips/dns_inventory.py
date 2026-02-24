#!/usr/bin/env python3

import sys
import yaml
import re
from ipaddress import ip_address
from collections import OrderedDict


def parse_dns_zone(zone_file):
    """Parse the DNS zone file and extract relevant records."""
    with open(zone_file, "r") as file:
        lines = file.readlines()

    records = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith(";"):
            continue  # Skip comments and empty lines
        parts = re.split(r"\s+", line)
        if len(parts) >= 4 and parts[2] in ["A", "AAAA"]:
            hostname = parts[0]
            # Skip any hostnames containing the '@' symbol
            if "@" in hostname:
                continue
            records.append(parts)

    return records


def generate_ansible_inventory(records):
    """Generate the Ansible inventory from the parsed records."""
    ip_to_hostname = OrderedDict()

    for record in records:
        hostname, _, record_type, ip = record[:4]

        if record_type == "A" or record_type == "AAAA":
            ip_to_hostname[ip] = hostname

    # Sort IPs numerically and keep the last hostname for each IP
    sorted_ips = sorted(ip_to_hostname.keys(), key=lambda ip: ip_address(ip))

    inventory = OrderedDict({"all": OrderedDict({"hosts": OrderedDict()})})

    for ip in sorted_ips:
        inventory["all"]["hosts"][ip_to_hostname[ip]] = {"ansible_host": ip}

    return inventory


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def represent_ordereddict(dumper, data):
    return dumper.represent_dict(data.items())


def main():
    """Main function to parse input and generate the output YAML file."""
    if len(sys.argv) != 3:
        print("Usage: {} <dns_zone_file> <output_yaml_file>".format(sys.argv[0]))
        sys.exit(1)

    zone_file = sys.argv[1]
    output_file = sys.argv[2]

    records = parse_dns_zone(zone_file)
    inventory = generate_ansible_inventory(records)

    yaml.add_representer(OrderedDict, represent_ordereddict, Dumper=NoAliasDumper)

    # Clean YAML output by dumping it without Python-specific types
    with open(output_file, "w") as file:
        yaml.dump(
            inventory,
            file,
            Dumper=NoAliasDumper,
            default_flow_style=False,
            allow_unicode=True,
        )

    print(f"Ansible inventory YAML file generated: {output_file}")


if __name__ == "__main__":
    main()
