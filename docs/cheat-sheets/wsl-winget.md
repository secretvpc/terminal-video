# WSL and Winget Universal Cheat Sheet

This document provides an end-to-end technical reference for managing Ubuntu-based WSL environments using Winget and WSL tooling in Windows 11. It covers installation, export/import, user configuration, network diagnostics, and integration with Windows Terminal. All guidance is structured, precise, and suitable for professional use.

---

## Winget: Installing Ubuntu Distributions

### Search for available Ubuntu variants

```powershell
winget search Ubuntu
```

### Install a specific Ubuntu version

```powershell
winget install --id Canonical.Ubuntu.2204
winget install --id 9NZ3KLHXDJP5 --source msstore  # Ubuntu 24.04.1 LTS
```

### View installed packages

```powershell
winget list
```

Note: Winget installations register Ubuntu distributions with default names such as "Ubuntu" or "Ubuntu-22.04". To assign a custom name, use the `wsl --export` and `wsl --import` method.

---

## WSL: Core Operations

### Remove and Unregister a Distribution

To fully delete and deregister a WSL distribution:

1. Shut it down if it's running:

```powershell
wsl --terminate <DistributionName>
```

2. Unregister and delete all associated data:

```powershell
wsl --unregister <DistributionName>
```

Note: This permanently removes the distribution and deletes its file system.

### List installed distributions

```powershell
wsl --list --verbose
```

### Start a specific distribution

```powershell
wsl -d <DistributionName>
```

### Set default distribution

```powershell
wsl --set-default <DistributionName>
```

### Set WSL version

```powershell
wsl --set-version <DistributionName> 2
```

### Shutdown all running instances

```powershell
wsl --shutdown
```

### Delete a distribution

```powershell
wsl --unregister <DistributionName>
```

---

## Export and Import for Custom Naming

### Export an existing distribution

```powershell
wsl --export <SourceName> C:\WSL\ubuntu-export.tar
```

### Import under a custom name

```powershell
wsl --import <NewName> C:\WSL\<Folder> C:\WSL\ubuntu-export.tar --version 2
```

You can register multiple independent WSL distributions using this method.

---

## Ubuntu Not Visible After Installation

If the distribution does not appear in `wsl --list` after a winget or Store installation:

1. Locate the app executable:

```powershell
Get-StartApps | Where-Object { $_.Name -like "*Ubuntu*" }
```

2. Launch manually:

```powershell
explorer.exe "shell:AppsFolder\CanonicalGroupLimited.Ubuntu24.04onWindows_...!App"
```

3. If unresolved, remove and reinstall:

```powershell
Get-AppxPackage *Ubuntu24.04* | Remove-AppxPackage
winget install --id 9NZ3KLHXDJP5 --source msstore
```

---

## User Management and Default Shell

### Create and switch to a new user

```bash
adduser <username>
usermod -aG sudo <username>
```

### Set as default user

Create or edit `/etc/wsl.conf`:

```ini
[user]
default=<username>
```

Then restart WSL:

```powershell
wsl --shutdown
```

---

## Windows Terminal Integration

### Sample profile entry in settings.json

```json
{
  "guid": "{generated-guid}",
  "name": "custom-ubuntu",
  "tabTitle": "Ubuntu Custom",
  "commandline": "wsl.exe -d custom-ubuntu -u <username>",
  "startingDirectory": "//wsl$/custom-ubuntu/home/<username>",
  "cursorShape": "filledBox",
  "font": {
    "face": "Cascadia Mono",
    "size": 13
  },
  "icon": "https://assets.ubuntu.com/v1/49a1a858-favicon-32x32.png",
  "hidden": false
}
```

To access the configuration file:

```powershell
notepad "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
```

---

## Network and Hostname Configuration

### Show hostname

```bash
hostname
```

### Show network configuration

```bash
ip addr
```

### Change hostname temporarily

```bash
sudo hostnamectl set-hostname <hostname>
```

### Make hostname change persistent

Edit `/etc/hostname` and `/etc/hosts`, then restart WSL:

```powershell
wsl --shutdown
```

---

## Best Practices Summary

* Use `wsl --export` and `--import` to control naming and duplication.
* Avoid default names to prevent conflicts across environments.
* Always define a non-root user and configure it in `wsl.conf`.
* Set `startingDirectory` in Windows Terminal profiles for clean navigation.
* Use structured folders for exported images and distributions.
* Combine `wsl`, `winget`, and PowerShell to automate full workflows.

End of reference.
