"""Create a self-contained skill ZIP, excluding local tools and build outputs."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from library import ROOT


def package():
    destination = ROOT / 'dist' / 'michael-damaige-skill-v0.1.0.zip'
    destination.parent.mkdir(exist_ok=True)
    omitted = {'.git', '.venv', '__pycache__', 'dist'}
    with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
        for path in sorted(ROOT.rglob('*')):
            relative = path.relative_to(ROOT)
            if path.is_file() and not omitted.intersection(relative.parts):
                archive.write(path, (Path('michael-damaige') / relative).as_posix())
    return destination


if __name__ == '__main__':
    print(package())
