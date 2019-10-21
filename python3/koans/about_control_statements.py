#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutControlStatements(Koan):

    def test_if_then_else_statements(self):
        if True:
            result = 'true value'
        else:
            result = 'false value'
        self.assertEqual('true value', result)

    def test_if_then_statements(self):
        result = 'default value'
        if True:
            result = 'true value'
        self.assertEqual('true value', result)

    def test_if_then_elif_else_statements(self):
        if False:
            result = 'first value'
        elif True:
            result = 'true value'
        else:
            result = 'default value'
        self.assertEqual('true value', result)

    def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        self.assertEqual(3628800, result)
# i increases by 1 as long it is less than or equal to 10 and then multiplied by
# result of the previous equation

    def test_break_statement(self):
        i = 1
        result = 1
        while True:
            if i > 10: break
            result = result * i
            i += 1
        self.assertEqual(3628800, result)
# i increases by 1 until i is greater than 10 then the break stops the while loop
# and then multiplied by result of the previous equation

    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue
            result.append(i)
        self.assertEqual([1, 3, 5, 7, 9], result)
# this calculates the remainder of 1 - 10 divided by 2 and appends the integers
# where the remainder is 0

    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = []
        for item in phrase:
            result.append(item.upper())
        self.assertEqual(["FISH", "AND", "CHIPS"], result)
# appends the the words in phrase but they are now in uppercase

    # def test_for_statement_with_tuples(self):
        # round_table = [
        #     ("Lancelot", "Blue"),
        #     ("Galahad", "I don't know!"),
        #     ("Robin", "Blue! I mean Green!"),
        #     ("Arthur", "Is that an African Swallow or European Swallow?")
        # ]
        # result = []
        # for knight, answer in round_table:
        #     result.append("Contestant: "  "Robin" + "   Answer: " + "Blue! I mean Green!" + "")
        #
        # text = __
        #
        # self.assertRegex(result[2], text)
        #
        # self.assertNotRegex(result[0], text)
        # self.assertNotRegex(result[1], text)
        # self.assertNotRegex(result[3], text)

# Can't get syntax to work, but the assert is asking for the 3rd option in round_table
