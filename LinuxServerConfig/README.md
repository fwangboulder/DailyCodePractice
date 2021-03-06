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

$ exit
you logout

$ vagrant ssh
you log back in.

If vagrant ssh doesn't work
If you get a message like this:

VM must be running to open SSH connection. Run `vagrant up`
to start the virtual machine.
This means that the VM program is not running, for instance because you rebooted your computer. This is just fine and it doesn't mean you've lost any work. Just run vagrant up to bring the VM back up, then vagrant ssh to log in.

This will not take as long as the first time you ran it, because it won't need to download the Linux OS.

If vagrant up doesn't work
If you get a message like this:

A Vagrant environment or target machine is required to run this
command. Run `vagrant init` to create a new Vagrant environment. Or,
get an ID of a target machine from `vagrant global-status` to run
this command on. A final option is to change to a directory with a
Vagrantfile and to try again.
That means that vagrant can't find the configuration file you downloaded. Go back to the instructions, check to be sure that you did step 5, and then do step 6 again.

Multiple terminals
If you open up more than one terminal window, only the one(s) that you ran vagrant ssh in will be connected to your Linux OS for this course. The others will be connected to your regular OS.

(It's actually really normal for Linux users to have to carefully keep track of which terminal windows are connected to which machines. Don't panic. Just look for whether "vagrant" appears on the command line.)


$ curl http://udacity.github.io/ud595-shell/stuff.zip -o things.zip

$ls

things.zip

Quiz: The Terminal Interface
If you'd like to use the cowsay program outside of the VM, on your own computer, you can install it like this:

Ubuntu and Debian users: sudo apt-get install cowsay

Redhat and CentOS users: sudo yum install cowsay

OS X users: brew install cowsay

(This requires the homebrew, a third party package manager for OS X, http://brew.sh/)

Arch Linux users: sudo pacman -S cowsay

Note: You typically need to be a “superuser” to install new software, that’s why these install commands begin with the sudo command . You can learn more about sudo in our Configuring Linux Web Servers course or on Wikipedia.


Different shells
Unix and Linux programmers over the years have written many different shell programs. You can read more about them on Wikipedia: the original Bourne shell or sh; the C shell or csh; the Korn shell or ksh; the Z shell or zsh; as well as the bash shell that this course uses.

Different systems may have different shells installed by default. Most Linux systems, and Mac OS X, default to bash for interactive shells. However, the most common default shell for scripting (shell programming) is classic sh. BSD Unix systems usually default to sh or ksh.

Almost everything in this course will work the same in any of these shell programs. The exception is one of the file matching (globbing) syntaxes at the end of Lesson 3.

Test for commands in the shell:
vagrant@vagrant-ubuntu-trusty-64:~$ date
Tue Feb 28 07:06:00 UTC 2017
vagrant@vagrant-ubuntu-trusty-64:~$ expr 2+2
2+2
vagrant@vagrant-ubuntu-trusty-64:~$ echo You rock
You rock
vagrant@vagrant-ubuntu-trusty-64:~$ uname
Linux
vagrant@vagrant-ubuntu-trusty-64:~$ hostname
vagrant-ubuntu-trusty-64
vagrant@vagrant-ubuntu-trusty-64:~$ host udacity.com
udacity.com has address 45.79.141.183
udacity.com mail is handled by 20 alt1.aspmx.l.google.com.
udacity.com mail is handled by 20 alt2.aspmx.l.google.com.
udacity.com mail is handled by 30 aspmx2.googlemail.com.
udacity.com mail is handled by 30 aspmx3.googlemail.com.
udacity.com mail is handled by 10 aspmx.l.google.com.
vagrant@vagrant-ubuntu-trusty-64:~$ bash --version
GNU bash, version 4.3.11(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2013 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
vagrant@vagrant-ubuntu-trusty-64:~$ history

Vagrant commands:
vagrant status
vagrant suspend
vagrant up
vagrant ssh
vagrant halt
vagrant destroy

**Linux Security************************************

vagrant ssh: login in as a standard user vagrant

List all of the files within the ubuntu users ssh directory.
$ ls -al /home/ubuntu/.ssh
permission deny!!

$ sudo ls -al /home/ubuntu/.ssh
run as if a root user

get Linux software: package source list.
$cat /etc/apt/sources.list

Keep software up to date with new releases.
$sudo apt-get update
$sudo apt-get upgrade
$man apt-get
get help for apt-get commands

$sudo apt-get autoremove

$sudo apt-get install finger
install new software

Discovering packages:
visit packages.ubuntu.com
common packages:  
Apache HTTP Server:apache2
PostgreSQL:  postgresql
Memcache: memcached

Use finger:
$finger
$finger vagrant
username vagrant

$cat /etc/passwd
file stored information about each user.
vagrant:x:1000:1000::/home/vagrant:/bin/bash

username: encryped passwords:userID:GroupID::homeDir:User's default shell
the hardware was too slow to crack a
well chosen password, thus encryped passwd can be ignored.
empty field is used to store a description about the user.

root:x:0:0:root:/root:/bin/bash


add a new user:
$sudo adduser student
Enter new UNIX password: student
reenter: student
change the user information for student: Full Name[]: Udacity Linux student

$finger student
Login: student        			Name: Udacity Linux Student
Directory: /home/student            	Shell: /bin/bash
Never logged in.
In local machine, connecting as the New User:
 $ssh student@127.0.0.1 -p 2222

 ssh remotely connect to the server
 127.0.0.1 is the IP address (localhost address) we want to connect to.
 port 2222

 $sudo cat /etc/passwd
 student@vagrant-ubuntu-trusty-64:~$ sudo cat /etc/passwd
[sudo] password for student:
student is not in the sudoers file.  This incident will be reported.

go back to vagrant connction: $sudo cat /etc/sudoers
change student to sudo users.

$sudo ls /etc/sudoers.d
$sudo cp /etc/sudoers.d/vagrant /etc/sudoers.d/student
$sudo nano /etc/sudoers.d/student

# CLOUD_IMG: This file was created/modified by the Cloud Image build process
student  ALL=(ALL) NOPASSWD:ALL

$sudo cat /etc/passwd
student:x:1002:1002:Udacity Linux Student,,,:/home/student:/bin/bash

User password expiration:
sudo passwd -e student

Authentication Method:
Public key encryption:
server to client : random message
client to server: encrypt the message with private key
server: decrypt message with public key and see if message is the same as sent out.

Generate key pairs in local computer.
$ssh-keygen
Enter file in which to save the key: /Users/
this path:/Users/Udacity/.ssh/linuxCourse (default)
Enter passphrase:

supported key types: DSA, ECDSA,ED25519, RSA
$ man apt-get ssh-keygen
check -t type

Installing a Public Key in user student connection:
$mkdir .ssh
create a .ssh directory

$touch .ssh/authorized_keys

in local computer:
$cat .ssh/linuxCourse.pub
copy the .pub content and paste it to authorized_keys
$nano .ssh/authorized_keys
$chmod 700 .ssh
$chmod 644 .ssh/authorized_keys

Then log in the student
$ssh student@127.0.0.1 -p 2222 -i ~/.ssh/linuxCourse
i flag and the key pair definitions will allow you to login in
if there is a passphrase for the key pair, enter it.

disable the password base login, and this will force all of your users
to only be able to login using a key pair.
To do this: $sudo nano /etc/ssh/sshd_config
edit the configuration file for SSHD.
PasswordAuthetication yes
change it to no
Then restart the service:
$sudo service ssh restart

File permissions
$ls -al
d or -  directory or file
the other three sections: owner, group, everyone

change file group:
$sudo chgrp root .bash_history
change file owner:
$sudo chown root .bash_history

Default ports for popular Services:
HTTP: 80
SSH:22
POP3:110
HTTPS:443
FTP:21
SMTP:25

Ubuntu comes with a firewall called ufw
$ sudo ufw status

$sudo ufw default deny incoming
$sudo ufw default allow outgoing

configuring Ports in UFW:
SSH adminisrater the server:
$sudo ufw allow SSH

Vagrant set up our SSH on Port 2222
$sudo ufw allow 2222/tcp

allow http services
$ sudo ufw allow www
$sudo ufw enable
