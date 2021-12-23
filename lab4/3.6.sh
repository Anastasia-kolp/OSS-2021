#!/bin/bash

COUNT_NUMBER=`echo -e "$USER$HOME" | tr -d "\n" | wc -c`

echo "$USER $HOME $COUNT_NUMBER"
