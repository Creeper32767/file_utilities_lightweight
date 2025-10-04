# File Utilities for Python

<div align="center">

A Python library providing a collection of helper classes and functions to streamline common operations with dictionaries, JSON, XLSX files, and logging.

[![PyPI version](https://badge.fury.io/py/file_utilities_lightweight.svg)](https://badge.fury.io/py/file_utilities_lightweight)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Creeper32767/file_utilities/pulls)

</div>

## About The Project

`file_utilities_lightweight` is designed to reduce boilerplate code when performing repetitive tasks. Whether you're handling configuration files, processing Excel data, or setting up a quick logger, this library offers simple, easy-to-use tools to get the job done faster.

### Key Features

*   **Dictionary Utilities:** Helper functions for common dictionary manipulations.
*   **JSON Handling:** A robust `BaseJsonOperator` for reading/writing JSON, plus a specialized class for managing internationalization (i18n) files.
*   **XLSX Operations:** Easily read from and write to Excel `.xlsx` files with minimal code.
*   **Simplified Logging:** A convenient wrapper to quickly set up a standard file and console logger.

## Installation

Install `file_utilities_lightweight` directly from PyPI:

```sh
pip install file_utilities_lightweight
```

### Requirements

*   Python 3.x
*   [openpyxl](https://openpyxl.readthedocs.io/en/stable/) (installed automatically as a dependency)

## Usage & API Overview

Here are some quick examples of how to use the modules in this library.

### `dict_utils`

Perform common lookups in dictionaries.

```python
from file_utilities_lightweight import dict_utils

my_dict = {'user_id': 101, 'name': 'admin', 'role': 'admin'}

# Get the first key that has the value 'admin'
key = dict_utils.get_key_by_value(my_dict, 'admin')
print(f"Key for value 'admin': {key}")
# > Key for value 'admin': name
```

### `json_utils`

Easily read from and write to `.json` files.

```python
from file_utilities_lightweight import json_utils

# Create a JSON operator for 'config.json'
json_op = json_utils.BaseJsonOperator('config.json')

# Write data to the file
default_config = {'theme': 'dark', 'version': '1.0'}
json_op.write_json(default_config)

# Read data from the file
config = json_op.read_json()
print(f"Theme from config: {config.get('theme')}")
# > Theme from config: dark
```

### ...and more

## Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

Don't forget to give the project a star! Thanks!

## License

Distributed under the MIT License. See `LICENSE` for more information.

Copyright © 2025 by Creeper32767

## Contact

Creeper32767 - [@Creeper32767](https://github.com/Creeper32767)

Project Link: [https://github.com/Creeper32767/file_utilities_lightweight](https://github.com/Creeper32767/file_utilities_lightweight)
