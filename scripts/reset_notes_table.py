#!/usr/bin/env python

import os
import sys

from notes import routes


if __name__ == "__main__":
    try:
        routes.reset()
    except Exception as e:
        note.logger.error("Error (Reset Notes): cannot reset notes table - %s" % e)
        sys.exit(1)
        
    sys.exit()
