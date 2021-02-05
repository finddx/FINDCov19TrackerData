get_stage("before_deploy") %>%
  add_step(step_setup_ssh()) %>%
  add_step(step_setup_push_deploy())

get_stage("deploy") %>%
  add_step(step_install_github("dsbbfinddx/FINDCov19Tracker")) %>%
  # FIXME https://github.com/dsbbfinddx/FINDCov19TrackerData/issues/30
  add_code_step(remotes::install_version("dplyr", "1.0.3")) %>%
  add_code_step(FINDCov19Tracker::create_shiny_data(), prepare_call = TRUE) %>%
  add_step(step_do_push_deploy(commit_paths = c(
    "processed/coronavirus_cases.csv",
    "processed/coronavirus_tests.csv",
    "issues/coronavirus_tests_new_negative.csv",
    "processed/jhu_data.csv",
    "processed/data_all.csv",
    "processed/unit_info.csv"
  )))
