import pytest
from pathlib import Path
from reporter.sarif import parse, render_html
import tempfile


@pytest.fixture
def test_sarif_file():
    return Path(__file__).parent / "data" / "findsecbugs-report.sarif"


@pytest.fixture
def test_pmd_sarif_file():
    return Path(__file__).parent / "data" / "pmd-report.sarif"


def test_parse(test_sarif_file):
    report_data = parse(test_sarif_file)
    assert report_data
    assert len(report_data["runs"]) == 1
    assert (
        report_data["runs"][0]["tool"]["driver"]["name"]
        == "Security audit by Find Security Bugs"
    )


def test_render(test_sarif_file):
    report_data = parse(test_sarif_file)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as hfile:
        html_content = render_html(report_data, hfile.name)
        assert "{{" not in html_content


def test_pmd_render(test_pmd_sarif_file):
    report_data = parse(test_pmd_sarif_file)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as hfile:
        html_content = render_html(report_data, hfile.name)
        assert "{{" not in html_content
