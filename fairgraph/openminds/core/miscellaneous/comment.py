"""
Structured information about a short text expressing an opinion on, or giving information about some entity.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field




class Comment(KGObject):
    """
    Structured information about a short text expressing an opinion on, or giving information about some entity.
    """
    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/core/Comment"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("about", ["openminds.computation.ValidationTest", "openminds.computation.ValidationTestVersion", "openminds.computation.WorkflowRecipe", "openminds.computation.WorkflowRecipeVersion", "openminds.core.Dataset", "openminds.core.DatasetVersion", "openminds.core.MetaDataModel", "openminds.core.MetaDataModelVersion", "openminds.core.Model", "openminds.core.ModelVersion", "openminds.core.Software", "openminds.core.SoftwareVersion", "openminds.core.WebService", "openminds.core.WebServiceVersion", "openminds.publications.LivePaper", "openminds.publications.LivePaperVersion", "openminds.sands.BrainAtlas", "openminds.sands.BrainAtlasVersion", "openminds.sands.CommonCoordinateSpace", "openminds.sands.CommonCoordinateSpaceVersion"], "vocab:about", multiple=False, required=True,
              doc="no description available"),
        Field("comment", str, "vocab:comment", multiple=False, required=True,
              doc="no description available"),
        Field("commenter", "openminds.core.Person", "vocab:commenter", multiple=False, required=True,
              doc="no description available"),
        Field("timestamp", datetime, "vocab:timestamp", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('about', 'comment', 'commenter', 'timestamp')

    def __init__(self, about=None, comment=None, commenter=None, timestamp=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, about=about, comment=comment, commenter=commenter, timestamp=timestamp)