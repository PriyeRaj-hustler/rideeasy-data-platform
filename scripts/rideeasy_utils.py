import csv

def read_csv(filepath):
    """Read CSV and return list of dict"""
    try:
        with open(filepath, "r", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"[RideEasy] File not found: {filepath}")
        return []


def validate_not_null(data, column):
    """Check null values"""
    null_count = sum(
        1 for row in data
        if row.get(column) is None or row.get(column) == ""
    )

    return {
        "column": column,
        "null_count": null_count,
        "valid": null_count == 0
    }


def count_duplicates(data, key_column):
    """Count duplicates"""
    values = [row[key_column] for row in data]
    return len(values) - len(set(values))


def log_summary(table_name, row_count, null_report, dup_count):
    """Print summary"""
    print(
        f"[RideEasy] {table_name} | rows:{row_count} "
        f"| nulls:{null_report['null_count']} "
        f"| duplicates:{dup_count}"
    )


if __name__ == "__main__":
    data = read_csv("data/rides.csv")
    nulls = validate_not_null(data, "ride_id")
    dups = count_duplicates(data, "ride_id")

    log_summary("rides", len(data), nulls, dups)