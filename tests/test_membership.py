"""Unit tests for the gym membership business logic."""
import pytest

from src.membership import (
    validate_membership_plan,
    validate_additional_features,
    validate_members_count,
    calculate_base_membership_cost,
    calculate_additional_features_cost,
    contains_premium_features,
    calculate_group_discount,
    calculate_special_offer_discount,
    calculate_premium_surcharge,
    calculate_membership_total,
    generate_membership_summary,
)


def test_validate_existing_membership_plan():
    assert validate_membership_plan("basic") is True


def test_validate_invalid_membership_plan():
    assert validate_membership_plan("gold") is False


def test_validate_valid_additional_features():
    features = ["personal_training", "group_classes"]

    assert validate_additional_features(features) is True


def test_validate_invalid_additional_features():
    features = ["personal_training", "invalid_feature"]

    assert validate_additional_features(features) is False


def test_validate_valid_members_count():
    assert validate_members_count(2) is True


def test_validate_invalid_members_count_zero():
    assert validate_members_count(0) is False


def test_validate_invalid_members_count_string():
    assert validate_members_count("2") is False


def test_calculate_base_membership_cost():
    assert calculate_base_membership_cost("basic") == 50


def test_calculate_base_membership_cost_invalid_plan():
    with pytest.raises(ValueError):
        calculate_base_membership_cost("invalid")


def test_calculate_additional_features_cost():
    features = ["personal_training", "group_classes"]

    assert calculate_additional_features_cost(features) == 120


def test_calculate_additional_features_cost_empty_list():
    assert calculate_additional_features_cost([]) == 0


def test_calculate_additional_features_cost_invalid_feature():
    with pytest.raises(ValueError):
        calculate_additional_features_cost(["invalid_feature"])


def test_contains_premium_features_true():
    features = ["exclusive_facilities"]

    assert contains_premium_features(features) is True


def test_contains_premium_features_false():
    features = ["group_classes"]

    assert contains_premium_features(features) is False


def test_calculate_group_discount_for_two_members():
    assert calculate_group_discount(100, 2) == 10


def test_calculate_group_discount_for_one_member():
    assert calculate_group_discount(100, 1) == 0


def test_calculate_special_offer_discount_over_200():
    assert calculate_special_offer_discount(250) == 20


def test_calculate_special_offer_discount_over_400():
    assert calculate_special_offer_discount(450) == 50


def test_calculate_special_offer_discount_without_discount():
    assert calculate_special_offer_discount(150) == 0


def test_calculate_premium_surcharge_with_premium_feature():
    features = ["exclusive_facilities"]

    assert calculate_premium_surcharge(100, features) == 15


def test_calculate_premium_surcharge_without_premium_feature():
    features = ["group_classes"]

    assert calculate_premium_surcharge(100, features) == 0


def test_calculate_total_basic_without_features():
    total = calculate_membership_total(
        plan="basic",
        features=[],
        members_count=1,
        confirmed=True,
    )

    assert total == 50


def test_calculate_total_with_group_discount():
    total = calculate_membership_total(
        plan="basic",
        features=[],
        members_count=2,
        confirmed=True,
    )

    assert total == 45


def test_calculate_total_with_special_discount_over_200():
    total = calculate_membership_total(
        plan="family",
        features=["personal_training"],
        members_count=1,
        confirmed=True,
    )

    assert total == 240


def test_calculate_total_with_special_discount_over_400():
    total = calculate_membership_total(
        plan="family",
        features=["exclusive_facilities", "specialized_training"],
        members_count=1,
        confirmed=True,
    )

    assert total == 437


def test_calculate_total_with_premium_surcharge():
    total = calculate_membership_total(
        plan="basic",
        features=["exclusive_facilities"],
        members_count=1,
        confirmed=True,
    )

    assert total == 172


def test_calculate_total_cancelled_plan():
    total = calculate_membership_total(
        plan="basic",
        features=[],
        members_count=1,
        confirmed=False,
    )

    assert total == -1


def test_calculate_total_invalid_plan():
    total = calculate_membership_total(
        plan="invalid",
        features=[],
        members_count=1,
        confirmed=True,
    )

    assert total == -1


def test_calculate_total_invalid_feature():
    total = calculate_membership_total(
        plan="basic",
        features=["invalid_feature"],
        members_count=1,
        confirmed=True,
    )

    assert total == -1


def test_calculate_total_invalid_members_count():
    total = calculate_membership_total(
        plan="basic",
        features=[],
        members_count=0,
        confirmed=True,
    )

    assert total == -1


def test_generate_valid_summary():
    summary = generate_membership_summary(
        plan="premium",
        features=["group_classes"],
        members_count=1,
    )

    assert summary["valid"] is True
    assert summary["plan"] == "Premium"
    assert summary["features_cost"] == 40
    assert summary["total"] == 160


def test_generate_summary_invalid_plan():
    summary = generate_membership_summary(
        plan="invalid",
        features=[],
        members_count=1,
    )

    assert summary["valid"] is False
    assert summary["message"] == "Selected membership plan is not available."


def test_generate_summary_invalid_feature():
    summary = generate_membership_summary(
        plan="basic",
        features=["invalid_feature"],
        members_count=1,
    )

    assert summary["valid"] is False
    assert summary["message"] == "One or more selected features are not available."


def test_generate_summary_invalid_members_count():
    summary = generate_membership_summary(
        plan="basic",
        features=[],
        members_count=0,
    )

    assert summary["valid"] is False
    assert summary["message"] == "The number of members must be a positive integer."


