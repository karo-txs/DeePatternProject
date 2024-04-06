from data.core.types import ExportProcessedData


class ExporterTFRecordStrategy(ExportProcessedData):
    
    def export(self):
        self._export(self.transitional_object.split_name)

    def _export(self, file_name: str):
        pass
