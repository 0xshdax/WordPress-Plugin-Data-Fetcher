# WordPress Plugin Data Fetcher
The WordPress Plugin Data Fetcher is a Python script designed to interact with the WordPress.org API to gather information about various plugins. The tool provides a flexible way to filter and download plugins based on user-defined criteria, allowing for efficient management of plugins according to specific requirements.

## Usage
```
$ python3 main.py
usage: main.py [-h] [--active-install-min ACTIVE_INSTALL_MIN] [--active-install-max ACTIVE_INSTALL_MAX]
               [--last-updated-year-min LAST_UPDATED_YEAR_MIN] [-o OUTPUT_FOLDER]

WordPress Plugin Data Fetcher

options:
  -h, --help            show this help message and exit
  --active-install-min ACTIVE_INSTALL_MIN
                        Minimum active installs
  --active-install-max ACTIVE_INSTALL_MAX
                        Maximum active installs
  --last-updated-year-min LAST_UPDATED_YEAR_MIN
                        Minimum last updated year
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        Output folder for extracted plugin files
```
## Example
```
$ python3 main.py --active-install-min 1000 --active-install-max 50000 --last-updated-year-min 2023 -o output_folder
```
