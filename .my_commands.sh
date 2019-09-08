#!/bin/bash

function createGh() {
    cd ~/scripts
    python createGh.py $1
    cd /home/vs/work/$1
    git init
    git remote add origin git@github.com:vladshut/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    phpstorm .
}

function createGl() {
    cd ~/scripts
    python createGl.py $1
    cd /home/vs/work/$1
    git init
    git remote add origin git@gitlab.com:vladshut/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    phpstorm .
}