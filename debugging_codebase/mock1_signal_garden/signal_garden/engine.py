from .aggregate import ReportAggregator
from .feature import FeatureBuilder
from .tree import build_balanced, leaves


class GardenEngine:
    def __init__(self, bucket_count: int = 4):
        self.builder = FeatureBuilder(bucket_count)
        self.aggregator = ReportAggregator(bucket_count)

    def run(self, observations):
        tree = build_balanced(observations)
        ordered = leaves(tree)
        stats = [self.builder.build(obs) for obs in ordered]
        return self.aggregator.aggregate(stats)
