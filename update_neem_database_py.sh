#!/bin/bash

# Function to display usage information
usage() {
  echo "Usage: $0 -u <user> [-p <password>] -h <host> -d <database>"
  exit 1
}

# Parse command line arguments
while getopts "u:p:h:d:" opt; do
  case $opt in
    u)
      USER=$OPTARG
      ;;
    p)
      PASSWORD=$OPTARG
      ;;
    h)
      HOST=$OPTARG
      ;;
    d)
      DATABASE=$OPTARG
      ;;
    *)
      usage
      ;;
  esac
done

# Check if required arguments are provided
if [ -z "$USER" ] || [ -z "$HOST" ] || [ -z "$DATABASE" ]; then
  usage
fi

# Construct the database URL based on whether the password is provided
if [ -z "$PASSWORD" ]; then
  DATABASE_URL="mysql+pymysql://${USER}@${HOST}/${DATABASE}"
else
  DATABASE_URL="mysql+pymysql://${USER}:${PASSWORD}@${HOST}/${DATABASE}"
fi

# Output the database URL (optional)
echo "Database URL: ${DATABASE_URL}"

pip install --quiet sqlacodegen

# Execute the sqlacodegen command
sqlacodegen "$DATABASE_URL" --outfile src/neem_query/neems_database.py

pip uninstall --quiet --yes sqlacodegen
pip install --quiet --upgrade sqlalchemy

# Check if the command was successful
if [ $? -eq 0 ]; then
  echo "SQLAlchemy code generation successful. Output written to neems_database.py."
else
  echo "SQLAlchemy code generation failed."
fi
