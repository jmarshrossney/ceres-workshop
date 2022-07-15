import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8")


@nox.session(venv_backend="mamba")
def task_1(session):
    session.run(
        "mamba",
        "env",
        "update",
        "--prefix",
        session.virtualenv.location,
        "--file",
        "environment.yml",
        silent=True,
    )
    session.conda_install("pytest")
    session.conda_install("pytest-timeout")
    session.install(".", "--no-deps")

    session.run("pytest", "grading", "-s", "--tb=no")
