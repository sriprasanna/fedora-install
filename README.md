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
    dconf write /org/gnome/shell/favorite-apps "['google-chrome.desktop', 'chrome-clhhggbfdinjmjhajaheehoeibfljjno-Default.desktop', 'chrome-https___web.whatsapp.com_.desktop', 'california.desktop', 'chrome-hmjkmjkepdijhoojdojkdfohbdgmmhki-Default.desktop', 'atom.desktop', 'gnome-terminal.desktop', 'org.gnome.Nautilus.desktop']"

    # gnome-terminal
    dconf write /org/gnome/terminal/legacy/new-terminal-mode "'tab'"
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)use-system-font" false
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)font" "'PragmataPro 12'"
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)login-shell" true
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)use-theme-colors" false
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)foreground-color" "'rgb(131,148,150)'"
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)background-color" "'rgb(0,43,54)'"
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)palette" "['rgb(7,54,66)', 'rgb(220,50,47)', 'rgb(133,153,0)', 'rgb(181,137,0)', 'rgb(38,139,210)', 'rgb(211,54,130)', 'rgb(42,161,152)', 'rgb(238,232,213)', 'rgb(0,43,54)', 'rgb(203,75,22)', 'rgb(88,110,117)', 'rgb(101,123,131)', 'rgb(131,148,150)', 'rgb(108,113,196)', 'rgb(147,161,161)', 'rgb(253,246,227)']"

    # deja-dup
    dconf write /org/gnome/deja-dup/include-list "['/home/edgard']"
    dconf write /org/gnome/deja-dup/exclude-list "['/home/edgard/.local/share/Trash', '/home/edgard/Downloads', '/home/edgard/Google Drive', '/home/edgard/VirtualBox VMs', '/home/edgard/.cache']"
    dconf write /org/gnome/deja-dup/backend "'file'"
    dconf write /org/gnome/deja-dup/file/path "'file:///home/edgard/Google%20Drive/Backups/lynxarc'"
    dconf write /org/gnome/deja-dup/delete-after 182
    dconf write /org/gnome/deja-dup/periodic-period 1
    dconf write /org/gnome/deja-dup/periodic true

### Post-Install: Atom packages
    apm install atom-beautify atom-terminal autocomplete-plus autocomplete-paths color-picker file-icons linter linter-pylint merge-conflicts solarized-dark-ui sort-lines
    sudo yum install pylint python-autopep8 nodejs-js-yaml
