

logo="\033[01;33m
  ___  _ __   ___\033[01;31m__  __
\033[01;33m 033[01;31m
\033[01;33m MCHACKC++ 033[01;31m
\033[01;33m 033[01;31m
"
prompt="\007\033[00m[\033[01;34monex\033[00m@\033[01;34mspace\033[00m]$"

# checking for system home dir
if [ -d $HOME ]; then
  home=$HOME
else
  home="~/"
fi

# checking for system bin dir
if [ -d /data/data/com.termux/files/usr/bin ]; then
  bin="/data/data/com.termux/files/usr/bin"
elif [ -d /usr/local/bin ]; then
  bin="/usr/local/bin"
elif [ -d /bin ]; then
  bin="/bin"
elif [ -d /sbin ]; then
  bin="/sbin"
fi

# checking for configuration dir
if [ -d /data/data/com.termux/files/usr/etc ]; then
  conf_dir="/data/data/com.termux/files/usr/etc"
elif [ -d /etc ]; then
  conf_dir="/etc"
fi

# configuration files
if [ -d $conf_dir/onex ]; then
  if [ -e $conf_dir/onex/data/tools.dat ]; then
    tools_data="$conf_dir/onex/data/tools.dat"
  fi
  if [ -e $conf_dir/onex/data/category.dat ]; then
    category_data="$conf_dir/onex/data/category.dat"
  fi
else
  if [ -e data/tools.dat ]; then
    tools_data="data/tools.dat"
  fi
  if [ -e data/category.dat ]; then
    category_data="data/category.dat"
  fi
fi

# checking for system root access
if [ -e /usr/lib/sudo ]; then
  sudo="sudo"
elif [ -e /usr/bin/sudo ]; then
  sudo="sudo"
elif [ -e /usr/sbin/sudo ]; then
  sudo="sudo"
elif [ -e /lib/sudo ]; then
  sudo="sudo"
elif [ -e /bin/sudo ]; then
  sudo="sudo"
elif [ -e /sbin/sudo ]; then
  sudo="sudo"
elif [ -e /data/data/com.termux/files/usr/bin/sudo ]; then
  sudo="sudo"
else
  sudo=""
fi

# checking for system package manager
if [ -e /bin/apt ]; then
  pac="apt-get"
  system="linux"
elif [ -e /bin/apt-get ]; then
  pac="apt-get"
  system="linux"
elif [ -e /usr/bin/apt-get ]; then
  pac="apt-get"
  system="linux"
elif [ -e /sbin/apt-get ]; then
  pac="apt-get"
  system="linux"
elif [ -e /usr/sbin/apt-get ]; then
  pac="apt-get"
  system="linux"
elif [ -e /bin/apk ]; then
  pac="apk"
  system="linux"
elif [ -e /usr/bin/apk ]; then
  pac="apk"
  system="linux"
elif [ -e /sbin/apk ]; then
  pac="apk"
  system="linux"
elif [ -e /usr/sbin/apk ]; then
  pac="apk"
  system="linux"
elif [ -e /bin/yum ]; then
  pac="yum"
  system="fedora"
elif [ -e /usr/bin/yum ]; then
  pac="yum"
  system="fedora"
elif [ -e /sbin/yum ]; then
  pac="yum"
  system="fedora"
elif [ -e /usr/sbin/yum ]; then
  pac="yum"
  system="fedora"
elif [ -e /usr/local/bin/brew ]; then
  pac="brew"
  system="mac"
  sudo=""
elif [ -e /data/data/com.termux/files/usr/bin/pkg ]; then
  pac="pkg"
  system="termux"
elif [ -e /data/data/com.termux/files/usr/bin/apt ]; then
  pac="apt"
  system="termux"
elif [ -e /data/data/com.termux/files/usr/bin/apt-get ]; then
  pac="apt-get"
  system="termux"
fi

# install tools
install() {
  # get tool alias name
  tool_name=`grep '.' $tools_data | sort -f | sed -n "$1p" | cut -d"|" -f1`
  # get tool package manager
  tool_installer=`grep '.' $tools_data | sort -f | sed -n "$1p" | cut -d"|" -f5`
  # tool dependency (requirements)
  tool_dependency=`grep '.' $tools_data | sort -f | sed -n "$1p" | cut -d"|" -f6 | tr ' ' ','`
  # tool url
  tool_url=`grep '.' $tools_data | sort -f | sed -n "$1p" | cut -d"|" -f4`
  # package name or tool name
  tool_pac=`grep '.' $tools_data | sort -f | sed -n "$1p" | cut -d"|" -f2`
  # check tool name is null or not
  if [ "$tool_name" ]; then

    # for default package
    if [ $tool_installer = "package_manager" ]; then
      # check tool is already installed or not
      if [ ! -e $bin/$tool_pac ]; then
        # check sudo is null or not
        if [ $sudo ]; then
          #check user is online or not
          wget -q --spider http://google.com
          if [ $? -eq 0 ]; then
            echo "\033[01;32mInstalling ...\033[00m"
            sleep 1
            # install tool dependency
            if [ $tool_dependency != "null" ]; then
              for dep_name in `ec