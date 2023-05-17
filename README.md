# Cron2Schedule

Cron2Schedule is an innovative Python utility designed to convert cron expressions into tasks for the Python Schedule library. The idea behind this utility is to introduce more flexibility and readability when it comes to scheduling and executing Python jobs, while still maintaining the syntax and structure that cron users are familiar with. The utility extends the capabilities of the powerful and cross-platform compatible Python Schedule library by including the functionality to schedule tasks using cron expressions.
## Features

* Cron Expressions Translation: Translates five field cron expressions into scheduled Python jobs.
* Intuitive Interface: Cron2Schedule provides an easy-to-use interface to add tasks to your schedule.
* Range Mapping: It supports a range mapping feature that provides an extensive representation of cron field values.


## Usage

To use Cron2Schedule, first import the library in your Python script. Define your job function, then add it to the schedule using the cron expression. For instance:

```

import cron2schedule
import time

def job():
    print("Job Executed!")

cron2schedule.add_to_schedule("*/5 * * * *", job)
cron2schedule.every().hour.do(job)

while True:
    cron2schedule.run_pending()
    time.sleep(1)
```

In this example, the job() function will be executed every 5 minutes, as indicated by the cron expression */5 * * * *. The utility runs the scheduled tasks as long as the Python script is running.
