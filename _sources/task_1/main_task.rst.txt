=========
Main Task
=========

------------
Fix the bugs
------------

On the last line of ``mandelbrot.py`` there is a commented-out line with ``plt.show()``.
Un-comment this and run the script.
You should see a rather boring figure appear which looks nothing like a fractal.
It seems we may have a bug...

Comment the ``plt.show()`` statement out again.

In the file ``test_utils.py`` there are some unit tests, which test some of the functions used to generate the fractal image.
A test fails if one of the conditions in the ``assert`` statements is ``False``.

Into your Conda environment, install the ``pytest`` package, and update your ``environment.yml`` file.
Inside the ``task-1`` directory, run the command ``pytest``.
You should find that there are test failures.

By inspecting the traceback provided by pytest, see if you can spot the bug.
Hint: it's a typo which affects the mathematical operations!

Once you've fixed the bug and the tests are all passing, uncomment the ``plt.show()`` statement.
The output should look rather more interesting than previously!

Commit your changes and push to Github.

-------------------
Open a pull request
-------------------

Now that things are actually working, let's be bold and state our intentions to merge our changes into the ``main`` branch.
Github provides a nice way to do this called a 'pull request' (PR).

Go to your repository on the Github website.
TODO: there's a setting which enables workflows on forks. Activate it.

On Github, create a PR to merge ``task-1`` into ``main``.
Give your PR a sensible title.
**Do not merge the PR**.

You should see that a Github 'workflow' starts to run, and that it fails pretty quickly.
Click on the workflow to see what went wrong.

-------------
Get Organised
-------------

Shoving everything in one ``.py`` file is not a scalable approach to writing code.
It's far better to adopt a **modular** structure where independent components are logically organised into packages and modules.

----------------
Create a package
----------------

----------------
Catch bad inputs
----------------

Assert statement if too many pixels
Warn user that file being overridden

----------------
Type annotations
----------------

