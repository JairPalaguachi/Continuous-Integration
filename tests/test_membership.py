
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
    """Test that existing membership plan validates as True."""
    assert validate_membership_plan("basic") is True


def test_validate_invalid_membership_plan():
    """Test that invalid membership plan validates as False."""
    assert validate_membership_plan("gold") is False


def test_validate_valid_additional_features():
    """Test that valid additional features validate as True."""
    features = ["personal_training", "group_classes"]

    assert validate_additional_features(features) is True


def test_validate_invalid_additional_features():
    """Test that invalid additional features validate as False."""
    features = ["personal_training", "invalid_feature"]

    assert validate_additional_features(features) is False


def test_validate_valid_members_count():
    """Test that valid members count validates as True."""
    assert validate_members_count(2) is True


def test_validate_invalid_members_count_zero():
    """Test that zero members count validates as False."""
    assert validate_members_count(0) is False


def test_validate_invalid_members_count_string():
    """Test that string members count validates as False."""
    assert validate_members_count("2") is False


def test_calculate_base_membership_cost():
    """Test that base membership cost is calculated correctly."""
    assert calculate_base_membership_cost("basic") == 50


def test_calculate_base_membership_cost_invalid_plan():
    """Test that invalid plan raises ValueError."""
    with pytest.raises(ValueError):
        calculate_base_membership_cost("invalid")


def test_calculate_additional_features_cost():
    """Test that additional features cost is calculated correctly."""
    features = ["personal_training", "group_classes"]

    assert calculate_additional_features_cost(features) == 120


def test_calculate_additional_features_cost_empty_list():
    """Test that empty features list has zero cost."""
    assert calculate_additional_features_cost([]) == 0


def test_calculate_additional_features_cost_invalid_feature():
    """Test that invalid feature raises ValueError."""
    with pytest.raises(ValueError):
        calculate_additional_features_cost(["invalid_feature"])


def test_contains_premium_features_true():
    """Test that premium features are correctly identified as True."""
    features = ["exclusive_facilities"]

    assert contains_premium_features(features) is True


def test_contains_premium_features_false():
    """Test that non-premium features are correctly identified as False."""
    features = ["group_classes"]

    assert contains_premium_features(features) is False


def test_calculate_group_discount_for_two_members():
    """Test that group discount is applied for two members."""
    assert calculate_group_discount(100, 2) == 10


def test_calculate_group_discount_for_one_member():
    """Test that no group discount is applied for one member."""
    assert calculate_group_discount(100, 1) == 0


def test_calculate_special_offer_discount_over_200():
    """Test that special discount is $20 for subtotal over $200."""
    assert calculate_special_offer_discount(250) == 20


def test_calculate_special_offer_discount_over_400():
    """Test that special discount is $50 for subtotal over $400."""
    assert calculate_special_offer_discount(450) == 50


def test_calculate_special_offer_discount_without_discount():
    """Test that no special discount is applied for low subtotal."""
    assert calculate_special_offer_discount(150) == 0


def test_calculate_premium_surcharge_with_premium_feature():
    """Test that premium surcharge is applied for premium features."""
    features = ["exclusive_facilities"]

    assert calculate_premium_surcharge(100, features) == 15


def test_calculate_premium_surcharge_without_premium_feature():
    """Test that no premium surcharge is applied without premium features."""
    features = ["group_classes"]

    assert calculate_premium_surcharge(100, features) == 0


def test_calculate_total_basic_without_features():
    """Test that total cost is calculated correctly for basic plan without features."""
    total = calculate_membership_total(
        plan="basic",
        features=[],
        members_count=1,
        confirmed=True,
    )

    assert total == 50


def test_calculate_total_with_group_discount():
    """Test that group discount is applied to total cost."""
    total = calculate_membership_total(
        plan="basic",
        features=[],
        members_count=2,
        confirmed=True,
    )

    assert total == 45