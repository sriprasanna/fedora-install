Install Fedora 21 Desktop
-------------------------
Available tags: **_desktop_**, **_macbook_**, **_htpc_**

Example local run:
> ansible-playbook site.yml --tags "desktop" -i 'localhost,'

Example remote run - sshd must be started on remote:
> ansible-playbook site.yml --tags "macbook" -i '192.168.25.107,' -k -K

**IMPORTANT: DO NOT FORGET THE COMMA AFTER THE HOST**

### Post-Install: GNOME configuration
    # settings
    dconf write /org/gnome/system/location/enabled true
    dconf write /org/gnome/desktop/datetime/automatic-timezone true
    dconf write /org/gtk/settings/file-chooser/clock-format "'12h'"
    dconf write /org/gnome/settings-daemon/peripherals/touchpad/tap-to-click true
    dconf write /org/gnome/settings-daemon/peripherals/touchpad/disable-while-typing true

    # gnome-shell-extensions
    dconf write /org/gnome/shell/enabled-extensions "['caffeine@patapon.info', 'alternate-tab@gnome-shell-extensions.gcampax.github.com']"
    dconf write /org/gnome/shell/window-switcher/current-workspace-only false
    dconf write /org/gnome/shell/extensions/caffeine/show-notifications false

    # gnome-tweak-tools
    dconf write /org/gnome/desktop/interface/icon-theme "'Numix-Circle'"
    dconf write /org/gnome/settings-daemon/plugins/xsettings/hinting "'slight'"
    dconf write /org/gnome/settings-daemon/plugins/xsettings/antialiasing "'rgba'"
    dconf write /org/gnome/desktop/interface/clock-show-date true
    dconf write /org/gnome/desktop/wm/preferences/button-layout "':minimize,maximize,close'"
    dconf write /org/gnome/shell/overrides/dynamic-workspaces false

    # gnome-dock
    dconf write /org/gnome/shell/favorite-apps "['google-chrome.desktop', 'chrome-clhhggbfdinjmjhajaheehoeibfljjno-Default.desktop', 'chrome-bgkodfmeijboinjdegggmkbkjfiagaan-Default.desktop', 'chrome-hmjkmjkepdijhoojdojkdfohbdgmmhki-Default.desktop', 'atom.desktop', 'terminator.desktop', 'org.gnome.Nautilus.desktop']"

### Post-Install: Atom packages
    apm install atom-beautify autocomplete-plus autocomplete-paths color-picker linter linter-pylint linter-js-yaml merge-conflicts sort-lines terminal-panel
    sudo yum install pylint python-autopep8 nodejs-js-yaml
