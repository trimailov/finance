finance
=======

Small django app to track your income and expenses: `finantious.com <http://finantious.com>`__.

Screenshot of how app looks in dev environment

.. image:: docs/dev-screenshot.png
   :alt: dev env screenshot

TODOs
-----------------

- Editable user profile
  - Password reset feature
  - custom currencies

- Better build environment
  - setuptools + Buildout?

- clone transactions (e.g. lunch)

- Do some statistics (maybe d3.js graphs?)
  - Income/Expense graph
  - how to categorize transactions?

Development
-----------

To develop Vagrant box with Ubuntu is used. To set up::

   vagrant up && vagrant ssh
   cd /vagrant
   make dev  # installs with dev dependencies, otherwise `make` is enough
   make migrate
   make run

Deployment
----------

Read `deployments/README.rst <deployments/README.rst>`__.
