#!/bin/bash

# Sets a reasonable secure SECRET_KEY configuration variable
# for deploying to Heroku.

heroku config:set SECRET_KEY="$(python -c 'import random; import string; print("".join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)]))')"
