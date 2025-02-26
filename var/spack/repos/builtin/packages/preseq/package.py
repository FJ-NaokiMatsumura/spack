# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Preseq(MakefilePackage):
    """The preseq package is aimed at predicting and estimating the complexity
       of a genomic sequencing library, equivalent to predicting and
       estimating the number of redundant reads from a given sequencing depth
       and how many will be expected from additional sequencing using an
       initial sequencing experiment."""

    homepage = "https://github.com/smithlabcode/preseq"
    url      = "https://github.com/smithlabcode/preseq/releases/download/v2.0.2/preseq_v2.0.2.tar.bz2"

    version('2.0.2', sha256='1d7ea249bf4e5826e09697256643e6a2473bc302cd455f31d4eb34c23c10b97c')

    depends_on('samtools')
    depends_on('gsl')

    def setup_build_environment(self, env):
        env.set('PREFIX', self.prefix)
