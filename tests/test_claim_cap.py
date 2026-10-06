"""Claim-cap inventory for The-Origin-Point-Hypothesis. No physics validation."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "CLAIM_STATUS.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "origin-point-core.tex",
)
PDF_NAME = "The Origin Point Hypothesis.pdf"


def test_required_files_exist():
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    assert missing == []


def test_classification_and_unsupported_cap():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    claims = (ROOT / "CLAIM_STATUS.md").read_text(encoding="utf-8")
    tex = (ROOT / "origin-point-core.tex").read_text(encoding="utf-8")
    assert "RESEARCH" in readme
    assert "UNSUPPORTED" in claims
    assert "UNSUPPORTED" in tex
    assert "validated against SPARC" not in tex


def test_canonical_index_not_promoted():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "(n-3)" in readme or "(n \u2212 3)" in readme or "n-3" in readme
    assert "Not a proof" in readme or "Not a SPARC" in readme


def test_historical_pdf_retained():
    pdf = ROOT / PDF_NAME
    assert pdf.is_file()
    assert pdf.stat().st_size > 0
