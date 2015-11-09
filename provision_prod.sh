sudo apt-get update
sudo apt-get install -y postgresql-9.3 nginx
sudo -u postgres createdb finance
sudo -u postgres psql -c "CREATE USER justas CREATEDB;"

sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install -y python3.5

sudo apt-get install -y build-essential python3-pip python3.5-venv python3-psycopg2 libpq-dev python3.5-dev

sudo apt-get install -y htop
