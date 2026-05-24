from rich.console import Console
from rich.table import Table
from collections import defaultdict

console = Console()

def format_vulnerabilities(vulns):
    if not vulns:
        console.print("[bold red]No findings detected[/bold red]")
        return

    # ---------------------------
    # 1. SUMMARY CALCULATION
    # ---------------------------
    summary = defaultdict(int)

    for v in vulns:
        severity = v["severity"].lower()
        summary[severity] += 1

    total = len(vulns)

    # ---------------------------
    # 2. SUMMARY BLOCK
    # ---------------------------
    console.print("\n[bold cyan]VULNSCOPE SUMMARY[/bold cyan]\n")
    console.print(f"[bold]Total Findings:[/bold] {total}")
    console.print(f"[red]High:[/red] {summary.get('high', 0)}")
    console.print(f"[yellow]Medium:[/yellow] {summary.get('medium', 0)}")
    console.print(f"[green]Low:[/green] {summary.get('low', 0)}\n")

    # ---------------------------
    # 3. GROUPED OUTPUT
    # ---------------------------
    grouped = defaultdict(list)

    for v in vulns:
        grouped[v["severity"].lower()].append(v)

    order = ["high", "medium", "low"]

    for level in order:
        items = grouped.get(level, [])
        if not items:
            continue

        console.print(f"\n[bold]{level.upper()} SEVERITY[/bold]")

        table = Table(show_header=True, header_style="bold")
        table.add_column("Vulnerability")
        table.add_column("Description")

        for v in items:
            table.add_row(v["name"], v["description"])

        console.print(table)
