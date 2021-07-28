import subprocess


message = "initial commit from gh:zehengl/cookiecutter-conda-script"

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", message])
