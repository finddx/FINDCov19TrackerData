#!/usr/bin/env python3
import argparse
import concurrent.futures
from test import TestDefaultSuite


def run_one_country(country):
    suite = TestDefaultSuite()
    suite.setup_method()
    getattr(suite, 'test_' + country)()
    return suite.vars


if __name__ == '__main__':
    countries = []
    for m in dir(TestDefaultSuite):
        if m.startswith('test_'):
            countries.append(m[5:])
    parser = argparse.ArgumentParser(
        description='Run all or some tests.',
        epilog="If countries list omitted, will run tests for all countries.")
    parser.add_argument('countries',
                        nargs='*',
                        metavar='country',
                        choices=countries + [[]],
                        help='Country name')
    country_list = []
    args = parser.parse_args()
    if args.countries:
        # check specified country names are valid
        for country in args.countries:
            country_list.append(run_one_country(country))
    else:
        # run all countries in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            country_list = executor.map(run_one_country, countries)
    with open("list_data.txt", 'w', encoding="utf-8") as f:
        for item in country_list:
            f.write("%s\n" % item)
        f.close()
