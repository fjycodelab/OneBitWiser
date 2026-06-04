"""Show that stable sorts can compose a multi-key ordering."""

records = [
    {"name": "ada", "team": "blue", "score": 90},
    {"name": "alan", "team": "red", "score": 95},
    {"name": "grace", "team": "blue", "score": 80},
    {"name": "linus", "team": "blue", "score": 90},
    {"name": "barbara", "team": "red", "score": 80},
]


def label(record):
    return f"{record['team']}:{record['score']}:{record['name']}"


def main():
    tuple_key_order = sorted(
        records,
        key=lambda record: (record["team"], -record["score"]),
    )

    score_order = sorted(records, key=lambda record: record["score"], reverse=True)
    stable_two_pass_order = sorted(score_order, key=lambda record: record["team"])

    assert stable_two_pass_order == tuple_key_order
    assert [record["name"] for record in stable_two_pass_order[:2]] == ["ada", "linus"]

    print(", ".join(label(record) for record in stable_two_pass_order))


if __name__ == "__main__":
    main()
