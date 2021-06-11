#!/bin/bash
copy_to=/var/backups/backup-$(date +"%m-%d-%Y-%H-%M")
mongodump --out "$copy_to"
