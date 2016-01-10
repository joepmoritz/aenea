# This file is part of Aenea
#
# Aenea is free software: you can redistribute it and/or modify it under
# the terms of version 3 of the GNU Lesser General Public License as
# published by the Free Software Foundation.
#
# Aenea is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Aenea.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (2014) Alex Roper
# Alex Roper <alex@aroper.net>

'''Contains generic utility data and functions useful when writing grammars.'''

try:
    import dragonfly
except ImportError:
    import dragonfly_mock as dragonfly

import configuration

LOWERCASE_LETTERS = configuration.make_grammar_commands('misc', {
    'A': 'a',
    'B': 'b',
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'H': 'h',
    'I': 'i',
    'J': 'j',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'O': 'o',
    'P': 'p',
    'Q': 'q',
    'R': 'r',
    'S': 's',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'X': 'x',
    'Y': 'y',
    'Z': 'z',
    }, 'letters.lower')

UPPERCASE_LETTERS = configuration.make_grammar_commands('misc', {
    'upper A': 's-a',
    'upper B': 's-b',
    'upper C': 's-c',
    'upper D': 's-d',
    'upper E': 's-e',
    'upper F': 's-f',
    'upper G': 's-g',
    'upper H': 's-h',
    'upper I': 's-i',
    'upper J': 's-j',
    'upper K': 's-k',
    'upper L': 's-l',
    'upper M': 's-m',
    'upper N': 's-n',
    'upper O': 's-o',
    'upper P': 's-p',
    'upper Q': 's-q',
    'upper R': 's-r',
    'upper S': 's-s',
    'upper T': 's-t',
    'upper U': 's-u',
    'upper V': 's-v',
    'upper W': 's-w',
    'upper X': 's-x',
    'upper Y': 's-y',
    'upper Z': 's-z'
    }, 'letters.upper')

DIGITS = configuration.make_grammar_commands('misc', {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
    }, 'digits')

LETTERS = LOWERCASE_LETTERS.copy()
LETTERS.update(UPPERCASE_LETTERS)

ALPHANUMERIC = LETTERS.copy()
ALPHANUMERIC.update(DIGITS)


class DigitalInteger(dragonfly.Repetition):
    '''An integer element spelled digit by digit (eg, enter 50 by saying
       'five zero'. Useful in places where Dragon would complain of the
       grammar's complexity if regular integers were used. min and max are
       number of digits, not value of the number.'''
    child = dragonfly.Choice('digit', DIGITS)

    def __init__(self, name, min, max, *args, **kw):
        dragonfly.Repetition.__init__(
            self,
            self.child,
            min,
            max,
            name=name,
            *args,
            **kw
            )

    def value(self, node):
        return int(''.join(dragonfly.Repetition.value(self, node)))
