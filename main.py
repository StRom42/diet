# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.models.wrapper import DIETClassifierWrapper

if __name__ == "__main__":
    config_file = "src/config.yml"

    wrapper = DIETClassifierWrapper(config=config_file)

    print(wrapper.predict(["Где встреча выпускников?"]))

    wrapper.train_model()

    print(wrapper.predict(["Где встреча выпускников 29 февраля"]))
