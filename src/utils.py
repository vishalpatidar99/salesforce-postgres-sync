import time

def wait_for_job(job, timeout=None):
    start_time = time.time()
    while True:
        if job.is_finished:
            return job.result
        if timeout is not None and time.time() - start_time > timeout:
            return None
        time.sleep(1)