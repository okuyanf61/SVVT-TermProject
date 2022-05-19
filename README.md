[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs) [![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Python Version](https://img.shields.io/pypi/pyversions/wemake-python-styleguide.svg)](https://pypi.org/project/wemake-python-styleguide/) [![WPS](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide) [![Lint Status](https://github.com/pycqa/isort/workflows/Lint/badge.svg?branch=develop)](https://github.com/pycqa/isort/actions?query=workflow%3ALint) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) [![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](http://mypy-lang.org/) 

![Logo](https://playwright.dev/img/playwright-logo.svg)
# CENG 4502 Software Validation Verification and Testing - Term Project

In this project, Playwright was used to create a test automation for the sahibinden.com website.

## Roadmap

The tasks were as follows:
    
- Create a dummy user profile. 
- Make a search which does enable less than 100 results.
- Save the search. 
- Sort the search list. 
- Calculate and represent the average prices DAILY.

## Run Locally

Clone the project

```bash
  git clone https://github.com/okuyanf61/SVVT-TermProject.git
```

Go to the project directory

```bash
  cd SVVT-TermProject
```

Install poetry (osx / linux / bashonwindows)

```bash
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Install poetry (windows powershell)

```bash
  (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

Install dependencies

```bash
  poetry install
```

Activate poetry shell

```bash
  poetry shell
```

Install playwright binaries

```bash
  playwright install
```

Run project

```bash
  poetry run python svvt/main.py
```


## Screenshots

![App Demo](/assets/demo.gif)


## Related Project

[Playwright](https://github.com/microsoft/playwright)


## License

[MIT](https://choosealicense.com/licenses/mit/)

