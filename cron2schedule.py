from schedule import *

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def add_to_schedule(cron_expression, job_func,*args, **kwargs):
    """
    Translates a cron expression into a job in the python Schedule library.
    Args:
        cron_expression (str): A cron expression.
        job_func (function): The job function to be scheduled.
    """
    fields = cron_expression.split()
    if len(fields) != 5:
        raise ValueError("Only five field cron expressions are supported.")

    minute, hour, day_of_month, month, day_of_week = fields

    day_ranges = _range_mapping(day_of_week, 1, 7)
    hour_ranges = _range_mapping(hour, 0, 23)
    minute_ranges = _range_mapping(minute, 0, 59)

    for day in day_ranges:
        for h in hour_ranges:
            for m in minute_ranges:
                getattr(default_scheduler.every(), DAYS[day - 1]).at(f'{h:02d}:{m:02d}').do(job_func,*args, **kwargs)

def _range_mapping(value: str, start: int, end: int) -> list:
    """
    Translates cron field into a list of integers.
    Args:
        value (str): A field value from cron expression.
        start (int): The start of the field range.
        end (int): The end of the field range.

    Returns:
        list_values (list): List of integers representing the cron field range.
    """
    # If the value is "*", return the entire range
    if value == "*":
        return list(range(start, end + 1))

    list_values = []

    # Split the value by commas and process each part individually
    for v in value.split(','):
        # Check for the presence of both '-' and '/'
        if '-' in v and '/' in v:
            range_part, step = v.split('/')
            min_val, max_val = map(int, range_part.split('-'))
            list_values.extend(range(min_val, max_val + 1, int(step)))

        # Check for the presence of '-' only
        elif '-' in v:
            min_val, max_val = map(int, v.split('-'))
            list_values.extend(range(min_val, max_val + 1))

        # Check for the presence of '/' only
        elif '/' in v:
            if v.startswith('*'):
                step = int(v.split('/')[1])
                list_values.extend(range(start, end + 1, step))
            else:
                min_val, step = map(int, v.split('/'))
                list_values.extend(range(min_val, end + 1, step))

        # No special characters, just a single number
        else:
            list_values.append(int(v))

    return list_values
