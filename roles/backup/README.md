# Backup

Backup script to backup each of the following partitions, individually, using **[rdiff-backup](https://rdiff-backup.net/)**:

* "/boot"
* "/etc"
* "/home"
* "/opt"
* "/root"
* "/srv"
* "/usr/local"
* "/var"

## Backup Vars

* backup_server
* backup_source_dir
* backup_dest_dir  

<!--
    TODO: Hidden task list:
        1. Split rdiff command so that home directory is backed-up separately than the other directories

-->
