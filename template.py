#! /usr/bin/env python
# -*- coding: utf-8 *-*

from optparse import OptionParser

import fileinput
import logging
import sys
import os

if __name__ == '__main__':
    parser = OptionParser(usage=u'usage: %prog [options]')
    parser.add_option('-o', '--output', dest='output', metavar="FILE",
                      help=u"Write output in file")
    parser.add_option('-v', '--verbose', dest='verbose', action="store_true",
                      default=False, help=u"Verbose mode")
    parser.add_option('-d', '--debug', dest='debug', action="store_true",
                      default=False, help=u"Debug mode")
    parser.add_option('-n', '--dry-run', dest='dryrun', action="store_true",
                      default=False, help="Do not really perform action")

    (options,args) = parser.parse_args()

    if options.output:
        output = open(options.output, 'w')
    else:
        output = sys.stdout

    loglvl = logging.NOTICE if option.verbose else logging.INFO
    loglvl = logging.DEBUG if option.debug else logging.INFO
    logging.basicConfig(level=loglvl,
                        format="%(asctime)s %(name)8s %(levelname)5s: %(message)s")
    daemonlog = logging.getLogger(sys.argv[0])

