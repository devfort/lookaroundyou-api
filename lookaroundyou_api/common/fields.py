from south.modelsinspector import add_introspection_rules
from uuidfield import UUIDField

class StringUUIDField(UUIDField):
    def to_python(self, value):
        if not value:
            return None
        return unicode(super(StringUUIDField, self).to_python(value))

add_introspection_rules([], [r"^lookaroundyou_api\.common\.fields\.StringUUIDField"])


