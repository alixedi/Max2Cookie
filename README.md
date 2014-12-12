Max2Cookie
==========

A rather daft little script that creates a [cookiecutter](https://github.com/audreyr/cookiecutter) template from a MaxCompiler project. Cookiecutter is a Python utility for bootstrapping projects from templates. The process of creating a project can be interactive or automatic. Project templates can be hosted on Github.


Usage
-----

There are 3 steps to use this tool:

1. Create a MaxCompiler project using the MaxIDE. You have to work hard for the good stuff you know! Go on - fill up the forms and push those buttons. Please do not forget to note down the project name as well as the stem name.

2. Copy the project folder to the current working directory - this is important-ish depending on how you have set up things. A word of warning though: the script works *in-place*!

3. Unleash the hounds! They are called grep and sed.

    $ python max2cookie.py <project_name> <stem_name>

4. Create your first project:

    $ cd..

    $ cookiecutter Max2Cookie


To-do
-----

* I have only tested this with the basic CPUStream template. I will get back to actively testing for all other types of projects after new year.

* This can be in the standard PyPI packaging format so that it can be installed simply by:

    $ pip install Max2Cookie

* Compare the project creation logic with the project creation logic in the MaxIDE.
