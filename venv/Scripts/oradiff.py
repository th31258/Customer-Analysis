#!E:\Customer Analysis\venv\Scripts\python.exe
# -*- coding: utf-8 -*-
# cython: language_level=3, always_allow_keywords=True

import sys


if __name__ == "__main__":
	from ll.orasql.scripts import oradiff
	sys.exit(oradiff.main())
