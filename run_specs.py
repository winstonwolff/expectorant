#!/usr/bin/env python3

import doctest
from expectorant import expector
import expectorant

print("Running doctests...")
doctest.testmod(expector)
print("doctests done.")

expectorant.main()



