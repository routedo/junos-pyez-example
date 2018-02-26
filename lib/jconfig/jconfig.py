"""
Configure a Juniper network device.
"""

import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import CommitError, LockError, UnlockError

def juniper_config_commit(dev, file_location):
    '''
    This function is used to configure a Juniper network device.

    dev = Juniper device connection
    file_location = Location of configuration changes to push.  Changes should be in the set format.
    '''

    try:
        cfg = Config(dev)
        print("\n" + "!!!!!  Locking the configuration   !!!!!")
        cfg.lock()

        print('\n' + '!!!!! Pushing changes to device ' + str(dev.hostname) + '   !!!!!' +'\n' + '\n')
        cfg.load(path=file_location, format="set")

        with open(file_location) as config_to_commit:
            print('###############################################################################' + '\n' + '\n')
            for line in config_to_commit:
                print(line)
            print('\n' + '\n' + '###############################################################################')

        commit_check = input("\n" + "Are you sure you want to commit changes to the device" + "\n" + "n/Y:")

        if commit_check.lower().strip() == 'y':
            cfg.commit(comment="Commit configuration", confirm=2)

            confirm_check = input("\n" + "Please confirm commit.  Device config will rollback in 2 minutes unless confirmed." + "\n" + "n/Y:")

            if confirm_check.lower().strip() == 'y':
                cfg.commit()
                print('\n' +"!!!!! Commit Confirmed   !!!!!")

            else:
                cfg.unlock()
                sys.exit('!!!!! Warning !!!!!!' + '\n' + 'Device config will rollback in 2 minutes.')

        else:
            cfg.rollback(0)
            print('\n' + 'Changes have been rolled back')
            print('\n' + "!!!!! Unlocking the configuration   !!!!!" +'\n')
            cfg.unlock()
            dev.close()
            sys.exit(1)

        print('\n' + "!!!!! Unlocking the configuration   !!!!!" +'\n')

        cfg.unlock()

    except CommitError as error:
        print('\n' + "!!!!!!!!!!  Config Error !!!!!!!!!!")
        print('\n' + str(error))
        print('\n' + "!!!!!!!!!!  Attempting to rollback config !!!!!!!!!!")
        cfg.rollback(0)
        cfg.unlock()
        dev.close()
        sys.exit(1)
        return

    except LockError as error:
        print('\n' + "Error: Unable to lock configuration")
        dev.close()
        sys.exit(1)
        return

    except UnlockError:
        print('\n' + "Error: Unable to unlock configuration")
        dev.close()
        sys.exit(1)
        return

    except Exception as err:
        print(err)
        dev.close()
        sys.exit(1)
        return

    return
