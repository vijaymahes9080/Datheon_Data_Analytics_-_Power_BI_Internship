"""Executive Reporting and Evidence-Driven Findings Register.

Part of RISK V3 - Autonomous Business Analytics & Decision Intelligence Engine.
Maintains structured findings registers conforming to the RISK methodology.
"""

from typing import List, Dict, Any, Optional
import os
import pandas as pd


class Finding:
    """Represents a single evidence-backed business finding."""

    def __init__(
        self,
        finding_id: str,
        business_question: str,
        metric: str,
        evidence: str,
        calculation: str,
        interpretation: str,
        action: str,
        limitation: str,
    ):
        self.finding_id = finding_id
        self.business_question = business_question
        self.metric = metric
        self.evidence = evidence
        self.calculation = calculation
        self.interpretation = interpretation
        self.action = action
        self.limitation = limitation

    def to_dict(self) -> Dict[str, str]:
        return {
            "ID": self.finding_id,
            "Business Question": self.business_question,
            "Metric": self.metric,
            "Evidence": self.evidence,
            "Calculation": self.calculation,
            "Interpretation": self.interpretation,
            "Action": self.action,
            "Limitation": self.limitation,
        }

    def to_markdown(self) -> str:
        return f"""### Finding {self.finding_id}: {self.business_question}

* **Metric Measured**: {self.metric}
* **Supporting Evidence**: {self.evidence}
* **Reproducible Calculation**: `{self.calculation}`
* **Business Interpretation**: {self.interpretation}
* **Strategic Recommendation**: {self.action}
* **Analytical Limitation**: {self.limitation}
"""


class FindingsRegister:
    """Registry maintaining all quantified findings across tasks."""

    def __init__(self, domain: str):
        self.domain = domain
        self.findings: List[Finding] = []

    def add_finding(self, finding: Finding) -> None:
        self.findings.append(finding)

    def to_markdown_table(self) -> str:
        if not self.findings:
            return "No findings registered."

        headers = ["ID", "Business Question", "Observed Metric", "Strategic Action"]
        rows = [
            f"| {f.finding_id} | {f.business_question} | {f.metric} | {f.action} |"
            for f in self.findings
        ]
        table_header = "| " + " | ".join(headers) + " |\n| " + " | ".join(["---"] * len(headers)) + " |"
        return table_header + "\n" + "\n".join(rows)

    def to_full_markdown(self) -> str:
        return "\n---\n".join([f.to_markdown() for f in self.findings])


def export_markdown_report(content: str, filepath: str) -> str:
    """Save formatted markdown report to designated path."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath
