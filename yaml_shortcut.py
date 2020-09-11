import sys
import yaml
import subprocess
import webbrowser
import urllib.parse

def main(config_fn, methods):
    with open(config_fn, 'r') as cf:
        cfg = yaml.safe_load(cf)
    print(cfg)
    for method, values in cfg.items():
        for params in values:
            methods[method](params)

    # subprocess.run(['explorer.exe', cfg['dirs'][0]])
    # webbrowser.open('vscode://file/' + cfg['dirs'][0])

def open_dir(params):
    # subprocess.run(['explorer.exe', cfg['dirs'][0]])
    pass

def open_vscode(params):
    # webbrowser.open('vscode://file/' + cfg['dirs'][0])
    pass

def open_fluent_terminal(params):
    cmd = r"C:\Windows\System32\cmd.exe /k " + ' & '.join(params['run'])
    uri = "ftcmd://fluent.terminal/?cmd={}&conpty=True&buffer=True".format(urllib.parse.quote_plus(cmd))
    webbrowser.open(uri)

if __name__ == "__main__":
    methods = {
        "dirs": open_dir,
        "vscode": open_vscode,
        "fluent_terminal": open_fluent_terminal
    }
    main(sys.argv[1], methods)