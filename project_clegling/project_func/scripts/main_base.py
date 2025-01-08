#!/usr/bin/env python3
import project_func.cli as cli

if __name__ == "__main__":
    print("Первая попытка запустить проект!")

    cli.show_help()
    cli.parse_cmd()
