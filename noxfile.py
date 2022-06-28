import nox


@nox.session
def test(session):
    session.install(".")
    session.install("pytest")
    session.run("pytest", "-k", "not grade")


@nox.session
def grade(session):
    session.install(".")
    session.install("pytest")
    session.run("pytest", "-k", "grade")


@nox.session(reuse_venv=True)
def lint(session):
    session.install("black")
    session.install("flake8")
    session.run("black", ".")
    session.run("flake8", ".")
