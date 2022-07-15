def pytest_terminal_summary(terminalreporter, exitstatus, config):
    try:
        passed = len(terminalreporter.stats["passed"])
    except KeyError:
        passed = 0

    try:
        failed = len(terminalreporter.stats["failed"])
    except KeyError:
        failed = 0

    total = passed + failed

    summary = f"*    Total score: {passed}/{total}    *"
    banner = "".join(["*" for _ in summary])
    print(
        f"""

        {banner}
        {summary}
        {banner}

    """
    )

    if not failed:
        print("    Congratulations! :)")
