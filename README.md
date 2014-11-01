pyflate
=======

Python3 inflate test. Objective is to find if there's something wrong with Node.js's pako library. [Initial tests with pako](//github.com/luciopaiva/pdfhacker) resulted in truncated output.

Well, after an initial test I proved pako is truncating its output for sure. Simply run ``python3 pyflate`` and compare output with pako's.
