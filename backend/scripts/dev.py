#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import venv
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parents[1]
VENV_DIR = BACKEND_DIR / ".venv"


def venv_python() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def run(command: list[str], *, cwd: Path = BACKEND_DIR) -> None:
    raise SystemExit(subprocess.call(command, cwd=cwd))


def install() -> None:
    venv.EnvBuilder(with_pip=True, clear=False).create(VENV_DIR)
    run([str(venv_python()), "-m", "pip", "install", "-r", "requirements-dev.txt"])


def command_python() -> str:
    python = venv_python()
    if python.exists():
        return str(python)
    return sys.executable


def main() -> None:
    parser = argparse.ArgumentParser(description="Comunity backend development tasks")
    subcommands = parser.add_subparsers(dest="command", required=True)

    subcommands.add_parser("install", help="Create .venv and install dev dependencies")
    subcommands.add_parser("run", help="Run the local FastAPI server on port 5000")
    subcommands.add_parser("test", help="Run pytest")
    subcommands.add_parser("lint", help="Run ruff")
    subcommands.add_parser("check", help="Run tests, lint, and render Alembic SQL")
    subcommands.add_parser("migrate", help="Apply Alembic migrations to DATABASE_URL")
    subcommands.add_parser("migration-sql", help="Render Alembic migration SQL without applying it")

    args = parser.parse_args()
    python = command_python()

    if args.command == "install":
        install()
    elif args.command == "run":
        run(
            [
                python,
                "-m",
                "uvicorn",
                "app.main:app",
                "--reload",
                "--host",
                "0.0.0.0",
                "--port",
                "5000",
            ]
        )
    elif args.command == "test":
        run([python, "-m", "pytest"])
    elif args.command == "lint":
        run([python, "-m", "ruff", "check", "."])
    elif args.command == "check":
        for command in (
            [python, "-m", "pytest"],
            [python, "-m", "ruff", "check", "."],
            [python, "-m", "alembic", "upgrade", "head", "--sql"],
        ):
            result = subprocess.call(command, cwd=BACKEND_DIR)
            if result != 0:
                raise SystemExit(result)
    elif args.command == "migrate":
        run([python, "-m", "alembic", "upgrade", "head"])
    elif args.command == "migration-sql":
        run([python, "-m", "alembic", "upgrade", "head", "--sql"])


if __name__ == "__main__":
    main()
