class Battery:
    PERCENTAGE = 0

    def get_percentage(self) -> int:
        return self.PERCENTAGE

    def is_full(self) -> bool:
        return self.PERCENTAGE == 100

    def set_percentage(self, new_percentage):
        my_percentage = new_percentage
        if new_percentage > 100:
            my_percentage = 100
        if new_percentage < 0:
            my_percentage = 0
        self.PERCENTAGE = my_percentage

    def show_battery_percentage(self):
        return f"My percentage is {self.get_percentage()}%"
