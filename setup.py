from setuptools import setup, find_packages
from typing import List

# Return the list of install requirements by parsing requirements.txt
def get_requirements() -> List[str]:
    """Read requirements.txt and return a list of requirements.

    Lines that are empty or start with '#' are ignored. Editable local
    installs (e.g. '-e .') and options are skipped.
    """
    requirements: List[str] = []
    try:
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                # Skip editable/local references and installer options
                if line.startswith('-e ') or line.startswith('--editable') or line.startswith('--'):
                    continue
                requirements.append(line)
    except FileNotFoundError:
        # No requirements file; return empty list
        pass
    return requirements


if __name__ == "__main__":
    # Minimal setup configuration; pyproject.toml already contains project metadata,
    # but a setup.py helps editable installs with legacy build backends.
    setup(
        name="ai-trip-planner",
        version="0.1.0",
        packages=find_packages(exclude=("tests",)),
        install_requires=get_requirements(),
    )

