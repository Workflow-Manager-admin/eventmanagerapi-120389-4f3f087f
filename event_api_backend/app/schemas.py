from marshmallow import Schema, fields, validate

# PUBLIC_INTERFACE
class EventSchema(Schema):
    """Schema for returning event information."""
    id = fields.Str(required=True, dump_only=True, description="Event unique identifier")
    title = fields.Str(required=True, description="Title of the event")
    description = fields.Str(required=True, description="Description of the event")
    start_time = fields.DateTime(required=True, description="Event start time (ISO format)")
    end_time = fields.DateTime(required=True, description="Event end time (ISO format)")
    location = fields.Str(required=True, description="Event location")
    created_at = fields.DateTime(dump_only=True, description="Creation timestamp")
    updated_at = fields.DateTime(dump_only=True, description="Update timestamp")

# PUBLIC_INTERFACE
class EventCreateSchema(Schema):
    """Schema for creating a new event."""
    title = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=True)
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    location = fields.Str(required=True)

# PUBLIC_INTERFACE
class EventUpdateSchema(Schema):
    """Schema for updating an event (partial allowed)."""
    title = fields.Str()
    description = fields.Str()
    start_time = fields.DateTime()
    end_time = fields.DateTime()
    location = fields.Str()
