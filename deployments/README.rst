finance deployments
===================

Requirements
------------
::

    pip install ansible

Vagrant deployment
------------------
::

    cd deployments
    vagrant up

To relaunch provisioning::

    vagrant provision

Deploy to production
--------------------

Deploys ``production`` branch.

::

    ansible-playbook -i production deploy.yml --ask-become-pass

To have a dry run::

    ansible-playbook -i production deploy.yml --ask-become-pass -C
