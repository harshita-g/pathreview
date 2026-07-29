# PathReview Contribution Journal

## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/50

**Issue title:** Add a has_tests boolean to the repo analysis output

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**

The repository analysis output currently does not indicate whether a project includes automated tests. This makes it harder to use test coverage as a signal of repository quality and portfolio readiness. The change will inspect repository contents for common testing indicators, including `tests/` or `test/` directories, a `pytest.ini` file, and Python files matching `test_*.py`. A successful implementation will expose the result as a `has_tests` boolean in the repository analysis output.

**Selection notes and scope reasoning:**

- The issue has clear acceptance criteria.
- The change is limited primarily to `agent/tools/github_tool.py` and `agent/tools/repo_analyzer.py`.
- The required detection rules are concrete and testable.
- The estimated effort of 2–4 hours fits the Module 3 timeline.
- I can verify the implementation using repositories with and without test files.

**Branch name:** feat/50-add-has-tests-field

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger
