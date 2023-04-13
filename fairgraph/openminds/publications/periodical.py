"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field




class Periodical(KGObject):
    """

    """
    default_space = "livepapers"
    type_ = ["https://openminds.ebrains.eu/publications/Periodical"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=False,
              doc="Word or phrase that constitutes the distinctive designation of the periodical."),
        Field("abbreviation", str, "vocab:abbreviation", multiple=False, required=False,
              doc="no description available"),
        Field("digital_identifier", "openminds.core.ISSN", "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),

    ]
    existence_query_fields = ('abbreviation',)

    def __init__(self, name=None, abbreviation=None, digital_identifier=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, name=name, abbreviation=abbreviation, digital_identifier=digital_identifier)