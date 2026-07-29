"""Tests for repo_analyzer.py."""

import pytest

from ingestion.parsers.base import ParseResult
from ingestion.parsers.repo_analyzer import RepoAnalyzer


@pytest.mark.unit
class TestRepoAnalyzer:
    """Test suite for RepoAnalyzer."""

    @pytest.fixture
    def parser(self):
        """Create a RepoAnalyzer instance."""
        return RepoAnalyzer()

    def test_detects_pytest_test_file(self, parser):
        """Repository with test_*.py should report has_tests=True."""
        repo_data = {
            "name": "sample-project",
            "language": "Python",
            "file_structure": [
                "app.py",
                "test_app.py",
            ],
        }

        result = parser.parse(repo_data)

        assert isinstance(result, ParseResult)
        assert result.metadata["has_tests"] is True

    def test_non_python_test_named_file_is_not_detected(self, parser):
        """A test_ file that is not Python should not count as a test file."""
        repo_data = {
            "name": "sample-project",
            "language": "Python",
            "file_structure": [
            "app.py",
            "docs/test_notes.md",
            ],
        }

        result = parser.parse(repo_data)

        assert isinstance(result, ParseResult)
        assert result.metadata["has_tests"] is False
