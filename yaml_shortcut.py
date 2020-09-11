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
            layout.append([sg.Button("Open", key=item), sg.Text(item)])

            def _open(method=method, params=params):
                methods[method](params)

            handlers[item] = _open
    layout.append([sg.Button("Open All", key="open-all")])

    def _open_all():
        for method, values in cfg.items():
            for params in values:
                methods[method](params)

    handlers["open-all"] = _open_all
    window = sg.Window(name, layout)
    while True:
        event, values = window.read()
        if event in handlers:
            handlers[event]()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break

    window.close()


def show_error_gui(reason):
    sg.theme("Material2")
    layout = [[sg.Text(reason)]]
    window = sg.Window("Yaml Shortcut", layout)
    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
    window.close()


def open_dir(params):
    subprocess.run(["explorer.exe", params])


def open_vscode(params):
    webbrowser.open("vscode://file/" + params)


def open_url(params):
    webbrowser.open(params)


def open_fluent_terminal(params):
    cmd = r"C:\Windows\System32\cmd.exe /k " + " & ".join(params["run"])
    uri = "ftcmd://fluent.terminal/?cmd={}&conpty=True&buffer=True".format(urllib.parse.quote_plus(cmd))
    webbrowser.open(uri)


if __name__ == "__main__":
    open_methods = {"dirs": open_dir, "url": open_url, "vscode": open_vscode, "fluent_terminal": open_fluent_terminal}
    try:
        main(sys.argv[1], open_methods)
    except Exception as e:
        show_error_gui(repr(e))
