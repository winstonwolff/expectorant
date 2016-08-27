#!/usr/bin/env python3

import doctest
import expectorant

from expectorant import expector, spec

print("Running doctests...")
doctest.testmod(expector)
doctest.testmod(spec)
print("doctests done.")

expectorant.main()



