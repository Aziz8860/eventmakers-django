from .models import Event

def create_event_method(form_data, user_id):
    print("[HUEY]: Processing create event...")
    try:
        # Create event from form data
        event = Event(
            name=form_data['name'],
            description=form_data['description'],
            eventDate=form_data['eventDate'],
            category=form_data.get('category', ''),
            image=form_data.get('image', ''),
            authorId=user_id
        )

        event.save()
        print("[HUEY]: Event created!")

        return {
            'success': True,
            'event_id': event.id,
            'message': 'Event created successfully!'
        }
    except Exception as e:
        return {
            'success': False,
            'message': f'Error creating event: {str(e)}'
        }

def update_event_method(event_id, form_data):
    print("[HUEY]: Processing update event...")
    try:
        # Get the event
        event = Event.objects.get(id=event_id)
        
        # Update event fields
        event.name = form_data['name']
        event.description = form_data['description']
        event.eventDate = form_data['eventDate']
        event.category = form_data.get('category', '')
        event.image = form_data.get('image', '')
        
        event.save()
        print("[HUEY]: Event updated!")
        
        return {
            'success': True,
            'event_id': event.id,
            'message': 'Event updated successfully!'
        }
    except Event.DoesNotExist:
        return {
            'success': False,
            'message': 'Event not found'
        }
    except Exception as e:
        return {
            'success': False,
            'message': f'Error updating event: {str(e)}'
        }