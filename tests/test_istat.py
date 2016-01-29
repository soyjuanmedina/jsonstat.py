# -*- coding: utf-8 -*-
# This file is part of https://github.com/26fe/jsonstat.py
# Copyright (C) 2016 gf <gf@26fe.com>
# See LICENSE file

# stdlib
from __future__ import print_function
from __future__ import unicode_literals
import os
import unittest

# jsonstat
import jsonstat.istat as istat


class TestIstat(unittest.TestCase):
    def setUp(self):
        self.fixture_dir = os.path.join(os.path.dirname(__file__), "fixtures", "istat")

    def test_istat_italian(self):
        i = istat.Istat(self.fixture_dir, lang=0)
        n = i.area(26).desc()
        self.assertEqual("Lavoro", n)

        d = i.area(26).dataset('DCCV_INATTIVMENS').name()
        self.assertEqual(u'Inattivi - dati mensili', d)

        dname = i.area(26).dataset('DCCV_INATTIVMENS').dimension(0).name()
        self.assertEquals("Territorio", dname)

    def test_istat_english(self):
        i = istat.Istat(self.fixture_dir, lang=1)
        n = i.area(26).desc()
        self.assertEqual("Labour", n)

        d = i.area(26).dataset('DCCV_INATTIVMENS').name()
        self.assertEqual(u'Inactive population - monthly data', d)

        dim = i.area(26).dataset('DCCV_INATTIVMENS').dimension(0)
        self.assertEqual('Territory', dim.name())
        
        dname = i.area(26).dataset('DCCV_INATTIVMENS').dimension(0).name()
        self.assertEquals("Territory", dname)

    def test_areas(self):
        i = istat.Istat(self.fixture_dir, lang=1)
        istat_area = i.area(3)
        self.assertEquals("CEN", istat_area.cod())

if __name__ == '__main__':
    unittest.main()
