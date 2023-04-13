"""
Structured information on the contribution made to a research product.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class Contribution(EmbeddedMetadata):
    """
    Structured information on the contribution made to a research product.
    """
    type_ = ["https://openminds.ebrains.eu/core/Contribution"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("contributor", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:contributor", multiple=False, required=True,
              doc="Legal person that gave or supplied something as a part or share."),
        Field("types", "openminds.controlledterms.ContributionType", "vocab:type", multiple=True, required=True,
              doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to."),

    ]

    def __init__(self, contributor=None, types=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, contributor=contributor, types=types)