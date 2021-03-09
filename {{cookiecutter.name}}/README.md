<div align="center">
    <img src="{{cookiecutter.img}}" alt="logo" height="196">
</div>

# {{cookiecutter.name}}

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

{{cookiecutter.description}}

## Install

```cmd
conda env create -f environment.yml -p .\venv
```

To update the `environment.yml` file, use the command below

```cmd
conda env export --no-builds | findstr -v "prefix" > environment.yml
```

<hr>

<sup>

## Credits

</sup>
