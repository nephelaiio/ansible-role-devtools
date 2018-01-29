# nephelaiio.devtools

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-devtools.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-devtools)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.devtools-blue.svg)](https://galaxy.ansible.com/nephelaiio/devtools/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/devtools) to install and configure devtools

## Role Variables

```
devtools_packages:
  - build-essential
```
The list of packages to manage

```
devtools_packages_state:
```
The desired package state (i.e present/absent/latest)

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook

```
- hosts: servers
  roles:
     - role: devtools
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch
  * Arch Linux

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
