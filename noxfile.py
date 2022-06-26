import pathlib
import nox

nox.options.sessions = []
nox.options.default_venv_backend = "conda"
nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session):
    session.conda_install("black")
    session.conda_install("flake8")
    # Hmm not sure if I want to use a pyproject
    # session.run("black", ".")
    session.run("flake8", ".")


@nox.session
def pages(session):

    root = pathlib.Path(__file__).parent
    source = str(root / "pages" / "source")
    package = str(root / "workshop")
    html = str(root / "pages" / "_build" / "html")
    index = str(root / "pages" / "_build" / "html" / "index.html")

    session.conda_install("sphinx", channel="anaconda")
    session.conda_install("cloud_sptheme", channel="conda-forge")

    # Maybe I don't use apidoc
    #session.run("sphinx-apidoc", "-o", source, package, "--no-toc", "--force")
    session.run("sphinx-build", source, html, "--color", "-b" "html")
