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

    print(f"Your grade is: {passed}/{total}")

    if not failed:
        print("Congratulations! :)")


"""
def pytest_sessionfinish(session, exitstatus):
    reporter = session.config.pluginmanager.get_plugin("terminalreporter")
    pprint.pprint(reporter)
"""
