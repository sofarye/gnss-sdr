#!/usr/bin/env python
#
# Copyright (C) 2010-2018 (see AUTHORS file for a list of contributors)
#
# This file is part of GNSS-SDR.
#
# GNSS-SDR is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GNSS-SDR is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNSS-SDR. If not, see <https://www.gnu.org/licenses/>.
#

from __future__ import print_function

import os
import re
import sys
import optparse
import volk_gnsssdr_arch_defs
import volk_gnsssdr_machine_defs
import volk_gnsssdr_kernel_defs
from mako.template import Template

def __parse_tmpl(_tmpl, **kwargs):
    defs = {
        'archs': volk_gnsssdr_arch_defs.archs,
        'arch_dict': volk_gnsssdr_arch_defs.arch_dict,
        'machines': volk_gnsssdr_machine_defs.machines,
        'machine_dict': volk_gnsssdr_machine_defs.machine_dict,
        'kernels': volk_gnsssdr_kernel_defs.kernels,
    }
    defs.update(kwargs)
    _tmpl = """
        
/* this file was generated by volk_gnsssdr template utils, do not edit! */
        
""" + _tmpl
    return str(Template(_tmpl).render(**defs))

def main():
    parser = optparse.OptionParser()
    parser.add_option('--input', type='string')
    parser.add_option('--output', type='string')
    (opts, args) = parser.parse_args()
    
    output = __parse_tmpl(open(opts.input).read(), args=args)
    if opts.output: open(opts.output, 'w').write(output)
    else: print(output)

if __name__ == '__main__': main()

