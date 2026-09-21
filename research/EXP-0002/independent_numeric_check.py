"""Read-only independent EXP-0002 point-score check; no refitting or new evidence."""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parent
read = lambda name: json.loads((ROOT / name).read_text(encoding="utf-8-sig"))
events = read("prepared-events.json")
fit = read("fit-lock.json")
results = read("results.json")
assert fit["config"] == results["config"] == [1, 1.5, 0.5]
c, s, w = fit["config"]
cdf = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
rows = []
for event in events:
    raw = [float(x) for x in event["b"]]
    outcome = [float(x) for x in event["y"]]
    count = len(raw)
    assert count == len(outcome) == len(event["intervals"]) and count > 0
    mass = math.fsum(raw)
    market = [x / mass for x in raw]
    weather = []
    for lower, upper in event["intervals"]:
        lower = -math.inf if lower is None else float(lower) - 0.5
        upper = math.inf if upper is None else float(upper) + 0.5
        weather.append(cdf((upper - event["mos_forecast"] - c) / s) - cdf((lower - event["mos_forecast"] - c) / s))
    candidate = [(1 - w) * a + w * b for a, b in zip(market, weather)]
    loss = lambda forecast: math.fsum((a - b) ** 2 for a, b in zip(forecast, outcome)) / count
    values = {"split": event["split"], "raw": loss(raw), "market": loss(market), "candidate": loss(candidate), "uniform": loss([1 / count] * count)}
    values["gain"] = values["market"] - values["candidate"]
    rows.append(values)
maximum = 0.0
summary = []
for split in ["train", "validation", "test_a", "test_b", "test_pooled"]:
    selected = [row for row in rows if row["split"] == split or (split == "test_pooled" and row["split"] in ["test_a", "test_b"])]
    assert len(selected) == results["splits"][split]["eligible"]
    output = {"split": split, "eligible_events": len(selected)}
    for metric in ["raw", "market", "candidate", "uniform", "gain"]:
        value = math.fsum(row[metric] for row in selected) / len(selected)
        difference = abs(value - results["splits"][split][metric])
        assert difference <= 1e-12, (split, metric, difference)
        maximum = max(maximum, difference)
        output[metric] = value
        if split in ["train", "validation"] and metric != "gain":
            difference = abs(value - fit[split + "_scores"][metric])
            assert difference <= 1e-12, (split, metric, difference)
            maximum = max(maximum, difference)
    summary.append(output)
print(json.dumps({"status": "PASSED", "maximum_absolute_difference": maximum, "tolerance": 1e-12, "no_refit_or_new_filters": True, "writes_files": False, "splits": summary}, indent=2))
