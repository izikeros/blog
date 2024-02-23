#!/bin/bash

# from: https://stackoverflow.com/a/30935242/3247880

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/github_id_rsa