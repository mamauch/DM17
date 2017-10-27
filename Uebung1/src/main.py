# -*- coding: utf-8 -*-
# Main file

def main():
    import sys
    from optparse import OptionParser
    from apriori import runApriori, dataFromFile, printResults

    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing csv',
                         default=None)
    optparser.add_option('-s', '--minSupport',
                         dest='minS',
                         help='minimum support value',
                         default=0.4,
                         type='float')

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = dataFromFile(options.input)
    else:
        print ('No dataset filename specified, system with exit\n')
        sys.exit('System will exit')

    minSupport = options.minS

    items = runApriori(inFile, minSupport)

    printResults(items, minSupport, options.input.split("/")[2])


if __name__ == "__main__":
    import profile
    import sys

    if sys.argv[1] == str(0):
        main()
    elif sys.argv[1] == str(1):
        profile.run('main()')

