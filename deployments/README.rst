finance deployments
===================

Requirements
------------
::

    pip install ansible

Vagrant deployment
------------------
::

    vagrant up

To relaunch provisioning::

    vagrant provision

Deploy to production
--------------------

Deploys ``prodcution`` branch.

::

    ansible-playbook -i production deploy.yml --ask-become-pass

To have a dry run::

    ansible-playbook -i production deploy.yml --ask-become-pass -C
