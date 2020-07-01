get_stage("install") %>%
  add_step(step_install_github("dsbbfindx/FIND_COV_19_Tracker@r-package"))

get_stage("before_deploy") %>%
  add_step(step_setup_push_deploy())

get_stage("deploy") %>%
  add_code_step(FindCovTracker::process_jhu_data(), prepare_call = TRUE) %>%
  add_code_step(FindCovTracker::process_test_data(), prepare_call = TRUE) %>%
  add_step(step_do_push_deploy(commit_paths = c(
    "processed/coronavirus.csv",
    "processed/coronavirus_tests.csv",
    "processed/jhu_data.csv"
  )))
