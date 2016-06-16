#!/usr/bin/env python

import helper_ansible

options = helper_ansible.Options()
options.connection = 'local'  # Need a connection type "smart" or "ssh"
options.become = False

runner = helper_ansible.Runner(
    playbook = './ansible/site.yml',
    inventory_file = "./ansible/inventory",
    options = options
)

result, stats = runner.run()
