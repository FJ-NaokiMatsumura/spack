# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import platform

from spack import *


class IntelOneapiTbb(IntelOneApiLibraryPackage):
    """Intel oneAPI TBB."""

    maintainers = ['rscohn2']

    homepage = 'https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onetbb.html'

    if platform.system() == 'Linux':
        version('2021.5.1',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/18473/l_tbb_oneapi_p_2021.5.1.738_offline.sh',
                sha256='c154749f1f370e4cde11a0a7c80452d479e2dfa53ff2b1b97003d9c0d99c91e3',
                expand=False)
        version('2021.5.0',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/18380/l_tbb_oneapi_p_2021.5.0.707_offline.sh',
                sha256='6ff7890a74a43ae02e0fa2d9c5533fce70a49dff8e73278b546a0995367fec5e',
                expand=False)
        version('2021.4.0',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/18194/l_tbb_oneapi_p_2021.4.0.643_offline.sh',
                sha256='33332012ff8ffe7987b1a20bea794d76f7d8050ccff04fa6e1990974c336ee24',
                expand=False)
        version('2021.3.0',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17952/l_tbb_oneapi_p_2021.3.0.511_offline.sh',
                sha256='b83f5e018e3d262e42e9c96881845bbc09c3f036c265e65023422ca8e8637633',
                expand=False)
        version('2021.2.0',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17759/l_tbb_oneapi_p_2021.2.0.357_offline.sh',
                sha256='c1c3623c5bef547b30eac009e7a444611bf714c758d7472c114e9be9d5700eba',
                expand=False)
        version('2021.1.1',
                url='https://registrationcenter-download.intel.com/akdlm/irc_nas/17378/l_tbb_oneapi_p_2021.1.1.119_offline.sh',
                sha256='535290e3910a9d906a730b24af212afa231523cf13a668d480bade5f2a01b53b',
                expand=False)

    provides('tbb')

    @property
    def component_dir(self):
        return 'tbb'
