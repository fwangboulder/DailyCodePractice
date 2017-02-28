Your own Linux box
To learn the Linux shell, you need a Linux machine to run it on. But we can't really ship a new Linux computer to every one of you. So instead you will set up a Linux virtual machine (VM) on your own computer.

You'll be using the VirtualBox application to run the virtual machine, and the vagrant software to configure it.

This virtual-machine setup is very similar to the ones you will use in later Udacity courses on the Linux platform. So when you get to those courses, you will not need to re-install this software.

Setting the virtual machine up is not complicated, but it will take some time when your computer downloads the Linux OS. Follow the instructions below to set it up before proceeding on in this course.

What's a virtual machine?
A virtual machine is a program that runs on your Windows or Mac computer, and that can run a different operating system inside it. In this case, you'll be running an Ubuntu Linux server system.

1. Install Git
You can skip this step if you are not running Windows, but many other courses use Git, so you may want to install it now.

Download Git from git-scm.com. Install the version for your operating system.

On Windows, Git will provide you with the Git Bash terminal program, which you will use to run and connect to your Linux VM.

2. Find your terminal program
To take this course you will need to use a terminal program, which presents the shell user interface and lets you log in to your Linux VM.

Windows: Use the Git Bash program, which is installed with Git (above).
Mac OS X: Use the Terminal program, located in your Applications/Utilities folder.
Linux: Use any terminal program (e.g. xterm or gnome-terminal).
3. Install VirtualBox
VirtualBox is the software that actually runs the VM. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

Ubuntu 14.04 Note: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

4. Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from vagrantup.com. Install the version for your operating system.

Windows Note: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

5. Download the VM configuration file (attached)
Make a new folder to keep your workspace for this course. You might call it Shell, but whatever name you pick is OK. Keep track of what folder you created it in (for instance, Desktop).

In the Supporting Materials section of this page, below, you'll find a link to the configuration file, called Vagrantfile. Download this file into the new folder you just created.

6. Run the virtual machine!
Open your terminal program. Type this shell command and press Enter:

cd Desktop/Shell

(If your new folder is called something other than "Shell", or is located somewhere other than "Desktop", change those.)
