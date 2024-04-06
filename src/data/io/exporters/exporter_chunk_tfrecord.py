from data.io.exporters.exporter_tfrecord import ExporterTFRecordStrategy
import os


class ExporterChunkTFRecordStrategy(ExporterTFRecordStrategy):
    
    def export(self):
        if not os.path.exists(self.cfg.exporter_dataset_path):
            os.makedirs(self.cfg.exporter_dataset_path)
            
        existent_files = os.listdir(self.cfg.exporter_dataset_path)

        existent_chunks = [int(name.split('_')[-1].split('.')[0]) for name in existent_files \
                               if name.startswith('chunk') and name.endswith('.tfrecord')]
        next_chunk = max(existent_chunks, default=-1) + 1

        chunk_name = f'chunk_{next_chunk}'
        self._export(chunk_name)
