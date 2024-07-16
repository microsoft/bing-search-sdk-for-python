<!-- Copyright (c) Microsoft Corporation.
 Licensed under the MIT License. -->
# Bing APIs SDK for Python

This repository is for active development of the Bing APIs SDK for Python. For consumers of the SDK we recommend visiting our [public developer docs](https://learn.microsoft.com/en-us/bing/search-apis/)

## Table of Contents

- [Bing APIs SDK for Python](#bing-apis-sdk-for-python)
  - [Features](#features)
    - [PyPi Packages](#pypi-packages)
  - [Getting started](#getting-started)
    - [Structure](#structure)
    - [Prerequisites](#prerequisites)
    - [Requiremnts](#requiremnts)
    - [Running Samples](#running-samples)
    - [Running Tests](#running-tests)
  - [Need help?](#need-help)
  - [Contributing](#contributing)
  - [Resources](#resources)
  - [Related Projects](#related-projects)
  - [Code of Conduct](#code-of-conduct)
  - [Trademarks](#trademarks)
  - [License](#license)
  - [Security](#security)

## Features

This project includes the following Bing-Search-APIs Python components:

- REST API [samples](./samples/rest/) and [tests](./tests/rest/)
- SDK [Implementation](./sdk/)
- SDK [Samples](./samples/sdk/)

It also contains CI/CD actions for test and deployment

This repo is actively maintained and issues / PRs are regularly looked-on

### PyPi Packages

This repo contains the implementations for the following packages

- [Autosuggest](https://pypi.org/project/microsoft-bing-autosuggest/)
- [Custom Image Search](https://pypi.org/project/microsoft-bing-customimagesearch/)
- [Custom Web Search](https://pypi.org/project/microsoft-bing-customwebsearch/)
- [Entity Search](https://pypi.org/project/microsoft-bing-entitysearch/)
- [Image Search](https://pypi.org/project/microsoft-bing-imagesearch/)
- [News Search](https://pypi.org/project/microsoft-bing-newssearch/)
- [Spell Check](https://pypi.org/project/microsoft-bing-spellcheck/)
- [Video Search](https://pypi.org/project/microsoft-bing-videosearch/)
- [Visual Search](https://pypi.org/project/microsoft-bing-visualsearch/)
- [Web Search](https://pypi.org/project/microsoft-bing-websearch/)

## Getting started

To get started with a specific library, see the `README.md` file located in the library's project folder

You can find service libraries in the `/sdk` directory

### Structure

| Directory (click to navigate)                      | Description                                    |
|----------------------------------------------------|------------------------------------------------|
| [`samples/`](./samples/)                           | Directory containing all the code samples      |
| [`samples/rest/`](./samples/rest/)                 | Directory containing all the REST code samples |
| [`samples/sdk/`](./samples/sdk/)                   | Directory containing all the SDK code samples  |
| [`sdk/`](./sdk/)                                   | Directory containing the SDK libraries         |
| [`sdk/Autosuggest`](./sdk/Autosuggest)             | Autosuggest SDK library                        |
| [`sdk/CustomImageSearch`](./sdk/CustomImageSearch) | Custom Image Search SDK library                |
| [`sdk/CustomWebSearch`](./sdk/CustomWebSearch)     | Custom Web Search SDK library                  |
| [`sdk/EntitySearch`](./sdk/EntitySearch)           | Entity Search SDK library                      |
| [`sdk/ImageSearch`](./sdk/ImageSearch)             | Image Search SDK library                       |
| [`sdk/NewsSearch`](./sdk/NewsSearch)               | News Search SDK library                        |
| [`sdk/SpellCheck`](./sdk/SpellCheck)               | Spell Check SDK library                        |
| [`sdk/VideoSearch`](./sdk/VideoSearch)             | Video Search SDK library                       |
| [`sdk/VisualSearch`](./sdk/VisualSearch)           | Visual Search SDK library                      |
| [`sdk/WebSearch`](./sdk/WebSearch)                 | Web Search SDK library                         |
| [`tests/`](./tests/)                               | Directory containing all the tests             |
| [`tests/rest`](./tests/rest)                       | Directory containing tests for REST samples    |

### Prerequisites

- Python 2.7, or 3.5 or later is required to use this package
- [Bing APIs Resouce on Azure](https://aka.ms/bingapisignup)
  - Create a `.env` file using `.env.example` as reference and fill it using your aquired credentials

### Requiremnts

See [requirements.txt](./requirements.txt)

### Running Samples

1. Clone the repo
2. (Optional) Create your virtual environment
3. Install dependencies

      ```shell
      pip install requirements.txt
      ```

4. Create a `.env` file and fill it using `.env.example` as guidance
5. Run the file you want

      ```shell
      python ./samples/rest/*.py
      ```

### Running Tests

1. Clone the repo
2. (*Optional*) Create a virtual environment
3. Install dependencies, e.g.:

      ```shell
      pip install requirements.txt
      pip install tests/test-requirements.txt
      ```

4. Create a `.env` file and fill it using `.env.example` as guidance
5. Run all the tests:

      ```shell
      pytest
      ```

## Need help?

See [Support](./SUPPORT.md)

## Contributing

See [Contributing guide](./CONTRIBUTING.md)


## Resources

- [Bing APIs for documentation](https://docs.microsoft.com/en-us/bing/search-apis/)
- [Github Issues](https://github.com/microsoft/bing-search-sdk-for-python/issues)

## Related Projects

- [.NET SDK and Samples repo](https://github.com/microsoft/bing-search-sdk-for-net/)
- [Java SDK and Samples repo](https://github.com/microsoft/bing-search-sdk-for-java)

## Code of Conduct

See [Code of Conduct](./CODE_OF_CONDUCT.md)

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)

Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship
Any use of third-party trademarks or logos are subject to those third-party's policies

## License

See [LICENSE](./LICENSE)

## Security

See [Security](./SECURITY.md)
