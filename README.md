# FastLAB

## Description

FastLAB is a project that aims to provide a easy starting point for FastAPI projects. It includes a basic project structure, a Dockerfile, a Docker Compose file, and a Tortoise ORM integration. The project is designed to be a starting point for FastAPI projects, providing a basic structure that can be used as a template for new projects.

## Prerequisites

This project requires Python 3.8 or later. To prevent any problems with the python version, we'll all be using Python 3.12. You can download it from [here](https://www.python.org/downloads/).

### Recommended Tools

- [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [DBeaver Community](https://dbeaver.io/download/)
- [Git Kraken](https://www.gitkraken.com/download)

### Recommended VS Code Extensions

- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)

A more complete list of recommended extensions for Visual Studio Code can be found in the `.vscode/extensions.json` file.

> [!NOTE]
> Some of the recommended tools and extensions aren't free. You can get access to them by using your student email address and signing up for the [GitHub Student Developer Pack](https://education.github.com/pack).

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
    python -m venv venv
    ```

> [!IMPORTANT]
> The following step can throw an `Scripts Disabled`, if it happens during your instalation, don't panic, use the following command and proceed with the next steps. 
> ```powershell
>Set-ExecutionPolicy Unrestricted -Scope Process
>```
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

For more information about Docker, you can visit the [Docker documentation](https://docs.docker.com/).

For more information about Docker Compose, you can visit the [Docker Compose documentation](https://docs.docker.com/compose/).

For more information about Tortoise ORM, you can visit the [Tortoise ORM documentation](https://tortoise.github.io/).

## Usage

> [!WARNING]
> **Before** running the project, go to the `__main__.py` file and choose the run command that fits your case, commenting the other.

To run the project, use the following command:

```bash
python -m app
```

Or, if you have Docker installed, you can use the following command:

```bash
docker-compose up -d --build
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