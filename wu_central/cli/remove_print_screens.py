from pathlib import Path


def remove_print_screens(directory: Path) -> None:
    if not directory.is_dir():
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    for path in directory.iterdir():
        if path.is_file() or path.is_symlink():
            path.unlink()


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    remove_print_screens(project_root / "print_screens")
