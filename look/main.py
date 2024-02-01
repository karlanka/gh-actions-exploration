import looker_sdk


# add variables to env variables, looker sdk use these for auth
# os.environ["LOOKERSDK_BASE_URL"] = Variable.get(
#     "system_activity_looker_base_url", default_var=""
# )
# os.environ["LOOKERSDK_CLIENT_ID"] = Variable.get(
#     "system_activity_looker_client_id", default_var=""
# )
# os.environ["LOOKERSDK_CLIENT_SECRET"] = Variable.get(
#     "system_activity_looker_client_secret", default_var=""
# )


def deploy_branch():
    sdk = looker_sdk.init40()
    results = sdk.deploy_ref_to_production(
        project_id="anton_prototyping_prod", branch="dev-anton-karling-whpn"
    )
    print(len(results))


deploy_branch()
