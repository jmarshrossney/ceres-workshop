from functools import wraps
import os
import pathlib
import shutil
import subprocess

REPO_ROOT = pathlib.Path(__name__).resolve().parent.parent
TASKS_DIR = REPO_ROOT / "tasks"


def verbose(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sp = "    "
        fname = func.__name__.replace("_", " ").replace("test", "Test:")
        fname = sp + fname + sp
        banner = "".join(["=" for _ in fname])
        header = f"{banner}\n{fname}\n{banner}"
        print()
        print(header)
        print(func.__doc__)
        print()
        print(">>> Captured output >>>")
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print("<<< Captured output <<<")

            print()
            print(sp + "*** Failed *** ")
            print()
            print(exc)
            raise exc
        else:
            print("<<<")

            print()
            print(sp + "*** Passed! ***")

        return result

    return wrapper


class BadImport(Exception):
    pass


def check_import(module: str, timeout: float = 2):
    try:
        result = subprocess.run(
            [
                "python",
                "-c",
                f"import {module}",
            ],
            capture_output=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        raise BadImport(f"Importing `{module}` took too long! (>{timeout}s)")

    if result.stderr:
        raise BadImport(
            f"An error occurred while importing `{module}`:\n{result.stderr.decode()}"
        )
    if result.stdout:
        raise BadImport(
            f"Importing `{module}` resulted in things being printed to stdout"
        )


def check_file(*path: str):
    path = pathlib.Path(TASKS_DIR).joinpath(*path)
    if not path.exists():
        raise FileNotFoundError(f"No file found at `{path}`")
    elif path.is_dir():
        raise IsADirectoryError(f"`{path}` is a directory, but it should be a file")
    elif not path.is_file():
        raise Exception(f"`{path}` is neither a file nor a directory. Hmm...")


def check_dir(*path: str):
    path = pathlib.Path(TASKS_DIR).joinpath(*path)
    if not path.exists():
        raise FileNotFoundError(f"No file found at `{path}`")
    elif path.is_file():
        raise NotADirectoryError(f"`{path}` is a file, but it should be a directory")
    elif not path.is_dir():
        raise Exception(f"`{path}` is neither a file nor a directory. Hmm...")


class temp_dir:
    def __init__(self, name: str = "tmp"):
        self.tmp = pathlib.Path.cwd().joinpath(name)
        self.tmp.mkdir(exist_ok=False)

    def __enter__(self):
        self.cwd = pathlib.Path.cwd()
        os.chdir(self.tmp)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir(self.cwd)
        shutil.rmtree(self.tmp)
