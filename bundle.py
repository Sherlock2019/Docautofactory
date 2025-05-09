
import shutil, os, zipfile, datetime, pathlib
def bundle(src=".", dest="docfactory_bundle.zip"):
    dst = pathlib.Path(dest)
    if dst.exists(): dst.unlink()
    with zipfile.ZipFile(dest,"w",zipfile.ZIP_DEFLATED) as z:
        for path in pathlib.Path(src).rglob("*"):
            if ".git" in path.parts: continue
            z.write(path,arcname=path.relative_to(src))
    print("Created", dest)
if __name__=="__main__":
    bundle()
