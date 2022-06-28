import pathlib
import nox

@nox.session(reuse_venv=True)
def pages(session):
    root = pathlib.Path(__file__).parent
    source = str(root / "pages")
    html = str(root / "pages" / "_build" / "html")

    session.install("sphinx")
    session.install("cloud_sptheme")

    session.run("sphinx-build", source, html, "--color", "-b" "html")
