PERM_READ = 0x01
PERM_UPDATE = 0x02
PERM_CREATE = 0x04
PERM_DELETE = 0x08
PERM_WRITE = PERM_UPDATE | PERM_CREATE | PERM_DELETE
PERM_DENY = 0
PERM_RW = PERM_READ | PERM_WRITE

MATCH_NO = 0
MATCH_YES = 1
MATCH_PARTIAL = 2