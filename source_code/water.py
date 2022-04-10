class Water:
    def get_state(self, temperature):
        if temperature <= 0:
            return "Solid"
        if 0 < temperature < 100:
            return "Liquid"
        if 100 <= temperature < 500:
            return "Gas"
        return None
