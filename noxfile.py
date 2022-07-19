import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8")
