import sys
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

from plugin.ilo_pana_pi_sitelen_pona import IloPanaPiSitelenPona

if __name__ == "__main__":
    IloPanaPiSitelenPona().run()