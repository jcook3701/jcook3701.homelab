# jcook3701.homelab playbooks

## jcook3701.homelab.backup (rdiff-backup)

Clear all ansible rdiff-backup logs
``` shell
$ ansible-playbook clear-all-logs.yml --tags clear-logs
```

Backup nas server
``` shell
$ ansible-playbook backup-server.yml --tags "server"
```

Backup all workstations
``` shell
$ ansible-playbook backup-workstation.yml --tags "workstation"
```

Backup all workstations and show debug output
``` shell
$ ansible-playbook backup-workstation.yml --tags "workstation, debug"
```

Backup subgroup within workstations host group.  
``` shell
$ ansible-playbook backup-workstation.yml --tags "workstation" --limit <child group>
```

## jcook3701.homelab.common

Get localhost system info.  
``` shell
$ ansible-playbook get-system-info.yml  
```

## jcook3701.homelab.cron_jobs

***

## NAS server cron-jobs
The following are **cron-jobs** that are run locally and used to automate important processes within this network.  

### Update Workstations  

Creates a cron-job that updates workstations each day at 4:00am.  
``` shell
$ ansible-playbook update-workstations-cron.yml --tags "server,update-workstations,create-cron"  
```
Removes the above **cron-job** that updates workstations each day at 4:00am.  
``` shell
$ ansible-playbook update-workstations-cron.yml --tags "server,update-workstations,remove-cron"  
```

### Backup NAS

This creates a **cron-job** that backups machines each day at 4:00am.
``` shell
$ ansible-playbook backup-cron.yml --tags "create-cron"
```

This removes the **cron-job** that backups machines each dat at 4:00am.
``` shell
$ ansible-playbook backup-cron.yml --tags "delete-cron"
```

### Backup workstations

``` shell
$
```

***

## jcook3701.homelab.pkg_install

## jcook3701.homelab.update

<!-- [back](../../README.md) -->
