# Bing Apis SDK for Python


This repository is for active development of the Bing Apis SDK for Python. For consumers of the SDK we recommend visiting our [public developer docs](https://docs.microsoft.com/en-us/bing/search-apis/).

## Getting started

To get started with a specific library, see the `README.md` file located in the library's project folder.

You can find service libraries in the `/sdk` directory.

### Prerequisites

* Python 2.7, or 3.5 or later is required to use this package.
* [Bing Apis Account](https://aka.ms/bingapisignup).


### Install the packages 

You can find all dependencies in requirements.txt
* [Autosuggest](https://pypi.org/project/microsoft-bing-autosuggest/).
* [Custom Image Search](https://pypi.org/project/microsoft-bing-customimagesearch/).
* [Custom Web Search](https://pypi.org/project/microsoft-bing-customwebsearch/).
* [Entity Search](https://pypi.org/project/microsoft-bing-entitysearch/).
* [Image Search](https://pypi.org/project/microsoft-bing-imagesearch/).
* [News Search](https://pypi.org/project/microsoft-bing-newssearch/).
* [Spell Check](https://pypi.org/project/microsoft-bing-spellcheck/).
* [Video Search](https://pypi.org/project/microsoft-bing-videosearch/).
* [Visual Search](https://pypi.org/project/microsoft-bing-visualsearch/).
* [Web Search](https://pypi.org/project/microsoft-bing-websearch/).
* required packages: "msrest>=0.5.0", "msrestazure>=0.4.32,<2.0.0", "azure-common~=1.1"

### Running tests
First execute the following command from the root level of the repo:
```bash
pip install -r ./tests/test-requirements.txt
```

Then run pytest by simply typing it into your CLI:
```bash
pytest
```

## Need help?

* For detailed documentation visit our [Bing Apis for documentation](https://docs.microsoft.com/en-us/bing/search-apis/)
* File an issue via [Github Issues](https://github.com/microsoft/bing-search-sdk-for-python/issues)



## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
