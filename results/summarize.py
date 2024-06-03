import json
import sys
from collections import defaultdict
import statistics
import csv


def summarize():
    data = json.load(sys.stdin)
    aggregates = defaultdict(list)
    for run in data:
        aggregates[(run['bench_name'], run['shader'])] += run['fpsData']

    writer = csv.DictWriter(
        sys.stdout,
        ['bench_name', 'shader', 'mean', 'stdev']
    )
    writer.writeheader()
    for (bench, shader), times in aggregates.items():
        mean = statistics.mean(times)
        stdev = statistics.stdev(times)
        writer.writerow({
            'bench_name': bench,
            'shader': shader,
            'mean': mean,
            'stdev': stdev,
        })


if __name__ == '__main__':
    summarize()
