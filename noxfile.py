import pathlib
import nox

nox.options.sessions = []
nox.options.reuse_existing_virtualenvs = True

# Seems like anaconda sphinx doesn't work on python 3.9
# nox.options.default_venv_backend = "conda"


@nox.session
def lint(session):
    session.install("black")
    session.install("flake8")
    # Hmm not sure if I want to use a pyproject
    # session.run("black", ".")
    session.run("flake8", ".")


@nox.session
def docs(session):

    root = pathlib.Path(__file__).parent
    source = str(root / "docs" / "source")
    package = str(root / "workshop")
    html = str(root / "docs" / "_build" / "html")
    index = str(root / "docs" / "_build" / "html" / "index.html")

    session.install("sphinx")
    session.install("cloud_sptheme")

    # Maybe I don't use apidoc
    # session.run("sphinx-apidoc", "-o", source, package, "--no-toc", "--force")
    session.run("sphinx-build", source, html, "--color", "-b" "html")
