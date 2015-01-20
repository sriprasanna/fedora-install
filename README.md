Fedora Configuration
====================

This is just a reminder repository for myself on how to install Fedora on some of my current setup while I don't create an Ansible playbook.

### COMMON: Update packages and install yum plugin
    sudo yum update -y
    sudo yum install -y yum-plugin-fastestmirror

### COMMON: Install Fedy
    su -c "curl https://satya164.github.io/fedy/fedy-installer -o fedy-installer && chmod +x fedy-installer && ./fedy-installer"

### COMMON: Run select Fedy tasks
    sudo fedy -e rpmfusion_repos font_rendering google_chrome google_talkplugin adobe_flash media_codecs numix_themes config_selinux disk_io_scheduler

### COMMON: Install base packages
    sudo yum install -y @c-development
    sudo yum install -y @development-tools
    sudo yum install -y @container-management
    sudo yum install -y @system-tools
    sudo yum install -y kernel-devel
    sudo yum install -y python-devel python-pip python-virtualenv

### COMMON: Install additional software
    sudo yum install -y htop iotop lm_sensors mercurial smartmontools unrar autojump ansible go java-1.8.0-openjdk ddclient
    sudo yum install -y gnome-tweak-tool gimp rawtherapee calibre deja-dup texlive-scheme-small VirtualBox akmod-VirtualBox
    sudo yum install -y http://s.insynchq.com/builds/insync-1.1.3.32034-1.x86_64.rpm              # installs repo
    sudo yum install -y https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.2_x86_64.rpm         # no repo
    sudo yum install -y https://github.com/atom/atom/releases/download/v0.174.0/atom.x86_64.rpm   # no repo
    git clone https://github.com/sstephenson/rbenv.git ~/.rbenv && git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
    git clone git://github.com/eonpatapon/gnome-shell-extension-caffeine.git && mkdir -p ~/.local/share/gnome-shell/extensions && cp -r gnome-shell-extension-caffeine/caffeine@patapon.info ~/.local/share/gnome-shell/extensions && rm -rf gnome-shell-extension-caffeine

### MBP: Install specific software and config
    export FIRMWARE_INSTALL_DIR="/lib/firmware" && wget http://www.lwfinger.com/b43-firmware/broadcom-wl-5.100.138.tar.bz2 && tar xjf broadcom-wl-5.100.138.tar.bz2 && sudo b43-fwcutter -w "$FIRMWARE_INSTALL_DIR" broadcom-wl-5.100.138/linux/wl_apsta.o && rm -rf broadcom-wl-5.100.138.tar.bz2 broadcom-wl-5.100.138
    sudo yum install -y tlp tlp-rdw
    sudo sed -i 's/^WIFI_PWR_ON_BAT=5/WIFI_PWR_ON_BAT=1/' /etc/default/tlp
    sudo cp files/60-synaptics.conf /etc/X11/xorg.conf.d
    sudo cp files/99-disable-apple-ir.rules /etc/udev/rules.d
    sudo sed -i '/^GRUB_CMDLINE_LINUX=/ s/rhgb/i915.modeset=1 i915.enable_rc6=1 i915.enable_fbc=0 i915.lvds_downclock=1 i915.semaphores=1 libata.force=1:noncq hid_apple.fnmode=2 irqpoll rhgb/' /etc/default/grub
    sudo grub2-mkconfig -o /etc/grub2-efi.cfg

### DESKTOP: Install specific software and config
    sudo yum install -y akmod-nvidia
    sudo cp files/20-nvidia.conf /etc/X11/xorg.conf.d

### COMMON: Enable additional services
    sudo systemctl enable sshd
    sudo systemctl enable docker
    sudo systemctl enable ddclient

### COMMON: GNOME configuration
    # settings
    dconf write /org/gnome/system/location/enabled true
    dconf write /org/gnome/desktop/datetime/automatic-timezone true
    dconf write /org/gtk/settings/file-chooser/clock-format "'12h'"
    dconf write /org/gnome/desktop/interface/icon-theme "'Numix-Circle'"
    dconf write /org/gnome/settings-daemon/peripherals/touchpad/tap-to-click true
    dconf write /org/gnome/settings-daemon/peripherals/touchpad/disable-while-typing true

    # gnome-shell-extensions
    dconf write /org/gnome/shell/enabled-extensions "['caffeine@patapon.info', 'alternate-tab@gnome-shell-extensions.gcampax.github.com']"
    dconf write /org/gnome/shell/window-switcher/current-workspace-only false
    dconf write /org/gnome/shell/extensions/caffeine/show-notifications false

    # gnome-tweak-tools
    dconf write /org/gnome/settings-daemon/plugins/xsettings/hinting "'slight'"
    dconf write /org/gnome/settings-daemon/plugins/xsettings/antialiasing "'rgba'"
    dconf write /org/gnome/desktop/interface/clock-show-date true
    dconf write /org/gnome/desktop/wm/preferences/button-layout "':minimize,maximize,close'"
    dconf write /org/gnome/shell/overrides/dynamic-workspaces false

    # gnome-dock
    dconf write /org/gnome/shell/favorite-apps "['google-chrome.desktop', 'chrome-clhhggbfdinjmjhajaheehoeibfljjno-Default.desktop', 'atom.desktop', 'chrome-hmjkmjkepdijhoojdojkdfohbdgmmhki-Default.desktop', 'gnome-terminal.desktop', 'org.gnome.Nautilus.desktop']"

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
    dconf write /org/gnome/deja-dup/exclude-list "['/home/edgard/.local/share/Trash', '/home/edgard/Downloads', '/home/edgard/Google Drive', '/home/edgard/VirtualBox VMs', '/home/edgard/.cache', '/home/edgard/.nv', '/home/edgard/.adobe', '/home/edgard/.macromedia']"
    dconf write /org/gnome/deja-dup/backend "'file'"
    dconf write /org/gnome/deja-dup/file/path "'file:///home/edgard/Google%20Drive/Backups/lynxarc'"
    dconf write /org/gnome/deja-dup/delete-after 182
    dconf write /org/gnome/deja-dup/periodic-period 1
    dconf write /org/gnome/deja-dup/periodic true

### COMMON: Atom packages
    apm install solarized-dark-ui autocomplete-plus autocomplete-paths atom-terminal sort-lines

### COMMON: Cleanup
    sudo fedy -e rem_oldkernels
