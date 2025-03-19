# Tic-Tac-Toe

## Installation

### With `pip`:

1. Ensure `pip` is installed.

2. Create a virtual environment:

    ```sh
    # Windows
    python -m venv .venv
    .venv/Scripts/activate
    ```

    ```sh
    # Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. For development, clone and install the repository in editable mode:

    ```sh
    git clone <repo-url> .
    pip install . -e
    ```

    Otherwise, you can install directly from the repository:

    ```sh
    pip install git+<repo-url>
    ```

### With `uv`:

1. Install the `uv` package manager by following the instructions [here](https://docs.astral.sh/uv/getting-started/installation/).

2. For development, clone and install the repository:

    ```sh
    git clone <repo-url> .
    uv sync
    ```

    For regular installation, run:

    ```sh
    uv add git+<repo-url>
    ```

## Usage

You can start the game using either command:

```sh
tic-tac-toe
```

`uv` users can use this single command to create a virtual environment, install the package, and launch the game:

```sh
uv run tic-tac-toe
```
