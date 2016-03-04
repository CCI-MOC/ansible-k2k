#!/usr/bin/python
# Insert auth_uri in [cinder] in nova.conf
import configparser

config = configparser.ConfigParser()
config.read('/etc/nova/nova.conf')

config['cinder']['auth_url'] = config['keystone_authtoken']['auth_uri']

with open('/etc/nova/nova.conf', 'w') as configfile:
    config.write(configfile)
