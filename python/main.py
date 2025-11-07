import sys
import hal_simplicity_py as pyhalsim

def main1():
    pyhalsim.setup_logger("debug")

    modulename = "pyhalsim"
    funcname = "run_cli_command"

    if hasattr(pyhalsim, funcname) and callable(getattr(pyhalsim, funcname)):
        cli_args = sys.argv[1:]
        cmdline = " ".join(cli_args)
        ret = pyhalsim.run_cli_command(cmdline)
    else:
        print(f"Could not find 'run_cli_command' in module '{modulename}'.")

    # activate this to print all logs
    # print(pyhalsim.get_logs(), flush=True)

if __name__ == "__main__":
    main1()
    
