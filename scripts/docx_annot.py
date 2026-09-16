#!/usr/bin/env python3
"""Extract highlighted / colored / struck annotation runs from a .docx.

Stdlib only (zipfile + ElementTree). Prints each paragraph that contains at
least one marked run, with the marked runs wrapped in [H]...[/H].
Usage: python3 scripts/docx_annot.py <file.docx> [--all]
"""
import sys, zipfile, xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def marked(rPr):
    """Return a short tag describing why this run is marked, or None."""
    if rPr is None:
        return None
    tags = []
    hl = rPr.find(W + "highlight")
    if hl is not None and hl.get(W + "val") not in (None, "none"):
        tags.append(hl.get(W + "val"))
    col = rPr.find(W + "color")
    if col is not None:
        v = (col.get(W + "val") or "").lower()
        if v not in ("", "auto", "000000", "ffffff"):
            tags.append("#" + v)
    if rPr.find(W + "strike") is not None:
        tags.append("strike")
    u = rPr.find(W + "u")
    if u is not None and u.get(W + "val") not in (None, "none"):
        tags.append("u")
    return ",".join(tags) if tags else None


def para_text(p):
    """(plain_text, marked_text, [reasons]) for one paragraph."""
    plain, out, reasons = [], [], []
    for r in p.iter(W + "r"):
        txt = "".join(t.text or "" for t in r.iter(W + "t"))
        if not txt:
            continue
        plain.append(txt)
        why = marked(r.find(W + "rPr"))
        if why:
            out.append("[H:%s]%s[/H]" % (why, txt))
            reasons.append(why)
        else:
            out.append(txt)
    return "".join(plain), "".join(out), reasons


def main():
    path = sys.argv[1]
    show_all = "--all" in sys.argv
    with zipfile.ZipFile(path) as z:
        names = [n for n in z.namelist()
                 if n in ("word/document.xml",)
                 or n.startswith("word/footnotes") or n.startswith("word/endnotes")]
        for name in names:
            root = ET.fromstring(z.read(name))
            for i, p in enumerate(root.iter(W + "p")):
                plain, marked_txt, reasons = para_text(p)
                if not plain.strip():
                    continue
                if reasons or show_all:
                    print("[%s p%04d] %s" % (name.split("/")[-1][:8], i, marked_txt))


if __name__ == "__main__":
    main()
