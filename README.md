# Core File Generator Library

## Overview

This is a reusable library for generating different types of files such as PowerPoint presentations (PPTX) and Excel files. It is intended to be used in different projects, where specific use cases require the generation of such files.

## Features

- Generate PowerPoint presentations from structured data.
- Generate Excel files from structured data.
- Input validation for both text and file uploads.
  
## Installation

To install the core library, clone the repository and run:

```bash
pip install -e .
```

## Usage
Example usage for generating a PowerPoint presentation:

```python

from core.file_generator import generate_pptx

slides_data = [{'title': 'Slide 1', 'content': 'Slide content.'}]
pptx_file = generate_pptx(slides_data)
```

## Environment Variables

The following environment variables are used by this library:

- MAX_FILE_SIZE: Defines the maximum size of uploaded files.
- DEFAULT_TEMPLATE_PATH: Path to default templates for file generation.

## Running Tests

To run the tests, use:

```bash
pytest
```
