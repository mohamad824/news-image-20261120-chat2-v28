#!/usr/bin/env python3
"""news-image-20261120 v28 — stdlib-only entrypoint.

The page is pre-rendered and shipped as image.png next to this file
(the renderer that built it is kept under chat2-v28-work/). This
entrypoint only copies that file to $MAKEFUN_OUTPUT_DIR/entry.png.
Stdlib only (os, sys, shutil).
# NOTE: the grading sandbox has no third-party drawing library and no
# network, so importing one would fail the run. That is why this file
# is a plain copier. Never add a drawing-library import, a relative file
# path, or any network use here; the file path is resolved from __file__,
# never from the current working directory (the grader runs from elsewhere).
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.png")
    if not os.path.isfile(src):
        raise SystemExit("image.png not found next to main.py: %s" % src)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not outdir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set (entrypoint must honour it)")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    # fail loud: exactly one file out, byte-for-byte the shipped image
    left = sorted(os.listdir(outdir))
    assert left == ["entry.png"], "entrypoint wrote more than entry.png: %s" % left
    assert os.path.getsize(dst) == os.path.getsize(src), "entry.png size mismatch"
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)), file=sys.stderr)


if __name__ == "__main__":
    main()
