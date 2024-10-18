#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule                                                                                                                                                                                                     # type: ignore

def manage_user(module, username, state):
    if state == 'present':
        cmd = "useradd " + username
        result = module.run_command(cmd, check_rc=True)
        return result
    elif state == 'absent':
        cmd = "userdel " + username
        result = module.run_command(cmd, check_rc=True)
        return result
    else:
        module.fail_json(msg="Invalid state. Use 'present' or 'absent'.")

def main():
    module = AnsibleModule(
        argument_spec=dict(
            username=dict(required=True, type='str'),
            state=dict(required=True, choices=['present', 'absent'])
        )
    )

    username = module.params['username']
    state = module.params['state']

    result = manage_user(module, username, state)

    if state == 'present':
        module.exit_json(changed=True, msg="User created successfully.")
    elif state == 'absent':
        module.exit_json(changed=True, msg="User deleted successfully.")

if __name__ == '__main__':
    main()
