# Ansible K2K Federation Playbook

This Ansible playbook sets up two VMs (Ubuntu 14.04 or CentOS/RHEL 7) with
DevStacks federated with K2K between them.

## Steps

Create a hosts file in the same directory with the information of the VMs.
```
[k2k-idp]
192.168.3.1 ansible_user=ubuntu

[k2k-sp]
192.168.3.2 ansible_user=ubuntu
```

Install ansible and run the playbook. You should've already tried to connect
to the VMs previously and have accepted their key.

```bash
# Install ansible
pip install ansible

# Run the playbook with hosts as the inventory file
ansible-playbook site.yml -i hosts -v
```

SSH to the IdP and run the test_k2k.py script in the home folder. If you get a
forbidden action because of the policy, everything works fine. 
