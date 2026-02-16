# Automation Workflows

## Available Automations

### Daily
- **morning-routine** - Updates, health checks, checkpoint
- **daily-cleanup** - Clean cache, old logs, auto-commit

### Weekly
- **weekly-maintenance** - Full system update, model updates, backups

### On-Demand
- **auto-backup** - Backup all configs before changes
- **task-scheduler** - Run scheduled tasks (use with Termux:Boot)

## Setup Automation

### Manual Widgets
Add to homescreen:
- morning-routine (daily use)
- daily-cleanup (evening)
- weekly-maintenance (Sunday)

### Automatic (with Termux:Boot app)
1. Install Termux:Boot from F-Droid
2. Create: ~/.termux/boot/task-scheduler
3. Link: ln -s ~/ai/scripts/task-scheduler ~/.termux/boot/
4. Reboot to activate

## Customization
Edit schedules in ~/ai/scripts/task-scheduler
