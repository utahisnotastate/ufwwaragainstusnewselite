"""Shared test helpers: load a module's simulation.py by folder name."""
import importlib.util
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_simulation(folder):
    path = ROOT / folder / "simulation.py"
    spec = importlib.util.spec_from_file_location(f"{folder}.simulation", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def sim(request):
    """The simulation module named by FOLDER in the requesting test file."""
    return load_simulation(request.module.FOLDER)
