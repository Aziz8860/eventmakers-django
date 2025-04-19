from huey.contrib.djhuey import task
from .methods import create_event_method, update_event_method

@task()
def create_event_task(form_data, user_id, request_id):
    result = create_event_method(form_data, user_id)
    # The result will be stored in Huey's result store
    # and can be retrieved later if needed
    return result

@task()
def update_event_task(event_id, form_data, request_id):
    result = update_event_method(event_id, form_data)
    # The result will be stored in Huey's result store
    # and can be retrieved later if needed
    return result