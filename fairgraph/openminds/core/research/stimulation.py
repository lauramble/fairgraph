"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Stimulation(KGObject):
    """

    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/Stimulation"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the stimulation."),
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("stimulation_approach", "openminds.controlledterms.StimulationApproach", "vocab:stimulationApproach", multiple=False, required=True,
              doc="no description available"),
        Field("stimulus_type", "openminds.controlledterms.StimulusType", "vocab:stimulusType", multiple=False, required=True,
              doc="no description available"),

    ]
    existence_query_fields = ('lookup_label',)
