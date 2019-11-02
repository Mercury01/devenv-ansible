#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Running the whole playbook"
    sudo ansible-playbook -i hosts playbook.yml
  else
    echo "Running tasks: $@"
    sudo ansible-playbook -i hosts playbook.yml --tags "$@"
fi
