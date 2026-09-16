from pathlib import Path
import argparse
import re


# Files are joined in this exact order.
FILES = [
    "business_term_Fiscal_and_School_Year_Calendar.md",
    "business_term_Account.md",
    "business_term_LCom_Customer.md",
    "business_term_Contact.md",
    "business_term_CSM.md",
    "business_term_Opportunity.md",
    "business_term_Opportunity_Line_Item_Deal.md",
    "business_term_booking_revenue_ARR_NRR.md",
    "business_term_Churn.md",
    "business_term_Product.md",
    "business_term_License_Order.md",
    "business_term_License_Provisioning_Metrics.md",
    "business_term_User.md",
    "business_term_Enrollment.md",
    "business_term_Usage.md",
    "business_term_Usage_Metrics.md",
    "business_term_Training_Session.md",
    "business_term_Case.md",
]

OUTPUT_FILE = "business_glossary.md"


def get_first_heading(content: str) -> str:
    """Return the first Markdown heading from the file."""
    for line in content.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            return match.group(1)

    raise ValueError("No Markdown heading found.")


def markdown_anchor(heading: str) -> str:
    """Convert a Markdown heading to a GitHub-style anchor."""
    anchor = heading.lower()

    # Remove Markdown formatting characters.
    anchor = re.sub(r"[*_`]", "", anchor)

    # Remove punctuation except spaces and hyphens.
    anchor = re.sub(r"[^\w\s-]", "", anchor)

    # Convert whitespace to hyphens.
    anchor = re.sub(r"\s+", "-", anchor)

    # Remove repeated hyphens.
    anchor = re.sub(r"-+", "-", anchor)

    return anchor.strip("-")


def create_business_glossary(input_path: str) -> Path:
    input_dir = Path(input_path)
    output_path = input_dir / OUTPUT_FILE

    if not input_dir.is_dir():
        raise NotADirectoryError(
            f"Directory does not exist: {input_dir}"
        )

    sections = []
    contents = []

    for filename in FILES:
        file_path = input_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Missing file: {file_path}"
            )

        content = file_path.read_text(
            encoding="utf-8"
        ).strip()

        heading = get_first_heading(content)
        anchor = markdown_anchor(heading)

        contents.append(
            f"- [{heading}](#{anchor})"
        )

        # Add navigation link at the end of each business term.
        section = (
            content
            + "\n\n"
            + "[↑ Back to Contents](#contents)"
        )

        sections.append(section)

    # Create the Contents section.
    table_of_contents = (
        "# Business Glossary\n\n"
        "## Contents\n\n"
        + "\n".join(contents)
    )

    # Combine Contents and all business glossary terms.
    combined_content = (
        table_of_contents
        + "\n\n---\n\n"
        + "\n\n---\n\n".join(sections)
        + "\n"
    )

    output_path.write_text(
        combined_content,
        encoding="utf-8"
    )

    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Combine business glossary Markdown files "
            "into one file."
        )
    )

    parser.add_argument(
        "path",
        help=(
            "Path to the directory containing the "
            "business glossary Markdown files."
        ),
    )

    args = parser.parse_args()

    output = create_business_glossary(args.path)

    print(f"Created: {output}")