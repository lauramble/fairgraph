"""
Structured information about an association of two or more persons or organizations, with the objective of participating in a common activity.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class Consortium(KGObject):
    """
    Structured information about an association of two or more persons or organizations, with the objective of participating in a common activity.
    """

    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/core/Consortium"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field("name", str, "vocab:fullName", required=True, doc="Whole, non-abbreviated name of the consortium."),
        Field("alias", str, "vocab:shortName", doc="Shortened or fully abbreviated name of the consortium."),
        Field(
            "contact_information",
            "openminds.core.ContactInformation",
            "vocab:contactInformation",
            doc="Any available way used to contact a person or business (e.g., address, phone number, email address, etc.).",
        ),
        Field("homepage", IRI, "vocab:homepage", doc="Main website of the consortium."),
        Field(
            "is_custodian_of",
            [
                "openminds.computation.ValidationTest",
                "openminds.computation.ValidationTestVersion",
                "openminds.computation.WorkflowRecipe",
                "openminds.computation.WorkflowRecipeVersion",
                "openminds.core.Dataset",
                "openminds.core.DatasetVersion",
                "openminds.core.MetaDataModel",
                "openminds.core.MetaDataModelVersion",
                "openminds.core.Model",
                "openminds.core.ModelVersion",
                "openminds.core.Software",
                "openminds.core.SoftwareVersion",
                "openminds.core.WebService",
                "openminds.core.WebServiceVersion",
                "openminds.publications.LivePaper",
                "openminds.publications.LivePaperVersion",
                "openminds.sands.BrainAtlas",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpace",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "^vocab:custodian",
            reverse="custodians",
            multiple=True,
            doc="reverse of 'custodian'",
        ),
        Field(
            "is_owner_of",
            [
                "openminds.ephys.Electrode",
                "openminds.ephys.ElectrodeArray",
                "openminds.ephys.Pipette",
                "openminds.specimenprep.SlicingDevice",
            ],
            "^vocab:owner",
            reverse="owners",
            multiple=True,
            doc="reverse of 'owner'",
        ),
        Field(
            "published",
            [
                "openminds.publications.Book",
                "openminds.publications.Chapter",
                "openminds.publications.LearningResource",
                "openminds.publications.ScholarlyArticle",
            ],
            "^vocab:publisher",
            reverse="publishers",
            multiple=True,
            doc="reverse of 'publisher'",
        ),
        Field(
            "is_provider_of",
            "openminds.chemicals.ProductSource",
            "^vocab:provider",
            reverse="providers",
            multiple=True,
            doc="reverse of 'provider'",
        ),
        Field(
            "coordinated_projects",
            "openminds.core.Project",
            "^vocab:coordinator",
            reverse="coordinators",
            multiple=True,
            doc="reverse of 'coordinator'",
        ),
        Field(
            "manufactured",
            "openminds.core.Setup",
            "^vocab:manufacturer",
            reverse="manufacturers",
            multiple=True,
            doc="reverse of 'manufacturer'",
        ),
        Field(
            "funded",
            "openminds.core.Funding",
            "^vocab:funder",
            reverse="funders",
            multiple=True,
            doc="reverse of 'funder'",
        ),
        Field(
            "contributions",
            "openminds.core.Contribution",
            "^vocab:contributor",
            reverse="contributors",
            multiple=True,
            doc="reverse of 'contributor'",
        ),
        Field(
            "has_members",
            "openminds.core.Affiliation",
            "^vocab:memberOf",
            reverse="member_of",
            multiple=True,
            doc="reverse of 'memberOf'",
        ),
        Field(
            "holds_copyrights",
            "openminds.core.Copyright",
            "^vocab:holder",
            reverse="holders",
            multiple=True,
            doc="reverse of 'holder'",
        ),
    ]
    existence_query_fields = ("name",)

    def __init__(
        self,
        name=None,
        alias=None,
        contact_information=None,
        homepage=None,
        is_custodian_of=None,
        is_owner_of=None,
        published=None,
        is_provider_of=None,
        coordinated_projects=None,
        manufactured=None,
        funded=None,
        contributions=None,
        has_members=None,
        holds_copyrights=None,
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
            contact_information=contact_information,
            homepage=homepage,
            is_custodian_of=is_custodian_of,
            is_owner_of=is_owner_of,
            published=published,
            is_provider_of=is_provider_of,
            coordinated_projects=coordinated_projects,
            manufactured=manufactured,
            funded=funded,
            contributions=contributions,
            has_members=has_members,
            holds_copyrights=holds_copyrights,
        )
