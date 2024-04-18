from config import chkpt, group_id
from chkp_harmony_endpoint_management_sdk import HarmonyEndpoint, InfinityPortalAuth


def init_harmony():

    # Create a new instance of HarmonyEndpoint
    he = HarmonyEndpoint()

    # Connect to management using CloudInfra API credentials
    he.connect(infinity_portal_auth=InfinityPortalAuth(
            client_id=chkpt['client_id'], 
            access_key= chkpt['secret_key'], 
            gateway= chkpt['main_url']
        )) 
    return he

if __name__=='__main__':

    he = init_harmony()

    # DEBUG="harmony-endpoint-management:*"

    # User
    user = ['test testov'] # test.test

    # Add user to Virtual group
    org_metadata_res = he.organizational_structure_api.add_members_to_virtual_group(
        body=user,
        header_params={ "x-mgmt-run-as-job": 'on'},
        path_params={"virtualGroupId" : group_id}
    )


    print(org_metadata_res.is_job)
    print(org_metadata_res.payload)


    # Once finish, disconnect to stop all background session management. 
    he.disconnect()