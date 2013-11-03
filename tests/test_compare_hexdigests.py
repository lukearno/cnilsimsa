
from unittest import TestCase

from cnilsimsa import compare_hexdigests


class HexDigestCompareTests(TestCase):

    def test_compare_identical(self):
        self.assertEqual(
            compare_hexdigests('0'*64, '0'*64),
            128)

    def test_compare_diametrical(self):
        self.assertEqual(
            compare_hexdigests('0'*64, 'F'*64),
            -128)

    def test_compare_digest_too_short(self):
        self.assertRaises(ValueError, compare_hexdigests, ('0'*63, '0'*64))

    def test_compare_digest_too_long(self):
        self.assertRaises(ValueError, compare_hexdigests,
                          ('0'*65, '0'*64))

    def test_compare_expected_values(self):
        self.assertEqual(
            compare_hexdigests(
                '4337648a22d209ceb1725fddea2c5529'
                '4ce183f9536286ac3f674bee520dfff6',
                '1da080602272e0aecd157c91f540a72a'
                '3c2b483f42569f462c43ea08e6f8e3ed'),
            9)
        self.assertEqual(
            compare_hexdigests(
                '4337648a22d209ceb1725fddea2c5529'
                '4ce183f9536286ac3f674bee520dfff6',
                '313461d90a7329c899511fa0ff4a9f21'
                '67832ff3097ad54daca1aa2df01b747f'),
            28)
        self.assertEqual(
            compare_hexdigests(
                '4337648a22d209ceb1725fddea2c5529'
                '4ce183f9536286ac3f674bee520dfff6',
                'f8f3afe6b0406176a043fc27f62277bb'
                'b6b2947c5c04fafd67871ffefec2d3db'),
            11)
