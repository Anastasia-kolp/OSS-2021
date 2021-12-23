#!/bin/bash

./$1 &
pstree | grep "$1"
