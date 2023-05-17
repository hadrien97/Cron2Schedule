# Cron2Schedule

An intuitive Python utility for translating cron expressions into Python Schedule library tasks. This utility allows for more flexibility and readability for scheduling and executing Python jobs, following the syntax and structure of cron.

## Features

- Translates a five field cron expression into a scheduled job in Python.
- Provides an intuitive interface to add jobs to the schedule.
- Allows for range mapping of cron field values.

## Installation

To use Cron2Schedule, you need to have Python 3.7 or above. You can install it using pip:
## Usage

```python
from cron2schedule import add_to_schedule

def job():
    print("Job Executed!")

add_to_schedule("*/5 * * * *", job)
```
