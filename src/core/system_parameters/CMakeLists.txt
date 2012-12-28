# Copyright (C) 2012-2013  (see AUTHORS file for a list of contributors)
#
# This file is part of GNSS-SDR.
#
# GNSS-SDR is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# at your option) any later version.
#
# GNSS-SDR is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNSS-SDR. If not, see <http://www.gnu.org/licenses/>.
#

set(SYSTEM_PARAMETERS_SOURCES
     gnss_satellite.cc
     gnss_signal.cc
     gps_navigation_message.cc
)

include_directories(
     $(CMAKE_CURRENT_SOURCE_DIR)
     ${GLOG_INCLUDE_DIRS}
     ${Boost_INCLUDE_DIRS}
)

link_directories(${Boost_LIBRARY_DIR})

add_library(gnss_system_parameters ${SYSTEM_PARAMETERS_SOURCES})
target_link_libraries(gnss_system_parameters ${Boost_LIBRARIES})