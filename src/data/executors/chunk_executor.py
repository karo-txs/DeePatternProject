from deepattern import Strategy, StrategyHandler


class ChunkExecutorStrategy(Strategy):

    def set_sub_strategies(self, sub_strategies: list, chunk: int = 4000):
        self.sub_strategies = sub_strategies
        self.chunk = chunk
        return self

    def create_batch(self, data_list, chunk_size):
        for i in range(0, len(data_list), chunk_size):
            yield data_list[i:i + chunk_size]

    def run_strategy(self):
        data_batch = list(self.create_batch(self.transitional_object.data_paths, self.chunk))

        count = 0
        for data_path in data_batch:
            self.logger.info(f"Chunk: {count}/{len(data_batch)}")
            self.transitional_object.data_paths = data_path
            count += 1

            handler = StrategyHandler.builder(self.sub_strategies)
            while handler.handle():
                continue
