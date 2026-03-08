# generators/metrics_generator.py
import os
import re
from bs4 import BeautifulSoup  # pip install beautifulsoup4

def calculate_metrics(ticket_id: str):
    """
    Calculates advanced metrics:
    - Number of test cases generated
    - Number of BDD scenarios
    - Self-healing actions applied (based on log/HTML report)
    """
    output_dir = os.path.join("output", ticket_id)

    # 1. Count test cases in CSV
    test_cases_file = os.path.join(output_dir, "test_cases.csv")
    if os.path.exists(test_cases_file):
        with open(test_cases_file, "r", encoding="utf-8") as f:
            test_case_count = sum(1 for line in f) - 1  # exclude header
    else:
        test_case_count = 0

    # 2. Count BDD scenarios
    bdd_file = os.path.join(output_dir, "feature.feature")
    if os.path.exists(bdd_file):
        with open(bdd_file, "r", encoding="utf-8") as f:
            bdd_scenarios = len([line for line in f if line.strip().lower().startswith("scenario")])
    else:
        bdd_scenarios = 0

    # 3. Self-healing actions from HTML report
    report_file = os.path.join(output_dir, "test_report.html")
    self_healing_count = 0
    if os.path.exists(report_file):
        with open(report_file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            # Assuming self-healing logs have "self-healed" keyword
            self_healing_count = len(soup(text=re.compile(r"self-healed", re.I)))

    metrics = {
        "test_cases_generated": test_case_count,
        "bdd_scenarios": bdd_scenarios,
        "self_healing_applied": self_healing_count
    }

    # Save metrics to a file
    metrics_file = os.path.join(output_dir, "metrics_summary.txt")
    with open(metrics_file, "w", encoding="utf-8") as f:
        for k, v in metrics.items():
            f.write(f"{k}: {v}\n")

    print(f"Advanced metrics saved to: {metrics_file}")
    return metrics