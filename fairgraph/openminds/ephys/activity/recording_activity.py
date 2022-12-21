"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class RecordingActivity(KGObject):
    """

    """
    default_space = "in-depth"
    type = ["https://openminds.ebrains.eu/ephys/RecordingActivity"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("lookup_label", str, "vocab:lookupLabel", multiple=False, required=False,
              doc="no description available"),
        Field("custom_property_sets", "openminds.core.CustomPropertySet", "vocab:customPropertySet", multiple=True, required=False,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the recording activity."),
        Field("devices", ["openminds.ephys.ElectrodeArrayUsage", "openminds.ephys.ElectrodeUsage", "openminds.ephys.PipetteUsage"], "vocab:device", multiple=True, required=False,
              doc="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function."),
        Field("ended_at_time", datetime, "vocab:endedAtTime", multiple=False, required=False,
              doc="no description available"),
        Field("inputs", ["openminds.core.SubjectGroupState", "openminds.core.SubjectState", "openminds.core.TissueSampleCollectionState", "openminds.core.TissueSampleState"], "vocab:input", multiple=True, required=True,
              doc="Something or someone that is put into or participates in a process or machine."),
        Field("internal_identifier", str, "vocab:internalIdentifier", multiple=False, required=False,
              doc="Term or code that identifies the recording activity within a particular product."),
        Field("is_part_of", "openminds.core.DatasetVersion", "vocab:isPartOf", multiple=False, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("outputs", ["openminds.core.File", "openminds.core.FileBundle"], "vocab:output", multiple=True, required=True,
              doc="Something or someone that comes out of, is delivered or produced by a process or machine."),
        Field("performed_by", ["openminds.computation.SoftwareAgent", "openminds.core.Person"], "vocab:performedBy", multiple=True, required=False,
              doc="no description available"),
        Field("preparation_design", "openminds.controlledterms.PreparationType", "vocab:preparationDesign", multiple=False, required=False,
              doc="no description available"),
        Field("protocols", "openminds.core.Protocol", "vocab:protocol", multiple=True, required=True,
              doc="Plan that describes the process of a scientific or medical experiment, treatment, or procedure."),
        Field("started_at_time", datetime, "vocab:startedAtTime", multiple=False, required=False,
              doc="no description available"),
        Field("study_targets", ["openminds.controlledterms.AuditoryStimulusType", "openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.BreedingType", "openminds.controlledterms.CellCultureType", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.ElectricalStimulusType", "openminds.controlledterms.GeneticStrainType", "openminds.controlledterms.GustatoryStimulusType", "openminds.controlledterms.Handedness", "openminds.controlledterms.MolecularEntity", "openminds.controlledterms.OlfactoryStimulusType", "openminds.controlledterms.OpticalStimulusType", "openminds.controlledterms.Organ", "openminds.controlledterms.Species", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.TactileStimulusType", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.controlledterms.VisualStimulusType", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.ParcellationEntity", "openminds.sands.ParcellationEntityVersion"], "vocab:studyTarget", multiple=True, required=False,
              doc="Structure or function that was targeted within a study."),

    ]
    existence_query_fields = ('lookup_label',)