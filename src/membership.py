"""Business logic for gym membership plans, features, discounts, and totals."""
MEMBERSHIP_PLANS = {
    "basic": {
        "name": "Basic",
        "cost": 50,
        "benefits": [
            "Access to gym equipment",
            "Locker room access",
            "Basic fitness assessment",
        ],
    },
    "premium": {
        "name": "Premium",
        "cost": 120,
        "benefits": [
            "Access to gym equipment",
            "Group classes",
            "Sauna access",
            "Monthly fitness assessment",
        ],
    },
    "family": {
        "name": "Family",
        "cost": 180,
        "benefits": [
            "Access for family members",
            "Group classes",
            "Locker room access",
            "Family fitness activities",
        ],
    },
}

ADDITIONAL_FEATURES = {
    "personal_training": {
        "name": "Personal Training Sessions",
        "cost": 80,
        "premium": False,
    },
    "group_classes": {
        "name": "Group Classes",
        "cost": 40,
        "premium": False,
    },
    "exclusive_facilities": {
        "name": "Exclusive Gym Facilities",
        "cost": 100,
        "premium": True,
    },
    "specialized_training": {
        "name": "Specialized Training Program",
        "cost": 150,
        "premium": True,
    },
}


def get_available_plans():
    """Return the dictionary of available membership plans."""
    return MEMBERSHIP_PLANS


def get_available_features():
    """Return the dictionary of available additional features."""
    return ADDITIONAL_FEATURES


def validate_membership_plan(plan):
    """Check if the membership plan is valid."""
    return plan in MEMBERSHIP_PLANS


def validate_additional_features(features):
    """Check if all additional features are valid."""
    return all(feature in ADDITIONAL_FEATURES for feature in features)


def validate_members_count(members_count):
    """Check if the members count is a valid positive integer."""
    return isinstance(members_count, int) and members_count >= 1


def calculate_base_membership_cost(plan):
    """Calculate the base cost of a membership plan."""
    if not validate_membership_plan(plan):
        raise ValueError("Selected membership plan is not available.")

    return MEMBERSHIP_PLANS[plan]["cost"]


def calculate_additional_features_cost(features):
    """Calculate the total cost of additional features."""
    if not validate_additional_features(features):
        raise ValueError("One or more selected features are not available.")

    total = 0

    for feature in features:
        total += ADDITIONAL_FEATURES[feature]["cost"]

    return total


def contains_premium_features(features):
    """Check if any of the selected features are premium."""
    if not validate_additional_features(features):
        raise ValueError("One or more selected features are not available.")

    return any(ADDITIONAL_FEATURES[feature]["premium"] for feature in features)


def calculate_group_discount(subtotal, members_count):
    """Calculate the group discount (10% for 2+ members)."""
    if members_count >= 2:
        return subtotal * 0.10

    return 0


def calculate_special_offer_discount(subtotal):
    """Calculate the special offer discount based on subtotal."""
    if subtotal > 400:
        return 50

    if subtotal > 200:
        return 20

    return 0


def calculate_premium_surcharge(subtotal, features):
    """Calculate the premium surcharge (15% if premium features are included)."""
    if contains_premium_features(features):
        return subtotal * 0.15

    return 0


def calculate_membership_total(plan, features=None, members_count=1, confirmed=True):
    """Calculate the total membership cost including all discounts and surcharges."""
    if features is None:
        features = []

    if not confirmed:
        return -1

    if not validate_members_count(members_count):
        return -1

    if not validate_membership_plan(plan):
        return -1

    if not validate_additional_features(features):
        return -1

    base_cost = calculate_base_membership_cost(plan)
    features_cost = calculate_additional_features_cost(features)

    subtotal = base_cost + features_cost

    group_discount = calculate_group_discount(subtotal, members_count)
    subtotal_after_group_discount = subtotal - group_discount

    special_discount = calculate_special_offer_discount(subtotal_after_group_discount)
    subtotal_after_special_discount = subtotal_after_group_discount - special_discount

    premium_surcharge = calculate_premium_surcharge(
        subtotal_after_special_discount,
        features,
    )

    total = subtotal_after_special_discount + premium_surcharge

    return int(round(total))


def generate_membership_summary(plan, features=None, members_count=1):
    """Generate a detailed summary of the membership with all cost breakdowns."""
    if features is None:
        features = []

    if not validate_membership_plan(plan):
        return {
            "valid": False,
            "message": "Selected membership plan is not available.",
        }

    if not validate_additional_features(features):
        return {
            "valid": False,
            "message": "One or more selected features are not available.",
        }

    if not validate_members_count(members_count):
        return {
            "valid": False,
            "message": "The number of members must be a positive integer.",
        }

    base_cost = calculate_base_membership_cost(plan)
    features_cost = calculate_additional_features_cost(features)
    subtotal = base_cost + features_cost

    group_discount = calculate_group_discount(subtotal, members_count)
    subtotal_after_group_discount = subtotal - group_discount

    special_discount = calculate_special_offer_discount(subtotal_after_group_discount)
    subtotal_after_special_discount = subtotal_after_group_discount - special_discount

    premium_surcharge = calculate_premium_surcharge(
        subtotal_after_special_discount,
        features,
    )

    total = calculate_membership_total(
        plan=plan,
        features=features,
        confirmed=True,
    )

    selected_features = []

    for feature in features:
        selected_features.append(ADDITIONAL_FEATURES[feature]["name"])

    return {
        "valid": True,
        "plan": MEMBERSHIP_PLANS[plan]["name"],
        "features": selected_features,
        "members_count": members_count,
        "base_cost": base_cost,
        "features_cost": features_cost,
        "group_discount": round(group_discount, 2),
        "special_discount": round(special_discount, 2),
        "premium_surcharge": round(premium_surcharge, 2),
        "total": total,
    }