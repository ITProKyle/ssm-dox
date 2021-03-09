"""Test build command."""
from __future__ import annotations

from typing import TYPE_CHECKING

from click.testing import CliRunner

from ssm_dox._cli.main import cli
from ssm_dox.constants import DOCUMENTS_DIR, DOX_DIR
from ssm_dox.dox import Dox
from ssm_dox.finder import Finder

if TYPE_CHECKING:
    from pathlib import Path

    from pytest_mock import MockerFixture

MODULE = "ssm_dox._cli.commands._build"


def test_build(dox_dir: Path, mocker: MockerFixture, tmp_path: Path) -> None:
    """Test build."""
    mock_dox_build = mocker.patch.object(Dox, "build", return_value=None)
    mock_finder = mocker.patch(
        f"{MODULE}.Finder", return_value=Finder(root_dir=dox_dir)
    )
    runner = CliRunner()
    result = runner.invoke(cli, ["build", str(dox_dir), "--output", str(tmp_path)])
    mock_finder.assert_called_once_with(root_dir=dox_dir)
    mock_dox_build.assert_called_once_with(tmp_path)
    assert result.exit_code == 0


def test_build_default(dox_dir: Path, mocker: MockerFixture) -> None:
    """Test build default values."""
    mock_dox_build = mocker.patch.object(Dox, "build", return_value=None)
    mock_finder = mocker.patch(
        f"{MODULE}.Finder", return_value=Finder(root_dir=dox_dir)
    )
    runner = CliRunner()
    result = runner.invoke(cli, ["build"])
    mock_finder.assert_called_once_with(root_dir=DOX_DIR)
    mock_dox_build.assert_called_once_with(DOCUMENTS_DIR)
    assert result.exit_code == 0


def test_build_is_file(tmp_path: Path) -> None:
    """Test build output is file."""
    file_path = tmp_path / "test.txt"
    file_path.touch()
    runner = CliRunner()
    result = runner.invoke(cli, ["build", str(file_path)])
    assert result.exit_code == 1
