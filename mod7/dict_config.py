dict_conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": '%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s'
        }
    },
    "handlers": {
        "server": {
            "class": "app_calc.CustomHttpHandler",
            "host": "localhost:5000",
            "url": "http://localhost:5000/runcode_post",
            "method": "POST",
            "level": "DEBUG"
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": "ext://sys.stdout",
            "filters": ["ascii"]
        },
        "utils": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "when": "h",
            "interval": 10,
            "formatter": "base",
            "filename": "utils.log",
            "encoding": "utf-8",
            "backupCount": 0,
            "filters": ["ascii"]
        },
        "file_debug": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calc_debug.log",
            "mode": 'a',
            "encoding": "utf-8",
            "filters": ["debug", "ascii"]
        },
        "file_notset": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calc_notset.log",
            "mode": 'a',
            "encoding": "utf-8",
            "filters": ["notset", "ascii"]
        },
        "file_info": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calc_info.log",
            "mode": 'a',
            "encoding": "utf-8",
            "filters": ["info", "ascii"]
        },
        "file_warning": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calc_warning.log",
            "mode": 'a',
            "encoding": "utf-8",
            "filters": ["warning", "ascii"]
        },
        "file_error": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calc_error.log",
            "mode": 'a',
            "encoding": "utf-8",
            "filters": ["error", "ascii"]
        },
        "file_critical": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calc_critical.log",
            "mode": 'a',
            "encoding": "utf-8",
            "filters": ["critical", "ascii"]
        }
    },
    "loggers": {
        "calculator_app": {
            "level": "DEBUG",
            "handlers": ["server", "file_debug", "file_notset", "file_info",
                         "file_critical", "file_error", "file_warning", "console"]
        },
        "calculator_utils": {
            "level": "DEBUG",
            "handlers": ["server", "file_debug", "file_notset", "file_info",
                         "file_critical", "file_error", "file_warning", "console", "utils"]
        }
    },
    "filters": {
        "debug": {
            "()": "app_calc.CustomFilter",
            "level": "debug"
        },
        "notset": {
            "()": "app_calc.CustomFilter",
            "level": "notset"
        },
        "info": {
            "()": "app_calc.CustomFilter",
            "level": "info"
        },
        "warning": {
            "()": "app_calc.CustomFilter",
            "level": "warning"
        },
        "error": {
            "()": "app_calc.CustomFilter",
            "level": "error"
        },
        "critical": {
            "()": "app_calc.CustomFilter",
            "level": "critical"
        },
        "ascii": {
            "()": "app_calc.AsciiFilter"
        }
    }
}
