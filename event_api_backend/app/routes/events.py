from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.models import (
    add_event, get_event,
    get_all_events, update_event,
    delete_event, Event
)
from app.schemas import EventSchema, EventCreateSchema, EventUpdateSchema

blp = Blueprint(
    "Events", "events",
    url_prefix="/events",
    description="Endpoints for managing events"
)

# PUBLIC_INTERFACE
@blp.route("/")
class EventList(MethodView):
    """
    Handles creation and listing of events.
    """
    @blp.response(200, EventSchema(many=True), description="Get all events")
    def get(self):
        """Get all events."""
        return [event.to_dict() for event in get_all_events()]

    @blp.arguments(EventCreateSchema)
    @blp.response(201, EventSchema, description="Event created")
    def post(self, event_data):
        """Create a new event."""
        event = Event(**event_data)
        add_event(event)
        return event.to_dict()


# PUBLIC_INTERFACE
@blp.route("/<string:event_id>")
class EventDetail(MethodView):
    """
    Handles operations on a single event.
    """
    @blp.response(200, EventSchema, description="Get an event by ID")
    def get(self, event_id):
        """Get an event by ID."""
        event = get_event(event_id)
        if not event:
            abort(404, message="Event not found.")
        return event.to_dict()

    @blp.arguments(EventUpdateSchema)
    @blp.response(200, EventSchema, description="Event updated")
    def patch(self, changes, event_id):
        """Update an event (partial update allowed)."""
        event = update_event(event_id, changes)
        if not event:
            abort(404, message="Event not found.")
        return event.to_dict()

    @blp.response(204, description="Event deleted")
    def delete(self, event_id):
        """Delete an event."""
        event = delete_event(event_id)
        if not event:
            abort(404, message="Event not found.")
        return ""
