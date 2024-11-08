from pathlib import Path

import pytest
from xmlschema import XMLSchema11, XMLSchemaValidationError

TEST_XSD = Path(__file__).parent.parent / "drafts" / "v1.0" / "MetronInfo.xsd"
TEST_FILES_PATH = Path(__file__).parent / "test_files" / "v1.0"


@pytest.mark.parametrize(
    ("xsd", "xml"), [(TEST_XSD, TEST_FILES_PATH / "valid.xml")], ids=["valid_xml"]
)
def test_valid(xsd, xml) -> None:
    schema = XMLSchema11(xsd)
    schema.validate(xml)


@pytest.mark.parametrize(
    ("xsd", "xml"),
    [(TEST_XSD, TEST_FILES_PATH / "dup_primary_attr.xml")],
    ids=["dup_primary_attr_xml"],
)
def test_invalid(xsd, xml) -> None:
    schema = XMLSchema11(xsd)
    with pytest.raises(XMLSchemaValidationError):
        schema.validate(xml)