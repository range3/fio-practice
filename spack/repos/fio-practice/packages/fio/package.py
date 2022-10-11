# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.fio import Fio as BuiltinFio

class Fio(BuiltinFio):
    url      = "https://github.com/axboe/fio/archive/fio-3.32.tar.gz"

    version('3.32', sha256='409e459840912e68be487dbbda9a7a1b3f6ddf1478e3f456f278f957ce4f7b66')
