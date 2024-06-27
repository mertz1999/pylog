# pylog

**pylog** is an open-source project designed to simplify logging within your code. It provides an easy-to-use logging mechanism that integrates seamlessly into your Python applications.

## Features

- **Easy Integration**: Quickly add logging to your projects.
- **Customizable**: Tailor the logging output to fit your needs.
- **Lightweight**: Minimal performance overhead.
- **Open Source**: Free to use and modify under the MIT license.

## Installation

To install pylog, use pip:

```bash
pip install pylog
```

# Usage

import easily and make an instance.

```python
from pylog import Logger
# Create a logger instance
logger = Logger(save=True)

# Log messages
logger.info('This is an info message')
logger.error('This is an error message')
logger.debug('This is a debug message')

```
