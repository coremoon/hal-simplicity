import sys
import pyhalsimplicity

def main():
    # Setup logging (optional)
    pyhalsimplicity.setup_logger("info")
    
    # Prepare the CLI command as a space-separated string
    cli_args = sys.argv[1:]
    cmdline = " ".join(cli_args)
    
    # Execute the command
    result = pyhalsimplicity.run_cli_command(cmdline)
    
    print(result)

    # Uncomment to see the internal logger buffer
    # print(pyhalsimplicity.get_logs(), flush=True)

if __name__ == "__main__":
    main()