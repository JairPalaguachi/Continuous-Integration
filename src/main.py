"""Command-line interface for the Gym Membership Management System."""

from src.membership import (
    get_available_plans,
    get_available_features,
    generate_membership_summary,
    calculate_membership_total,
)


def display_membership_plans():
    """Display the available membership plans."""
    print("Available Membership Plans")
    print("--------------------------")

    plans = get_available_plans()

    for key, plan in plans.items():
        print(f"{key}: {plan['name']} - ${plan['cost']}")
        print("Benefits:")

        for benefit in plan["benefits"]:
            print(f"  - {benefit}")

        print()


def display_additional_features():
    """Display the available additional features."""
    print("Available Additional Features")
    print("-----------------------------")

    features = get_available_features()

    for key, feature in features.items():
        feature_type = "Premium Feature" if feature["premium"] else "Standard Feature"
        print(f"{key}: {feature['name']} - ${feature['cost']} ({feature_type})")

    print()


def get_user_features():
    """Read additional features entered by the user."""
    features_input = input(
        "Enter additional features separated by commas, or press Enter for none: "
    )

    if not features_input.strip():
        return []

    return [feature.strip().lower() for feature in features_input.split(",")]


def display_summary(summary):
    """Display the selected membership summary."""
    print()
    print("Membership Summary")
    print("------------------")
    print(f"Plan: {summary['plan']}")

    if summary["features"]:
        print(f"Additional features: {', '.join(summary['features'])}")
    else:
        print("Additional features: None")

    print(f"Members signing up together: {summary['members_count']}")
    print(f"Base cost: ${summary['base_cost']}")
    print(f"Additional features cost: ${summary['features_cost']}")
    print(f"Group discount: ${summary['group_discount']}")
    print(f"Special offer discount: ${summary['special_discount']}")
    print(f"Premium surcharge: ${summary['premium_surcharge']}")
    print(f"Total cost: ${summary['total']}")
    print()


def main():
    """Run the command-line membership application."""
    print("Gym Membership Management System")
    print("================================")
    print()

    display_membership_plans()
    display_additional_features()

    plan = input("Select a membership plan: ").strip().lower()
    features = get_user_features()

    try:
        members_count = int(input("Enter the number of members: "))
    except ValueError:
        print("Error: The number of members must be a positive integer.")
        print(-1)
        return

    summary = generate_membership_summary(
        plan=plan,
        features=features,
        members_count=members_count,
    )

    if not summary["valid"]:
        print(f"Error: {summary['message']}")
        print(-1)
        return

    if members_count >= 2:
        print("Notice: A 10% group discount can be applied.")

    display_summary(summary)

    confirmation = input("Do you want to confirm this membership? yes/no: ")
    confirmation = confirmation.strip().lower()

    if confirmation != "yes":
        print("Membership process canceled.")
        print(-1)
        return

    total = calculate_membership_total(
        plan=plan,
        features=features,
        members_count=members_count,
        confirmed=True,
    )

    print("Membership confirmed successfully.")
    print(total)


if __name__ == "__main__":
    main()