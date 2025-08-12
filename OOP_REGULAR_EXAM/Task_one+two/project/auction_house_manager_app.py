from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    valid_artifacts = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}
    valid_collectors = {"Museum": Museum, "PrivateCollector": PrivateCollector}

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.valid_artifacts:
            raise ValueError("Unknown artifact type!")
        if any(a.name == artifact_name for a in self.artifacts):
            raise ValueError(f"{artifact_name} has been already registered!")
        if artifact_type == "RenaissanceArtifact":
            artifact = RenaissanceArtifact(artifact_name, artifact_price, artifact_space)
            self.artifacts.append(artifact)
            return f"{artifact_name} is successfully added to the auction as {artifact_type}."
        else:
            artifact = ContemporaryArtifact(artifact_name, artifact_price, artifact_space)
            self.artifacts.append(artifact)
            return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.valid_collectors:
            raise ValueError("Unknown collector type!")
        if any(c.name == collector_name for c in self.collectors):
            raise ValueError(f"{collector_name} has been already registered!")
        if collector_type == "Museum":
            collector = Museum(collector_name)
            self.collectors.append(collector)
            return f"{collector_name} is successfully registered as a {collector_type}."
        else:
            collector = PrivateCollector(collector_name)
            self.collectors.append(collector)
            return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        try:
            collector = [c for c in self.collectors if c.name == collector_name][0]
        except IndexError:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
            # return f"Collector {collector_name} is not registered to the auction!"

        try:
            artifact = [a for a in self.artifacts if a.name == artifact_name][0]
        except IndexError:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
            # return f"Artifact {artifact_name} is not registered to the auction!"

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required
        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        try:
            artifact = [a for a in self.artifacts if a.name == artifact_name][0]
        except IndexError:
            return "No such artifact."
        # if not artifact:
        #     return "No such artifact."
        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        counter = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                counter += 1
        return f"{counter} collector/s increased their available money."

    def get_auction_report(self):
        total_sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        available_artifacts = len(self.artifacts)
        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))
        collectors_output = "\n".join(str(c) for c in sorted_collectors)
        return (f"**Auction statistics**\n"
                f"Total number of sold artifacts: {total_sold_artifacts}\n"
                f"Available artifacts for sale: {available_artifacts}\n"
                f"***\n"
                f"{collectors_output}")