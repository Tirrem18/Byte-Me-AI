import os
from core.mode_manager.modes.test_mode import run_test_mode
from core.mode_manager.modes.production_mode import run_production_mode

class ModeManager:
    def __init__(self, model):
        self.mode = os.getenv("MODE", "Production").lower()
        self.model = model

    def run(self):
        print(f"🧠 Mode set to: {self.mode.title()}")
        if self.mode == "test":
            run_test_mode(self.model)
        elif self.mode == "production":
            run_production_mode(self.model)
        else:
            raise ValueError(f"Unsupported MODE: {self.mode}")
