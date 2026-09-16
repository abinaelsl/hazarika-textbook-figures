#!/usr/bin/env python3
"""Extract embedded media from a .docx into <outdir>/. Stdlib only.
Usage: python3 scripts/docx_extract.py <file.docx> <outdir>
Note: EMF/WMF are vector-Office formats and are NOT renderable here — prefer
the .png/.jpeg siblings.
"""
import sys, zipfile, os

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
with zipfile.ZipFile(src) as z:
    media = [n for n in z.namelist() if n.startswith("word/media/")]
    for n in sorted(media):
        base = os.path.basename(n)
        data = z.read(n)
        with open(os.path.join(out, base), "wb") as fh:
            fh.write(data)
        print("%-24s %8d bytes" % (base, len(data)))
