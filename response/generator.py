from utils.law_loader import get_laws_for_crime
from response.templates import DISCLAIMER
from rules.safety_rules import sanitize

def generate_response(contexts, confidence):
    """
    Generate structured legal guidance based on identified contexts
    """

    lines = []

    for context in contexts:
        # Title
        lines.append(f"\n🔹 Identified Issue:")
        lines.append(context.replace("_", " ").title())

        # Applicable laws
        laws = get_laws_for_crime(context)
        if laws:
            lines.append("\nApplicable Indian laws and sections (commonly invoked):")
            for law in laws:
                lines.append(f"- {law['law']}")
                for sec, desc in law["sections"].items():
                    lines.append(f"  Section {sec}: {desc}")

        # Standard procedural steps
        lines.append("\nPrimary procedural steps generally followed:")
        lines.append("- Ensure immediate safety")
        lines.append("- Seek medical help if there is any injury")
        lines.append("- Preserve evidence such as messages, photos, or witnesses")
        lines.append("- Visit the nearest police station to lodge an FIR")
        lines.append("- Request a copy of the FIR for your records")

    # Low-confidence handling
    if confidence < 0.5:
        lines.append(
            "\nThe description is not fully clear. "
            "Providing additional details may help identify applicable laws more accurately."
        )

    # Mandatory disclaimer
    lines.append(f"\n⚠️ {DISCLAIMER}")

    return sanitize("\n".join(lines))
