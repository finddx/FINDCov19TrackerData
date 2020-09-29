get_stage("before_deploy") %>%
  add_step(step_setup_ssh()) %>%
  add_step(step_setup_push_deploy())

get_stage("deploy") %>%
  add_step(step_install_github("dsbbfinddx/FINDCov19Tracker")) %>%
  add_code_step(FINDCov19Tracker::create_shiny_data(), prepare_call = TRUE) %>%
  add_step(step_do_push_deploy(commit_paths = c(
    "processed/coronavirus_cases.csv",
    "processed/coronavirus_tests.csv",
    "processed/jhu_data.csv",
    "processed/data_all.csv",
    "processed/unit_info.csv"
  )))
