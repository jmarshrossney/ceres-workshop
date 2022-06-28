import pathlib
import nox

nox.options.sessions = []
# nox.options.reuse_existing_virtualenvs = True


@nox.session
def test(session):
    session.install(".")
    session.install("pytest")
    session.run("pytest", "-s")


@nox.session(reuse_venv=True)
def lint(session):
    session.install("black")
    session.install("flake8")
    session.run("black", ".")
    session.run("flake8", ".")


@nox.session(reuse_venv=True)
def docs(session):
    root = pathlib.Path(__file__).parent
    source = str(root / "docs" / "source")
    html = str(root / "docs" / "_build" / "html")

    session.install("sphinx")
    session.install("cloud_sptheme")

    session.run("sphinx-build", source, html, "--color", "-b" "html")
