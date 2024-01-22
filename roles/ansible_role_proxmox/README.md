# Ansible Proxmox role
Configure Proxmox on Debian 12 system.

## 1. Requirements
You need Python an GNU tar installed on the target system and sudo privileges.

## 2. Role Variables
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

### 3.1. defaults/main.yml
```yaml
delete_repositories_files:
  - path: /etc/apt/sources.list
  - path: /etc/apt/sources.list.d/ceph.list
  - path: /etc/apt/sources.list.d/pve-enterprise.list
  - path: /etc/apt/sources.list.d/pve-no-subscription.list

gpg_keys:
  - url: https://enterprise.proxmox.com/debian/proxmox-release-bookworm.gpg

add_repositories_files:
  - name: "deb http://deb.debian.org/debian/ bookworm main contrib non-free"
  - name: "deb http://deb.debian.org/debian/ bookworm-updates main contrib non-free"
  - name: "deb http://deb.debian.org/debian/ bookworm-backports main contrib non-free"
  - name: "deb http://deb.debian.org/debian-security bookworm-security main contrib"
  - name: "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/proxmox-release-bookworm.gpg] http://download.proxmox.com/debian/pve bookworm pve-no-subscription"

programs:
  - name: gnupg
  - name: gnupg2
  - name: apt-transport-https
  - name: ca-certificates
  - name: software-properties-common
  - name: sudo
  - name: mc
  - name: vim
  - name: ncdu
  - name: htop
  - name: net-tools
  - name: tcpdump

users: []
ssh_pub_keys: []
root_password: ""

_delete_repositories_files: []
_gpg_keys: []
_add_repositories_files: []
_programs: []
```

### 3.2. playbook configuration
```yaml
delete_repositories_files:
  - path: /etc/apt/sources.list

gpg_keys:
  - url: https://enterprise.proxmox.com/debian/proxmox-release-bookworm.gpg

add_repositories_files:
  - name: "deb http://deb.debian.org/debian/ bookworm main contrib non-free"

programs:
  - name: gnupg

users: "ansible"
ssh_pub_keys: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDEwMc0aDED9PHkFQnLHzKQTuvgiDI3lkBbwkhOo+crsILlu7hryjIJcG9makzGLd6oWvt2P+2NteTZryQFBHvtYWIeOVNIXb391CDWOaNzg1MDTh60Ef98H8ZSIcn2tHoE6cfkknVgUMs2hjV4bjUwUgBPnFpn4fDfR3OuI4CQa5thUwN1S2UOsZoZNtpZcF0PLzrvyBXL7eGOG4/Ouhk9sdNObt5G4A084js8ctiyG/BdFFvIG/ax0bKFSL27vNcUj+i7zBedzlTdU0AF3Kt1bzt1gpFjj6i6wGWcwswqwa+LsWklgYUotlmTEGLCRyQx7lfusAkSwfBC9CuY2AHzpTtHqag0OOw+kaMjevI8hd8yA5/exEPFOUk2Sv6uI844t9TYeHSSgJx3M92uKVd1TVYjRcIObw0RdWy18ga7iFnMy90e9Bo4RYcS0V1OrFRGto39SHaRu0+JkUlT5RbImo7jBwjTE+F1Yd60e1kvhFqAMMDWQigCq3HBGoZD2RC8HKjicTSWbGMZWdsnQf1seTE3mhyk7DZswDQ7oDS8oBHupl8s8bbsTW0OYid54CSF5OFOpLeK4TgxGtivsqPaQiqguk++430gVBaz0kmGdqqF68LXV2UXQ6cTh2l6au9hLwAl9ws7NMNwZLiNeOEa09r9qarU2y+l59NAHAML3Q== test.services.jenkins@mydomain.com"
root_password: "root123"

_delete_repositories_files:
  - path: /etc/apt/sources.list.d/ceph.list
_gpg_keys:
  - url: https://enterprise.proxmox.com/debian/proxmox-release-bookworm.gpg
_add_repositories_files:
  - name: "deb http://deb.debian.org/debian/ bookworm main contrib non-free"
_programs: "ncdu"
```