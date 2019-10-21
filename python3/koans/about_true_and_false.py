#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTrueAndFalse(Koan):
    def truth_value(self, condition):
        if condition:
            return 'true stuff'
        else:
            return 'false stuff'

    def test_true_is_treated_as_true(self):
        self.assertEqual('true stuff', self.truth_value(True))
# True returns 'true stuff' because true is truthy.

    def test_false_is_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(False))
# False returns 'false stuff' because false is falsey.

    def test_none_is_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(None))
# None returns 'false stuff' because None is falsey.

    def test_zero_is_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(0))
# 0 returns 'false stuff' because 0 is falsey.

    def test_empty_collections_are_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value([]))
        self.assertEqual('false stuff', self.truth_value(()))
        self.assertEqual('false stuff', self.truth_value({}))
        self.assertEqual('false stuff', self.truth_value(set()))
#  the empty collections return 'false stuff' because empty collections are flasey

    def test_blank_strings_are_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(""))
#  empty strings are falsey

    def test_everything_else_is_treated_as_true(self):
        self.assertEqual('true stuff', self.truth_value(1))
        self.assertEqual('true stuff', self.truth_value([0]))
        self.assertEqual('true stuff', self.truth_value((0,)))
        self.assertEqual(
            'true stuff',
            self.truth_value("Python is named after Monty Python"))
        self.assertEqual('true stuff', self.truth_value(' '))
        self.assertEqual('true stuff', self.truth_value('0'))
#  the above asserts are truthy
