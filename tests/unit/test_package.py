"""Tests de fumée : le package est installé et importable."""

import re

import pytest

import depression


def test_version_is_semver() -> None:
    assert re.fullmatch(r"\d+\.\d+\.\d+", depression.__version__)


def test_main_prints_version(capsys: pytest.CaptureFixture[str]) -> None:
    depression.main()

    assert capsys.readouterr().out.strip() == f"depression {depression.__version__}"
