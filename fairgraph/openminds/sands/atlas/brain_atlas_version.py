"""
Structured information on a brain atlas (version level).
"""

# this file was auto-generated

from fairgraph import KGObject, IRI
from fairgraph.properties import Property


from datetime import date
from fairgraph.base import IRI


class BrainAtlasVersion(KGObject):
    """
    Structured information on a brain atlas (version level).
    """

    default_space = "atlas"
    type_ = ["https://openminds.ebrains.eu/sands/BrainAtlasVersion"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    properties = [
        Property("abbreviation", str, "vocab:abbreviation", doc="no description available"),
        Property(
            "accessibility",
            "openminds.controlled_terms.ProductAccessibility",
            "vocab:accessibility",
            required=True,
            doc="Level to which something is accessible to the brain atlas version.",
        ),
        Property(
            "authors",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:author",
            multiple=True,
            doc="Creator of a literary or creative work, as well as a dataset publication.",
        ),
        Property(
            "coordinate_space",
            "openminds.sands.CommonCoordinateSpaceVersion",
            "vocab:coordinateSpace",
            required=True,
            doc="Two or three dimensional geometric setting.",
        ),
        Property(
            "copyright",
            "openminds.core.Copyright",
            "vocab:copyright",
            doc="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
        ),
        Property(
            "custodians",
            ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"],
            "vocab:custodian",
            multiple=True,
            doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the brain atlas version.",
        ),
        Property(
            "digital_identifier",
            ["openminds.core.DOI", "openminds.core.ISBN", "openminds.core.RRID"],
            "vocab:digitalIdentifier",
            doc="Digital handle to identify objects or legal persons.",
        ),
        Property(
            "full_documentation",
            ["openminds.core.DOI", "openminds.core.File", "openminds.core.WebResource"],
            "vocab:fullDocumentation",
            required=True,
            doc="Non-abridged instructions, comments, and information for using a particular product.",
        ),
        Property("full_name", str, "vocab:fullName", doc="Whole, non-abbreviated name of the brain atlas version."),
        Property(
            "funding",
            "openminds.core.Funding",
            "vocab:funding",
            multiple=True,
            doc="Money provided by a legal person for a particular purpose.",
        ),
        Property(
            "has_terminology",
            "openminds.sands.ParcellationTerminologyVersion",
            "vocab:hasTerminology",
            required=True,
            doc="no description available",
        ),
        Property("homepage", IRI, "vocab:homepage", doc="Main website of the brain atlas version."),
        Property(
            "how_to_cite",
            str,
            "vocab:howToCite",
            doc="Preferred format for citing a particular object or legal person.",
        ),
        Property(
            "is_alternative_version_of",
            "openminds.sands.BrainAtlasVersion",
            "vocab:isAlternativeVersionOf",
            multiple=True,
            doc="Reference to an original form where the essence was preserved, but presented in an alternative form.",
        ),
        Property(
            "is_new_version_of",
            "openminds.sands.BrainAtlasVersion",
            "vocab:isNewVersionOf",
            doc="Reference to a previous (potentially outdated) particular form of something.",
        ),
        Property(
            "keywords",
            [
                "openminds.controlled_terms.ActionStatusType",
                "openminds.controlled_terms.AgeCategory",
                "openminds.controlled_terms.AnalysisTechnique",
                "openminds.controlled_terms.AnatomicalAxesOrientation",
                "openminds.controlled_terms.AnatomicalIdentificationType",
                "openminds.controlled_terms.AnatomicalPlane",
                "openminds.controlled_terms.AnnotationCriteriaType",
                "openminds.controlled_terms.AnnotationType",
                "openminds.controlled_terms.AtlasType",
                "openminds.controlled_terms.AuditoryStimulusType",
                "openminds.controlled_terms.BiologicalOrder",
                "openminds.controlled_terms.BiologicalProcess",
                "openminds.controlled_terms.BiologicalSex",
                "openminds.controlled_terms.BreedingType",
                "openminds.controlled_terms.CellCultureType",
                "openminds.controlled_terms.CellType",
                "openminds.controlled_terms.ChemicalMixtureType",
                "openminds.controlled_terms.Colormap",
                "openminds.controlled_terms.ContributionType",
                "openminds.controlled_terms.CranialWindowConstructionType",
                "openminds.controlled_terms.CranialWindowReinforcementType",
                "openminds.controlled_terms.CriteriaQualityType",
                "openminds.controlled_terms.DataType",
                "openminds.controlled_terms.DeviceType",
                "openminds.controlled_terms.DifferenceMeasure",
                "openminds.controlled_terms.Disease",
                "openminds.controlled_terms.DiseaseModel",
                "openminds.controlled_terms.EducationalLevel",
                "openminds.controlled_terms.ElectricalStimulusType",
                "openminds.controlled_terms.EthicsAssessment",
                "openminds.controlled_terms.ExperimentalApproach",
                "openminds.controlled_terms.FileBundleGrouping",
                "openminds.controlled_terms.FileRepositoryType",
                "openminds.controlled_terms.FileUsageRole",
                "openminds.controlled_terms.GeneticStrainType",
                "openminds.controlled_terms.GustatoryStimulusType",
                "openminds.controlled_terms.Handedness",
                "openminds.controlled_terms.Language",
                "openminds.controlled_terms.Laterality",
                "openminds.controlled_terms.LearningResourceType",
                "openminds.controlled_terms.MeasuredQuantity",
                "openminds.controlled_terms.MeasuredSignalType",
                "openminds.controlled_terms.MetaDataModelType",
                "openminds.controlled_terms.ModelAbstractionLevel",
                "openminds.controlled_terms.ModelScope",
                "openminds.controlled_terms.MolecularEntity",
                "openminds.controlled_terms.OlfactoryStimulusType",
                "openminds.controlled_terms.OperatingDevice",
                "openminds.controlled_terms.OperatingSystem",
                "openminds.controlled_terms.OpticalStimulusType",
                "openminds.controlled_terms.Organ",
                "openminds.controlled_terms.OrganismSubstance",
                "openminds.controlled_terms.OrganismSystem",
                "openminds.controlled_terms.PatchClampVariation",
                "openminds.controlled_terms.PreparationType",
                "openminds.controlled_terms.ProductAccessibility",
                "openminds.controlled_terms.ProgrammingLanguage",
                "openminds.controlled_terms.QualitativeOverlap",
                "openminds.controlled_terms.SemanticDataType",
                "openminds.controlled_terms.Service",
                "openminds.controlled_terms.SetupType",
                "openminds.controlled_terms.SoftwareApplicationCategory",
                "openminds.controlled_terms.SoftwareFeature",
                "openminds.controlled_terms.Species",
                "openminds.controlled_terms.StimulationApproach",
                "openminds.controlled_terms.StimulationTechnique",
                "openminds.controlled_terms.SubcellularEntity",
                "openminds.controlled_terms.SubjectAttribute",
                "openminds.controlled_terms.TactileStimulusType",
                "openminds.controlled_terms.Technique",
                "openminds.controlled_terms.TermSuggestion",
                "openminds.controlled_terms.Terminology",
                "openminds.controlled_terms.TissueSampleAttribute",
                "openminds.controlled_terms.TissueSampleType",
                "openminds.controlled_terms.TypeOfUncertainty",
                "openminds.controlled_terms.UBERONParcellation",
                "openminds.controlled_terms.UnitOfMeasurement",
                "openminds.controlled_terms.VisualStimulusType",
            ],
            "vocab:keyword",
            multiple=True,
            doc="Significant word or concept that are representative of the brain atlas version.",
        ),
        Property(
            "license",
            "openminds.core.License",
            "vocab:license",
            required=True,
            doc="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
        ),
        Property("major_version_identifier", str, "vocab:majorVersionIdentifier", doc="no description available"),
        Property(
            "ontology_identifier",
            IRI,
            "vocab:ontologyIdentifier",
            doc="Term or code used to identify the brain atlas version registered within a particular ontology.",
        ),
        Property(
            "other_contributions",
            "openminds.core.Contribution",
            "vocab:otherContribution",
            multiple=True,
            doc="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.",
        ),
        Property(
            "related_publications",
            [
                "openminds.core.DOI",
                "openminds.core.HANDLE",
                "openminds.core.ISBN",
                "openminds.core.ISSN",
                "openminds.publications.Book",
                "openminds.publications.Chapter",
                "openminds.publications.ScholarlyArticle",
            ],
            "vocab:relatedPublication",
            multiple=True,
            doc="Reference to something that was made available for the general public to see or buy.",
        ),
        Property(
            "release_date",
            date,
            "vocab:releaseDate",
            required=True,
            doc="Fixed date on which a product is due to become or was made available for the general public to see or buy",
        ),
        Property(
            "repository",
            "openminds.core.FileRepository",
            "vocab:repository",
            doc="Place, room, or container where something is deposited or stored.",
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",
            required=True,
            doc="Shortened or fully abbreviated name of the brain atlas version.",
        ),
        Property(
            "support_channels",
            str,
            "vocab:supportChannel",
            multiple=True,
            doc="Way of communication used to interact with users or customers.",
        ),
        Property(
            "type",
            "openminds.controlled_terms.AtlasType",
            "vocab:type",
            doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
        ),
        Property(
            "used_specimens",
            [
                "openminds.core.Subject",
                "openminds.core.SubjectGroup",
                "openminds.core.TissueSample",
                "openminds.core.TissueSampleCollection",
            ],
            "vocab:usedSpecimen",
            multiple=True,
            doc="no description available",
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",
            required=True,
            doc="Term or code used to identify the version of something.",
        ),
        Property(
            "version_innovation",
            str,
            "vocab:versionInnovation",
            required=True,
            doc="Documentation on what changed in comparison to a previously published form of something.",
        ),
        Property(
            "comments",
            "openminds.core.Comment",
            "^vocab:about",
            reverse="about",
            multiple=True,
            doc="reverse of 'about'",
        ),
        Property(
            "is_input_to",
            [
                "openminds.computation.DataAnalysis",
                "openminds.core.DatasetVersion",
                "openminds.core.ProtocolExecution",
            ],
            ["^vocab:input", "^vocab:inputData"],
            reverse=["input_data", "inputs"],
            multiple=True,
            doc="reverse of input, inputData",
        ),
        Property(
            "is_old_version_of",
            "openminds.sands.BrainAtlasVersion",
            "^vocab:isNewVersionOf",
            reverse="is_new_version_of",
            multiple=True,
            doc="reverse of 'isNewVersionOf'",
        ),
        Property(
            "is_part_of",
            ["openminds.core.Project", "openminds.core.ResearchProductGroup"],
            "^vocab:hasPart",
            reverse="has_parts",
            multiple=True,
            doc="reverse of 'hasPart'",
        ),
        Property(
            "is_version_of",
            "openminds.sands.BrainAtlas",
            "^vocab:hasVersion",
            reverse="has_versions",
            multiple=True,
            doc="reverse of 'hasVersion'",
        ),
        Property(
            "learning_resources",
            "openminds.publications.LearningResource",
            "^vocab:about",
            reverse="about",
            multiple=True,
            doc="reverse of 'about'",
        ),
    ]
    aliases = {"name": "full_name", "alias": "short_name"}
    existence_query_properties = ("short_name", "version_identifier")

    def __init__(
        self,
        name=None,
        alias=None,
        abbreviation=None,
        accessibility=None,
        authors=None,
        comments=None,
        coordinate_space=None,
        copyright=None,
        custodians=None,
        description=None,
        digital_identifier=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        has_terminology=None,
        homepage=None,
        how_to_cite=None,
        is_alternative_version_of=None,
        is_input_to=None,
        is_new_version_of=None,
        is_old_version_of=None,
        is_part_of=None,
        is_version_of=None,
        keywords=None,
        learning_resources=None,
        license=None,
        major_version_identifier=None,
        ontology_identifier=None,
        other_contributions=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        support_channels=None,
        type=None,
        used_specimens=None,
        version_identifier=None,
        version_innovation=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            alias=alias,
            abbreviation=abbreviation,
            accessibility=accessibility,
            authors=authors,
            comments=comments,
            coordinate_space=coordinate_space,
            copyright=copyright,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            has_terminology=has_terminology,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_alternative_version_of=is_alternative_version_of,
            is_input_to=is_input_to,
            is_new_version_of=is_new_version_of,
            is_old_version_of=is_old_version_of,
            is_part_of=is_part_of,
            is_version_of=is_version_of,
            keywords=keywords,
            learning_resources=learning_resources,
            license=license,
            major_version_identifier=major_version_identifier,
            ontology_identifier=ontology_identifier,
            other_contributions=other_contributions,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channels=support_channels,
            type=type,
            used_specimens=used_specimens,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
