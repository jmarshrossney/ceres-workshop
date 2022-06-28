import nox


@nox.session(venv_backend="mamba")
def grade(session):
    session.conda_install("conda-lock")
    session.run(
        "conda-lock",
        "render",
        "--kind",
        "env",
        "conda-lock.yml",
    )
    session.run(
        "mamba",
        "env",
        "update",
        "--file",
        "conda-linux-64.lock.yml",
    )
    session.install(".", "--no-deps")

    session.run("flake8")
    session.run("pytest")
    session.run("pytest", "grading")
