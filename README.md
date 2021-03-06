# Yaml Shortcut

> Create Windows desktop shortcuts using YAML.

## What It Looks Like

![kicNC26j55](https://user-images.githubusercontent.com/6625384/93635158-71b15580-f9b7-11ea-8ec2-04a273b7860a.gif)

## Install

1. Create a shortcut file (ex. `my-project.ys`) and add configure the shortcuts you want to use.

```
dirs:
  - C:\Dev\sshh12\yaml-shortcut
vscode:
  - C:\Dev\sshh12\yaml-shortcut
url:
  - https://github.com/sshh12/yaml-shortcut
fluent_terminal:
  - name: Dev Terminal
    run:
      - call C:\Dev\bin\setup-cmd.bat
      - cd C:\Dev\sshh12\yaml-shortcut
      - activate yaml-shortcut
cmd:
  - name: Dev Cmd
    run:
      - call C:\Dev\bin\setup-cmd.bat
      - cd C:\Dev\sshh12\yaml-shortcut
      - activate yaml-shortcut
meta:
  name: 'Yaml Shortcut'
```

2. Download and unzip the latest release [yaml_shortcut.zip](https://github.com/sshh12/yaml-shortcut/releases)
3. Double-click the shortcut and choose to open with `yaml_shortcut.exe`

## Adding to Windows Menu

Create `~/.yaml_shortcut.yaml`:

```
dirs:
  - "%CWD%"
vscode:
  - "%CWD%"
fluent_terminal:
  - name: Dev Terminal
    run:
      - cd "%CWD%"
meta:
  name: "%CWD%"
```

Open the Windows Registry Editor and add these entries (change `...` to install path):

```
[HKEY_CLASSES_ROOT\Directory\Background\shell\yamlshortcut]
@="Open Dev Here"
"Icon"="...\\yaml_shortcut.exe"

[HKEY_CLASSES_ROOT\Directory\Background\shell\yamlshortcut\command]
@="...\\yaml_shortcut.exe \"%V\""
```
