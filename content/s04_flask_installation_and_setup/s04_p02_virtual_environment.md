Once you have Python installed, it's time to set up a virtual environment. We won't cover what a virtual environment is here, but [this article](https://realpython.com/python-virtual-environments-a-primer/) is a great introduction on the subject. For this course, we'll be using the `venv` python module to create virtual environments.

If you aren't already there, go ahead and change your directory to your project folder:

```bash
cd /path/to/ragtime/
```

Then in the command line use Python to create your virtual environment:

```python
python3 -m venv env
```

The choice is yours in what to name your virtual environment folder. In this case I used the name `env`. Now all you'll need to do is "activate" the virtual environment. With your command line, just type the following:

```bash
source env/bin/activate
```

Note that you'll want to activate your virtual environment *every time you begin work on your project*.

At this point, you should be all set to start installing packages in your virtual environment.