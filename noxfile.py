import pathlib
import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8")


@nox.session
def pages(session):
    root = pathlib.Path(__file__).parent
    source = str(root / "pages")
    html = str(root / "pages" / "_build" / "html")

    session.install("sphinx")
    session.install("cloud_sptheme")
    session.install("pytest")

    session.run("sphinx-build", source, html, "--color", "-b" "html")
