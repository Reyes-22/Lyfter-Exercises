class ToyotaCar:
    def __init__(self, model, year, **kwargs):
        self.model = model
        self.year = year
        super().__init__(**kwargs)

    def start_engine(self):
        return f"{self.model} engine started."

    def stop_engine(self):
        return f"{self.model} engine stopped."


class FourWheelDrive:
    def __init__(self, chassis_type, **kwargs):
        self.chassis_type = chassis_type
        super().__init__(**kwargs)


class Automobile:
    def __init__(self, chassis_type, **kwargs):
        self.chassis_type = chassis_type
        super().__init__(**kwargs)


class ToyotaFortuner(ToyotaCar, FourWheelDrive):
    def __init__(self, model, year, chassis_type):
        super().__init__(model=model, year=year, chassis_type=chassis_type)

    def display_info(self):
        return f"Model: {self.model}, Year: {self.year}, Chassis Type: {self.chassis_type}"


class ToyotaCorolla(ToyotaCar, Automobile):
    def __init__(self, model, year, chassis_type):
        super().__init__(model=model, year=year, chassis_type=chassis_type)

    def display_info(self):
        return f"Model: {self.model}, Year: {self.year}, Chassis Type: {self.chassis_type}"


fortuner = ToyotaFortuner("Fortuner", 2022, "SUV")
print(fortuner.start_engine())
print(fortuner.display_info())


corolla = ToyotaCorolla("Corolla", 2021, "Sedan")
print(corolla.start_engine())
print(corolla.display_info())
