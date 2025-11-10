import sys
import pyhalsimplicity

def main1():
    pyhalsimplicity.setup_logger("info")
    modulename = "pyhalsimplicity"
    funcname = "run_cli_command"

    if hasattr(pyhalsimplicity, funcname) and callable(getattr(pyhalsimplicity, funcname)):
        cli_args = sys.argv[1:]
        cmdline = " ".join(cli_args)
        ret = pyhalsimplicity.run_cli_command(cmdline)
        print(ret)
    else:
        print(f"Could not find 'run_cli_command' in module '{modulename}'.")

    # activate this to print all logs
    # print(pyhalsim.get_logs(), flush=True)

if __name__ == "__main__":
    main1()
    
