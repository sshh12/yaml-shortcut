"""
yaml_shortcut
"""
import sys
import urllib.parse
import PySimpleGUI as sg
import subprocess
import webbrowser
import yaml


def main(config_fn, methods):
    with open(config_fn, "r") as cf:
        cfg = yaml.safe_load(cf)
    cfg.setdefault("meta", {})
    meta = cfg["meta"]
    name = meta.get("name", "Yaml Shortcut")
    del cfg["meta"]
    sg.theme("Material2")
    layout = []
    handlers = {}
    for method, values in cfg.items():
        for params in values:
            if isinstance(params, dict) and "name" in params:
                item = params["name"]
            else:
                item = method + " " + str(params)
            layout.append([sg.Text(item), sg.Button("Open", key=item)])

            def _open(method=method, params=params):
                methods[method](params)

            handlers[item] = _open
    window = sg.Window(name, layout)
    while True:
        event, values = window.read()
        if event in handlers:
            handlers[event]()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break

    window.close()


def open_dir(params):
    subprocess.run(["explorer.exe", params])


def open_vscode(params):
    webbrowser.open("vscode://file/" + params)


def open_fluent_terminal(params):
    cmd = r"C:\Windows\System32\cmd.exe /k " + " & ".join(params["run"])
    uri = "ftcmd://fluent.terminal/?cmd={}&conpty=True&buffer=True".format(urllib.parse.quote_plus(cmd))
    webbrowser.open(uri)


if __name__ == "__main__":
    open_methods = {"dirs": open_dir, "vscode": open_vscode, "fluent_terminal": open_fluent_terminal}
    main(sys.argv[1], open_methods)
