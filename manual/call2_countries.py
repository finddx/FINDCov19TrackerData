
import test_2_countries

country_list = []

australia = test_2_countries.TestDefaultSuite()
australia.setup_method()
australia.test_australia()
australia.teardown_method()
australia.vars

country_list.append(australia.vars)

emirates = test_2_countries.TestDefaultSuite()
emirates.setup_method()
emirates.test_unitedArabEmirates()
emirates.teardown_method()
emirates.vars

country_list.append(emirates.vars)

with open("list_data.txt", 'w', encoding="utf-8") as f:
                            for item in country_list:
                                f.write("%s\n" % item)
                            f.close()

