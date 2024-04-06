from deepattern import Strategy


class SetCallbacksStrategy(Strategy):

    def run_strategy(self):
        self.transitional_object.create_attr("callbacks", [])
