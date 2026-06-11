# Gym Membership Management System

Command-line application for managing gym memberships, calculating membership costs, applying discounts, validating user selections, and confirming or canceling membership plans.

This project was developed as part of a Continuous Integration workshop using **Jenkins**, **Ngrok**, **GitHub Actions**, **pytest**, and **pylint**.

## Project Description

The Gym Membership Management System allows users to:

* View available gym membership plans.
* Select a membership plan.
* Add optional features to the selected membership.
* Calculate the total membership cost.
* Apply group discounts.
* Apply special offer discounts.
* Apply premium feature surcharges.
* Validate selected plans and features.
* Confirm or cancel the membership process.
* Return the final cost as a positive integer when the plan is valid and confirmed.
* Return `-1` when the input is invalid or the plan is canceled.

## Membership Plans

| Plan    | Cost | Benefits                                                                                |
| ------- | ---: | --------------------------------------------------------------------------------------- |
| Basic   |  $50 | Access to gym equipment, locker room access, basic fitness assessment                   |
| Premium | $120 | Access to gym equipment, group classes, sauna access, monthly fitness assessment        |
| Family  | $180 | Access for family members, group classes, locker room access, family fitness activities |

## Additional Features

| Feature                      | Cost | Type     |
| ---------------------------- | ---: | -------- |
| Personal Training Sessions   |  $80 | Standard |
| Group Classes                |  $40 | Standard |
| Exclusive Gym Facilities     | $100 | Premium  |
| Specialized Training Program | $150 | Premium  |

## Discount Rules

The system applies the following rules:

* If two or more members sign up together, a **10% group discount** is applied.
* If the total cost exceeds **$200**, a **$20 discount** is applied.
* If the total cost exceeds **$400**, a **$50 discount** is applied.
* If the membership includes premium features, a **15% surcharge** is applied.

## Project Structure

```text
/
│
├── src/
│   ├── __init__.py
│   ├── membership.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_membership.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

* Python
* pytest
* pylint
* Jenkins
* Ngrok
* GitHub Actions
* Git
* GitHub

## Requirements

Before running the project, make sure you have installed:

* Python 3.12 or higher
* Git
* Jenkins
* Ngrok

Python dependencies are listed in `requirements.txt`.

## Installation

Clone the repository:

```bash
https://github.com/JairPalaguachi/Continuous-Integration.git
```

Enter the project folder, then install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

To start the command-line application, run:

```bash
python -m src.main.py
```

The application will display the available membership plans and additional features. Then, the user can select a plan, add features, enter the number of members, and confirm or cancel the membership.

## Run Unit Tests

To execute all unit tests, run:

```bash
pytest
```

## Generate Test Report for Jenkins

To generate a JUnit XML report that can be read by Jenkins, run:

```bash
pytest --junitxml=test-results.xml
```

This command creates a file named:

```text
test-results.xml
```

Jenkins uses this file to display test results and reports.

## Run Linting

To analyze the code quality with pylint, run:

```bash
pylint src tests
```

This command checks the source code and test files for style, syntax, and quality issues.


## GitHub Actions

GitHub Actions is used to run linting automatically when a pull request is opened toward the main branch.

Workflow file location:

```text
.github/workflows/ci.yml
```

The workflow runs when a pull request targets:

```text
main
master
```

It performs the following steps:

* Checks out the repository.
* Sets up Python.
* Installs dependencies.
* Runs pylint on the source code and tests.



## Expected Output

If the selected membership plan is valid and confirmed, the application returns the total cost as a positive integer.

Example:

```text
Membership confirmed successfully.
160
```

If the input is invalid or the membership is canceled, the application returns:

```text
-1
```

## Testing Strategy

The project includes unit tests for:

* Valid membership plans.
* Invalid membership plans.
* Valid additional features.
* Invalid additional features.
* Base membership cost calculation.
* Additional feature cost calculation.
* Group discount calculation.
* Special offer discount calculation.
* Premium surcharge calculation.
* Membership cancellation.
* Invalid member count.
* Membership summary generation.

## Continuous Integration

This project uses two continuous integration tools:

### Jenkins

Jenkins runs the unit tests automatically after changes are pushed to the repository. It also publishes the test results using the JUnit XML report generated by pytest.

### GitHub Actions

GitHub Actions runs pylint automatically when a pull request is opened toward the main branch. This helps detect code quality issues before merging changes.

## Repository URL

Add the repository URL here:

```text
https://github.com/JairPalaguachi/Continuous-Integration.git
```

## Authors

Developed by:

* Derian Baque
* Christopher Villon
* Dhamar Patino
* Gustavo Guzmán
* Jair Palaguachi

