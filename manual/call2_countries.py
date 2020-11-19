
import test_2_countries

country_list = []

algeria = test_2_countries.TestDefaultSuite()
algeria.setup_method()
algeria.test_algeria()
algeria.teardown_method()
algeria.vars

country_list.append(algeria.vars)

other = test_2_countries.TestDefaultSuite()
other.setup_method()
other.test_other()
other.teardown_method()
other.vars

country_list.append(other.vars)

with open("list_data.txt", 'w', encoding="utf-8") as f:
                            for item in country_list:
                                f.write("%s\n" % item)
                            f.close()

