import re

LOG_LINE_REGEX = re.compile(r'(?P<timestamp>[a-zA-Z]{3}\s+\d{1,2} \d{2}:\d{2}:\d{2}) (?P<hostname>\w+) (?P<appname>[\w\-\.\+]+)\[(?P<pid>\d+)\]: (?P<message>.*)')


def parse_log_line(log_line):
    """
    Parse une ligne de log et renvoie un dictionnaire contenant les champs de log.
    """
    match = LOG_LINE_REGEX.match(log_line)
    if not match:
        return None
    return match.groupdict()


def parse():
    """
    Parse le fichier de logs spécifié et renvoie une liste de dictionnaires contenant les champs de log.
    """
    with open('fontconfig.log') as f:
        return [parse_log_line(line) for line in f if parse_log_line(line)]
