import pytest
import src.data_provider as data_provider


def test_is_expected_fixture_result():

    result = data_provider.annual_percentiles_for_soc(
        "151251", "Alabama", "state_M2023_dl"
    )

    expected = [55640, 73200, 100920, 121150, 127270]
    assert (result) == expected
