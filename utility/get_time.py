import time

def get_time():

    """
    Return the current time for the locale of your host.
    """

    unfiltered_time = time.localtime()
    current_time = time.strftime("%H:%M:%S", unfiltered_time)
    return current_time