import logging


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg = msg.replace('"', '\\"')
        return msg, kwargs


logger = JsonAdapter(logging.getLogger(__name__))
logging.basicConfig(level=logging.DEBUG,
                        filename='skillbox_json_messages.log',
                        format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
                        encoding='utf-8',
                        filemode='w',
                        datefmt='%H:%M:%S')
