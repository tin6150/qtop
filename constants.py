import os

QTOPCONF_YAML = 'qtopconf.yaml'
# QTOP_LOGFILE = '$HOME/.local/qtop/qtop.log'
QTOP_LOGFILE = '$HOME/.local/qtop/qtop_%s.log'  % os.getpid()
QTOP_LOGFILE = os.path.expandvars(QTOP_LOGFILE)
USERPATH = os.path.expandvars('$HOME/.local/qtop')
MAX_CORE_ALLOWED = 150000  # not used anywhere
MAX_UNIX_ACCOUNTS = 87  # was : 62