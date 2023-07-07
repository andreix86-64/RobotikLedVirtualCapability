import sys
from abc import ABC

from AbstractVirtualCapability import AbstractVirtualCapability, VirtualCapabilityServer


class DistanceSensorVirtualCapability(AbstractVirtualCapability, ABC):
    """ Simple calculator to test virtual capabilities """

    def __init__(self, server):
        super().__init__(server)
        # From 0 to 100
        self.current_brightness_percent = 0
        self.auto_measure = False

    def _error(self, message) -> dict:
        return self._result(f"[ERROR] {message}")

    def andrei_led_toggle_auto_measure(self, args: dict):
        self.auto_measure = not self.auto_measure

    def andrei_led_set_brightness(self, args: dict):
        raw_value = args["SimpleDoubleParameter"]
        # Check if the values are out of bound
        if raw_value < 0:
            raw_value = 0
        elif raw_value > 100:
            raw_value = 100

        # Save the brightness level
        self.current_brightness_percent = raw_value

    def loop(self):
        if self.auto_measure:
            # Should trigger the measure distance capability
            pass


if __name__ == "__main__":
    try:
        port = None
        if len(sys.argv[1:]) > 0:
            port = int(sys.argv[1])
        server = VirtualCapabilityServer(port)
        tf = DistanceSensorVirtualCapability(server)
        tf.start()
        while server.running:
            pass
    except KeyboardInterrupt:
        print("[Main] Received KeyboardInterrupt")
