"""JSON source plugin scaffold."""

from graph_explorer_api.plugins.data_source import DataSourcePlugin


class JsonDataSource(DataSourcePlugin):
    @property
    def name(self) -> str:
        return "JSON file"

    def load(self, source):
        raise NotImplementedError("JSON parsing is not implemented yet.")
