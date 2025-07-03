from datetime import datetime
from uuid import uuid4

# This is a simple in-memory store for demo purposes.
# In a real application, use a database.
EVENT_DB = {}

class Event:
    """Represents an event record."""
    def __init__(self, title, description, start_time, end_time, location):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'location': self.location,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def update(self, data):
        updated = False
        for key in ['title', 'description', 'start_time', 'end_time', 'location']:
            if key in data:
                setattr(self, key, data[key])
                updated = True
        if updated:
            self.updated_at = datetime.utcnow()

# Interface to in-memory DB
def add_event(event: Event):
    EVENT_DB[event.id] = event
    return event

def get_event(event_id: str):
    return EVENT_DB.get(event_id)

def get_all_events():
    return list(EVENT_DB.values())

def update_event(event_id: str, data):
    event = EVENT_DB.get(event_id)
    if event:
        event.update(data)
    return event

def delete_event(event_id: str):
    return EVENT_DB.pop(event_id, None)
