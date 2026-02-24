#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests
import urllib.parse

# Dictionary for platform-specific configurations
PLATFORMS = {
    "github": {
        "api_url": "https://api.github.com/repos/{owner}/{repo}/tags",
        "auth_header": lambda token: (
            {"Authorization": f"token {token}"} if token else {}
        ),
    },
    "gitlab": {
        "api_url": "https://gitlab.com/api/v4/projects/{project_path}/repository/tags",
        "auth_header": lambda token: {"Private-Token": token} if token else {},
    },
    "gitlab-freedesktop": {
        "api_url": "https://gitlab.freedesktop.org/api/v4/projects/{project_path}/repository/tags",
        "auth_header": lambda token: {"Private-Token": token} if token else {},
    },
}


def fetch_tags(platform, owner, repo, token, latest):
    """
    Fetch tags from a given platform's API.

    Args:
        platform (str): The platform name (e.g., 'github', 'gitlab').
        owner (str): The owner or group of the repository.
        repo (str): The repository name.
        token (str): Authentication token (if required).
        latest (bool): Whether to return only the most recent tag.

    Returns:
        list or dict: List of tags, a single tag if latest=True, or an error dictionary.
    """
    if platform not in PLATFORMS:
        return {"error": f"Unsupported platform: {platform}"}

    config = PLATFORMS[platform]
    headers = config["auth_header"](token)

    # For GitLab, format owner/repo as `group%2Fproject`
    if platform.startswith("gitlab"):
        project_path = urllib.parse.quote_plus(f"{owner}/{repo}")
        url = config["api_url"].format(project_path=project_path)
    else:
        url = config["api_url"].format(owner=owner, repo=repo)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            tags = [tag["name"] for tag in data]
            return tags[0] if latest and tags else tags
        else:
            return {
                "error": f"Unable to fetch tags (status code {response.status_code})"
            }
    except Exception as e:
        return {"error": f"Failed to fetch tags: {str(e)}"}


def main():
    # Define Ansible module arguments
    module_args = dict(
        provider=dict(
            type="str",
            required=True,
            choices=["github", "gitlab", "gitlab-freedesktop"],
        ),
        owner=dict(type="str", required=True),
        repo=dict(type="str", required=True),
        token=dict(type="str", required=False, no_log=True),
        latest=dict(type="bool", required=False, default=False),
    )

    # Initialize Ansible module
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # Extract parameters
    provider = module.params["provider"]
    owner = module.params["owner"]
    repo = module.params["repo"]
    token = module.params.get("token")
    latest = module.params["latest"]

    # Fetch tags
    result = fetch_tags(provider, owner, repo, token, latest)

    # Return results
    if isinstance(result, dict) and "error" in result:
        module.fail_json(msg=result["error"])
    else:
        module.exit_json(changed=False, tags=result)


if __name__ == "__main__":
    main()
