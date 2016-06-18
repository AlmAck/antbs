#!/usr/bin/env python
#  -*- coding: utf-8 -*-
#
#  package.py
#
#  Copyright © 2016 Antergos
#
#  This file is part of The Antergos Build Server, (AntBS).
#
#  AntBS is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  AntBS is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  The following additional terms are in effect as per Section 7 of the license:
#
#  The preservation of all legal notices and author attributions in
#  the material or in the Appropriate Legal Notices displayed
#  by works containing it is required.
#
#  You should have received a copy of the GNU General Public License
#  along with AntBS; If not, see <http://www.gnu.org/licenses/>.

from views import *

package_view = Blueprint('package', __name__)


###
##
#   Utility Functions For This View
##
###

###
##
#   Views Start Here
##
###

@package_view.route('/<pkgname>', methods=['GET'])
def get_and_show_pkg_profile(pkgname=None):
    if pkgname is None or not status.all_packages.ismember(pkgname):
        abort(404)

    pkgobj = get_pkg_object(name=pkgname)
    if '' == pkgobj.description:
        desc = pkgobj.get_from_pkgbuild('pkgdesc')
        pkgobj.description = desc
        pkgobj.pkgdesc = desc

    build_history, timestamps = get_build_history_chart_data(pkgobj)

    return try_render_template('package.html', pkg=pkgobj, build_history=build_history,
                               timestamps=timestamps)
