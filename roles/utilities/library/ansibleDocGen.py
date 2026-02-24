#!/usr/bin/python
# utilities/library/docgen.py

from ansible.module_utils.basic import AnsibleModule
import yaml
import glob
from pathlib import Path


def yaml_to_md(data):
    return yaml.dump(data, sort_keys=False)


def run_module():
    module_args = dict(
        roles_path=dict(type="str", required=True),
        playbooks_path=dict(type="str", required=False, default=None),
        output_path=dict(type="str", required=True),
        include_tasks=dict(type="bool", default=True),
        include_defaults=dict(type="bool", default=True),
        include_meta=dict(type="bool", default=True),
    )

    result = dict(changed=False, message="", generated_files=[])

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    roles_path = module.params["roles_path"]
    playbooks_path = module.params["playbooks_path"]
    output_path = Path(module.params["output_path"])
    include_tasks = module.params["include_tasks"]
    include_defaults = module.params["include_defaults"]
    include_meta = module.params["include_meta"]

    output_path.mkdir(parents=True, exist_ok=True)

    # Process roles
    for role_dir in Path(roles_path).iterdir():
        if not role_dir.is_dir():
            continue
        role_name = role_dir.name
        md = f"# Role: {role_name}\n\n"

        if include_defaults:
            defaults_file = role_dir / "defaults/main.yml"
            if defaults_file.exists():
                defaults = yaml.safe_load(defaults_file.read_text())
                md += f"## Defaults\n```yaml\n{yaml_to_md(defaults)}```\n\n"

        if include_tasks:
            tasks_files = glob.glob(str(role_dir / "tasks/*.yml"))
            if tasks_files:
                md += "## Tasks\n"
                for tf in tasks_files:
                    tasks = yaml.safe_load(Path(tf).read_text())
                    md += f"### {Path(tf).name}\n```yaml\n{yaml_to_md(tasks)}```\n\n"

        if include_meta:
            meta_file = role_dir / "meta/main.yml"
            if meta_file.exists():
                meta = yaml.safe_load(meta_file.read_text())
                md += f"## Meta\n```yaml\n{yaml_to_md(meta)}```\n\n"

        output_file = output_path / f"{role_name}.md"
        output_file.write_text(md)
        result["generated_files"].append(str(output_file))

    # Optional: process playbooks
    if playbooks_path:
        for pb_file in glob.glob(f"{playbooks_path}/*.yml"):
            pb_name = Path(pb_file).stem
            tasks = yaml.safe_load(Path(pb_file).read_text())
            md = f"# Playbook: {pb_name}\n\n```yaml\n{yaml_to_md(tasks)}```\n"
            output_file = output_path / f"{pb_name}.md"
            output_file.write_text(md)
            result["generated_files"].append(str(output_file))

    result["changed"] = True
    result["message"] = f"Docs generated at {output_path}"
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
