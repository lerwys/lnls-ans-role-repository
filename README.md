LNLS Ansible Role Repository
=======================

References: https://bitbucket.org/europeanspallationsource/ics-ans-role-repository

This Ansible role enables the Debian NSLS-II repositories.

## Requirements

- ansible >= 2.2
- molecule >= 2.20

Role Variables

```yaml
repository_installroot: "/"
```

The `repository_installroot` variable allows to specify an alternative installroot, e.g. /export/nfsroots/debian9/rootfs

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: lnls-ans-role-repository
```

## Tests

Tests are performed using Molecule. To run them with python virtualenv, issue:

```bash
    bash -c "\
        cd ../ && \
        virtualenv env --python python3 && \
        source env/bin/activate && \
        cd lnls-ans-role-repository && \
        pip install molecule docker-py && \
        molecule test"
```

## License

BSD 2-clause
