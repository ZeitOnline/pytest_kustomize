import pytest

from pytest_kustomize import resolve_configmaps


parametrize = pytest.mark.parametrize


@parametrize("environment", ["staging", "production"])
def test_name_transform_removes_configmap_hash(kustomize_resources, environment):
    config = resolve_configmaps(kustomize_resources[environment])
    for deployment in ["webui", "api"]:
        assert config[deployment]["global_setting"] == "42"
