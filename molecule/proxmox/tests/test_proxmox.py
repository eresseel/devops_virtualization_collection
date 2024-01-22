# """
# Testing Proxmox
# """

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("ansible")
    assert passwd.mode == 0o644


def test_not_exists_file(host):
    ceph = host.file("/etc/apt/sources.list.d/ceph.list")
    assert not ceph.exists


def test_exists_file(host):
    proxmox = host. \
      file("/etc/apt/sources.list.d/download_proxmox_com_debian_pve.list")
    assert proxmox.contains("pve-no-subscription")
    assert proxmox.exists


def test_install_program(host):
    assert host.package("mc").is_installed
