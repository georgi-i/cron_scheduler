## Cron scheduler

You can run the script as follows: ./cron_scheduler.py HH:MM < your_config_file

Note that for Windows OS you should \.\ in cmd. 

The config file should contain set of tasks, as the example below:

> 30 1 /bin/run_me_daily

> 45 \* /bin/run_me_hourly

> \* \* /bin/run_me_every_minute

> \* 19 /bin/run_me_sixty_times

The first field represents minutes, the second one is hours.
For both cases \* means that it should run for all values of that field.

**Linux:**
![Image of Spreadsheet](https://github.com/georgi-i/cron_scheduler/blob/main/samples/linux_sample.png)

**Windows:**
![Image of Spreadsheet](https://github.com/georgi-i/cron_scheduler/blob/main/samples/windows_sample.png)





