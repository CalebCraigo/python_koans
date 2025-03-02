#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual({'MacLeod', 'Ramirez', 'Matunas', 'Malcolm'}, there_can_only_be_only_one)
# the assert returns the set for each name listed in highlanders.

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        self.assertEqual({1, 2, 3}, {1, 2, 3})
        self.assertEqual(set(), set())

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        # Note: Literal sets using braces were introduced in python 3.
        #       They were also backported to python 2.7.

        self.assertEqual(set, {1, 2, 3}.__class__)
        self.assertEqual(dict, {'one': 1, 'two': 2}.__class__)
#  the set doesn't have a key for the value
#  the dictionary has keys for the values

        self.assertEqual(dict, {}.__class__)
#  empty curly brackets are considerd dictionaries

    # def test_creating_sets_using_strings(self):
    #     self.assertEqual({'12345'}, {'12345'})
    #     self.assertEqual({'1''2''3''4''5'}, set('12345'))
    #
    # def test_convert_the_set_into_a_list_to_sort_it(self):
    #     self.assertEqual({'1''2''3''4''5'}, sorted(set('12345')))

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual({'Willie'}, scotsmen - warriors)
#  returns the string for scotsmen that is not in warriors
        self.assertEqual({'MacLeod', 'Leonidas', 'Wallace', 'Willie'}, scotsmen | warriors)
# returns one instance for each name that appears in both sets
        self.assertEqual({'MacLeod', 'Wallace'}, scotsmen & warriors)
# returns the 2 names that appear in both sets
        self.assertEqual({'Willie', 'Leonidas'}, scotsmen ^ warriors)
# returns the 2 names that only appear in 1 of the 2 sets
    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in {127, 0, 0, 1} )
# truthy sense number appears in set
        self.assertEqual(True, 'cow' not in set('apocalypse now') )
# truthy sense cow doesn't appear in set

    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake'))
# truthy sense cake appears in the set
        self.assertEqual(True, set('cake').issubset(set('cherry cake')) )
# truth sense cake appears in subset
        self.assertEqual(False, set('cake') > set('pie'))
# flasey sense cake cannot be greater than pie
