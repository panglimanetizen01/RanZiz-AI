from source.runtime.composition.runtime_composition_root import (
    RuntimeCompositionRoot,
)


def test_runtime_facade_available():

    root = RuntimeCompositionRoot()

    runtime = root.get_runtime()

    assert runtime is not None


def test_runtime_facade_status():

    root = RuntimeCompositionRoot()

    facade = root.get_runtime()

    status = facade.status()

    assert "runtime" in status
    assert "snapshot" in status


def test_runtime_facade_inspect():

    root = RuntimeCompositionRoot()

    facade = root.get_runtime()

    result = facade.inspect()

    assert isinstance(
        result,
        dict
    )
