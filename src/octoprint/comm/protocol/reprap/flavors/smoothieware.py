__license__ = "GNU Affero General Public License http://www.gnu.org/licenses/agpl.html"
__copyright__ = "Copyright (C) 2018 The OctoPrint Project - Released under terms of the AGPLv3 License"

from octoprint.comm.protocol.reprap.flavors import StandardFlavor


class ReprapFirmwareFlavor(StandardFlavor):

    key = "smoothieware"
    name = "Smoothieware"
