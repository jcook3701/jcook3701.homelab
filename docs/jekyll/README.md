# {{ site.title }}

[![License](https://img.shields.io/github/license/{{ site.github_username }}{{ site.baseurl }})](LICENSE.md)

**Author:** {{ site.author }}  
**Version:** {{ site.version }}  

## Overview

{{ site.description }}  

**Utilizes:**  
The **{{ site.title }}** depends on the following repositories for its documentation and sub-features.  

* **[jcook3701.docker](https://github.com/jcook3701/jcook3701.docker)** Ansible Galaxy collection used to install docker packages.
* **[jcook3701.flatpak](https://github.com/jcook3701/jcook3701.flatpak)** Ansible Galaxy collection used to install flatpak packages.
* **[jcook3701.pkgs](https://github.com/jcook3701/jcook3701.pkgs)** Ansible Galaxy collection used to install system (Debian, Ubuntu, RHEL) packages.
* **[jcook3701.snap](https://github.com/jcook3701/jcook3701.snap)** Ansible Galaxy collection used to install snap packages.
* **[jcook3701.source](https://github.com/jcook3701/jcook3701.source)** Ansible Galaxy collection used to install packages from source code.
* **[jcook3701.utils](https://github.com/jcook3701/jcook3701.utils)** Ansible Galaxy collection of utilities for assisting automation processes.

***

🛠️ **CI/CD Check List:**

* ![dependency-check]({{ site.repo_url }}/actions/workflows/dependency-check.yml/badge.svg)
* ![format-check]({{ site.repo_url }}/actions/workflows/format-check.yml/badge.svg)
* ![lint-check]({{ site.repo_url }}/actions/workflows/lint-check.yml/badge.svg)
* ![security-audit]({{ site.repo_url }}/actions/workflows/security-audit.yml/badge.svg)
* ![spellcheck]({{ site.repo_url }}/actions/workflows/spellcheck.yml/badge.svg)
* ![tests]({{ site.repo_url }}/actions/workflows/tests.yml/badge.svg)
* ![typecheck]({{ site.repo_url }}/actions/workflows/typecheck.yml/badge.svg)

***
<!-- NOTE: This page is currently included in _copy_without_render which is why there are no raw or endraw tags. And no calls to {{ cookiecutter.etc }}. -->
<!-- NOTE: On this page all links need to be from site.github_io_url and not jinja2 links -->

## 🌱 Getting Started

* [Requirements]({{ site.github_io_url }}/manual/setup-guide/requirements)
* [Installation guide]({{ site.github_io_url }}/manual/introduction/installation-guide)  

## 📚 Documentation

The {{ site.title }} documentation is available at [docs]({{ site.github_io_url }}).  

## 🤝 Contributing

If you're interested in contributing to the {{ site.title }} project:  
* Start by reading the [contributing guide]({{ site.github_io_url }}/manual/developer-resources/contribute).  
* Learn how to setup your local environment, in our [developer guide]({{ site.github_io_url }}/manual/contribute/developer-guide).  
* Look through our [style guide]({{ site.github_io_url }}/manual/contribute/style-guides/index).  

## 🍹 Authors Notes

## ⚖️ License

{{ site.copyright }}  

This project is licensed under the **{{ site.license }} License**.  
See the [LICENSE]({{ site.repo_blob }}/LICENSE.md) file for the full license text.  

SPDX-License-Identifier: {{ site.license }}  
