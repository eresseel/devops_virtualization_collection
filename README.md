# devops_virtualization_collection

## 1. Prepare developer environment
```bash
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r test-requirements.txt

molecule test (--all|-s <scenario name>)        // mind that there is no scenario named 'default'
```

## 2. Documentation
* [ansible_role_proxmox](roles/ansible_role_proxmox/README.md)
