## Cron scheduler

You can run the script as follows: ./cron_scheduler.py HH:MM < your_config_file

The config file should contain set of tasks, as the example below:

> 30 1 /bin/run_me_daily

> 45 \* /bin/run_me_hourly

> \* \* /bin/run_me_every_minute

> \* 19 /bin/run_me_sixty_times

The first field represents minutes, the second one is hours.




