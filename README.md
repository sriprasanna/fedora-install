Install Fedora 21
-------------------------
First time:
> sudo su -

> ssh-keygen -t rsa -C "root"

> cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys

> chmod 600 ~/.ssh/authorized_keys

Available tags: **_macbook_**

Example local run (also for updates):
> sudo ansible-playbook /path/to/ansible/folder/site.yml --tags "macbook" -i 'localhost,'

Example remote run - sshd must be started on remote:
> sudo ansible-playbook /path/to/ansible/folder/site.yml --tags "macbook" -i '192.168.25.107,' -k -K

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

    # gnome-tweak-tools - You can choose different icons from Numix project
    dconf write /org/gnome/desktop/interface/icon-theme "'Numix-Circle'"
    dconf write /org/gnome/settings-daemon/plugins/xsettings/hinting "'slight'"
    dconf write /org/gnome/settings-daemon/plugins/xsettings/antialiasing "'rgba'"
    dconf write /org/gnome/desktop/interface/clock-show-date true
    dconf write /org/gnome/desktop/wm/preferences/button-layout "':minimize,maximize,close'"
    dconf write /org/gnome/shell/overrides/dynamic-workspaces false

    # gnome-dock (to add your favorites to dock)
    dconf write /org/gnome/shell/favorite-apps "['google-chrome.desktop', 'atom.desktop', 'gnome-terminal.desktop', 'org.gnome.Nautilus.desktop']"

    # gnome-terminal
    dconf write /org/gnome/terminal/legacy/new-terminal-mode "'tab'"
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)use-system-font" false
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)font" "'PragmataPro 12'"
    dconf write "/org/gnome/terminal/legacy/profiles:/$(dconf list /org/gnome/terminal/legacy/profiles:/ | sed s/^\'// | sed s/\'$//)login-shell" true

