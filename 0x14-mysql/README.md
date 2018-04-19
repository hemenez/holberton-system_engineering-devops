# 0x14. Mysql

## Synopsis
This project covers:
* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 14.04 LTS
* The first line of all files should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* All files should end with a new line
* A `README.md` at the root of the folder of the project is mandatory
* Your Bash script must pass `Shellcheck` (version `0.3.3-1~ubuntu14.04.1` via `apt-get`)
* All files must be executalbe

## Environment
The project was tested and compiled on `Ubuntu 14.04 (trusty64)` via Vagrant run through VirtualBox.

## File Descriptions
This repository contains the following files. Listed are the parameters of each task:

### 0-mysql_configuration_primary, 0-mysql_configuration_replica

Install and configure MySQL on web-01 and web-02 servers using a primary/replica (master/slave) cluster.

* primary is hosted on `web-01`
* replica is hosted on `web-02`
* provide the configuration files (`my.cnf`) as the answer of these files

### 1-mysql_backup

Bash script that generates a MySQL dump and creates a compressed archive out of it.