#!/bin/bash

# create repository in github.com
function createGh() {
    cd ~/scripts # path to the python scripts folder
    python createGh.py $1
    cd /home/vs/work/$1 # TODO: change to your projects folder
    git init
    git remote add origin git@github.com:vladshut/$1.git # TODO: change to your profile link
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    phpstorm . # TODO: change to your IDE
}

# create repository in gitlab.com
function createGl() {
    cd ~/scripts # path to the python scripts folder
    python createGl.py $1
    cd /home/vs/work/$1 # TODO: change to your projects folder
    git init
    git remote add origin git@gitlab.com:vladshut/$1.git # TODO: change to your profile link
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    phpstorm . # TODO: change to your IDE
}