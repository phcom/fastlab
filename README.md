# FastLAB

## Description

[Provide a brief description of your project here]

## Prerequisites

This project requires Python 3.8 or later. To prevent any problems with the python version, we'll all be using Python 3.12. You can download it from [here](https://www.python.org/downloads/).

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/phcom/fastlab.git
    ```

2. Navigate to the project directory:
    ```
    cd fastlab
    ```

3. Create a virtual environment:
    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```
        source venv/bin/activate
        ```

5. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Documentation

For more information about Python, you can visit the [Python documentation](https://docs.python.org/3/).

For more information about FastAPI, you can visit the [FastAPI documentation](https://fastapi.tiangolo.com/).

## Usage

To run the project, use the following command:

```bash
python -m app
```

## Contributing

We welcome contributions from everyone. Here are some guidelines to follow:

1. Always create a new branch for each user story from the `dev` branch. Never commit directly to the `dev` or `main` branches.

2. Use descriptive commit messages with tags to indicate the type of changes made. For example, use `[Feat]` for new features, `[Fix]` for bug fixes, `[Refactor]` for code refactoring, etc.

3. Before creating a pull request, ensure your feature branch is up-to-date with the latest changes from `dev`.

4. Create a pull request to merge your feature branch into `dev`, not `main`.

5. Remember to always update the requirements.txt file if you add or update any packages.

6. If working with another developer, add him as a co-author in the commit message.

By following these guidelines, we can maintain a clean, manageable project structure and history.

## License

This is a private project. All rights are reserved by the project owner. Unauthorized distribution, modification, or use without explicit permission from the project owner is strictly prohibited.