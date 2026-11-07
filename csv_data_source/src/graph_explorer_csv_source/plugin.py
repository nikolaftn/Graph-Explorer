"""CSV source plugin scaffold."""

from graph_explorer_api.plugins.data_source import DataSourcePlugin


class CsvDataSource(DataSourcePlugin):
    @property
    def name(self) -> str:
        return "CSV file"

    def load(self, source):
        raise NotImplementedError("CSV parsing is not implemented yet.")
