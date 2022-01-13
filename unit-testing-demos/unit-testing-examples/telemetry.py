class TelemetryDiagnosticControls:
    DiagnosticChannelConnectionString = "*111#"

    def __init__(self, client=None):
        self.telemetry_client = client or TelemetryClient()
        self.diagnostic_info = ""

    def check_transmission(self):
        self._reconnect()
        self._send_and_receive()

    def _send_and_receive(self):
        self.diagnostic_info = ""
        self.telemetry_client.send(TelemetryClient.DIAGNOSTIC_MESSAGE)
        self.diagnostic_info = self.telemetry_client.receive()

    def _reconnect(self):
        self.telemetry_client.disconnect()
        retries_left = 3
        while not self.telemetry_client.get_online_status() and retries_left > 0:
            self.telemetry_client.connect(TelemetryDiagnosticControls.DiagnosticChannelConnectionString)
            retries_left -= 1
        if not self.telemetry_client.get_online_status():
            raise Exception("Unable to connect.")


class TelemetryClient:
    DIAGNOSTIC_MESSAGE = "AT#UD"

    def __init__(self):
        self.online_status = False
        self._diagnostic_message_result = ""

    def connect(self, telemetry_server_connection_string):
        if not telemetry_server_connection_string:
            raise Exception()

        # simulate the operation on a real modem
        success = random.randint(0, 10) <= 8
        self.online_status = success

    def disconnect(self):
        self.online_status = False

    def send(self, message):
        if not message:
            raise Exception()

        if message == TelemetryClient.DIAGNOSTIC_MESSAGE:
            # simulate a status report
            self._diagnostic_message_result = """\
LAST TX rate................ 100 MBPS\r\n
HIGHEST TX rate............. 100 MBPS\r\n
LAST RX rate................ 100 MBPS\r\n
HIGHEST RX rate............. 100 MBPS\r\n
BIT RATE.................... 100000000\r\n
WORD LEN.................... 16\r\n
WORD/FRAME.................. 511\r\n
BITS/FRAME.................. 8192\r\n
MODULATION TYPE............. PCM/FM\r\n
TX Digital Los.............. 0.75\r\n
RX Digital Los.............. 0.10\r\n
BEP Test.................... -5\r\n
Local Rtrn Count............ 00\r\n
Remote Rtrn Count........... 00"""

            return
        # here should go the real Send operation (not needed for this exercise)

    def receive(self):
        if not self._diagnostic_message_result:
            # simulate a received message (just for illustration - not needed for this exercise)
            message = ""
            messageLength = random.randint(0, 50) + 60
            i = messageLength
            while (i >= 0):
                message += chr((random.randint(0, 40) + 86))
                i -= 1
        else:
            message = self._diagnostic_message_result
            self._diagnostic_message_result = ""

        return message
