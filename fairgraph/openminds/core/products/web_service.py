"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class WebService(KGObject):
    """

    """
    default_space = "webservice"
    type_ = ["https://openminds.ebrains.eu/core/WebService"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the web service."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the web service."),
        Field("custodians", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product."),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the web service."),
        Field("developers", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:developer", multiple=True, required=True,
              doc="Legal person that creates or improves products or services (e.g., software, applications, etc.)."),
        Field("versions", "openminds.core.WebServiceVersion", "vocab:hasVersion", multiple=True, required=True,
              doc="Reference to variants of an original."),
        Field("homepage", IRI, "vocab:homepage", multiple=False, required=False,
              doc="Main website of the web service."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),

    ]
    existence_query_fields = ('name', 'alias', 'description', 'developers', 'versions')

    def __init__(self, name=None, alias=None, custodians=None, description=None, developers=None, versions=None, homepage=None, how_to_cite=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, name=name, alias=alias, custodians=custodians, description=description, developers=developers, versions=versions, homepage=homepage, how_to_cite=how_to_cite)