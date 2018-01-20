import sys
from modules import command_work


def main(argv):
    wk = command_work.CommandWork(argv)

    cmd_list = [
        "help",
        "install",
        "uninstall",
        "remove",
        "search",
        "list",
        "show",
        "help",
        "addserver",
        "removeserver",
        "regserver",
        "loginaccount",
        "gui",
    ]
    for cmd in cmd_list:
        if argv[0] == cmd:
            eval("wk." + cmd)()

    # Not in command list:
    if argv[0] not in cmd_list:
        wk.help()


if __name__ == "__main__":
    main(sys.argv[1:])
