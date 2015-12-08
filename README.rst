finance
=======

Small django app to track your income and expenses: `finantious.com <http://finantious.com>`__.

Screenshot of how app looks in dev environment

.. image:: docs/dev-screenshot.png
   :alt: dev env screenshot

Most urgent TODOs
-----------------

- Editable user profile
  - Password reset feature
  - custom currencies

- Income/Expense graph

Development
-----------

To develop Vagrant box with Ubuntu is used. To set up::

   vagrant up && vagrant ssh
   cd /vagrant
   make dev  # installs with dev dependancies, otherwise `make` is enough
   make migrate
   make run

Deployment
----------

Read `deployments/README.rst <deployments/README.rst>`__.
