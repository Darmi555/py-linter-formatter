def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": point["line_number"],
                "column": point["column_number"],
                "message": point["text"],
                "name": point["code"],
                "source": "flake8"
            } for point in errors
        ],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": point["line_number"],
                    "column": point["column_number"],
                    "message": point["text"],
                    "name": point["code"],
                    "source": "flake8"
                }
                for point in linter_report[src]
            ] if linter_report[src] else [],
            "path": src,
            "status": "passed" if len(linter_report[src]) == 0 else "failed"
        }
        for src in linter_report
    ]
