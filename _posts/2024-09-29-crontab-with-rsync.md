---
layout: post
title: crontab with rsync for backing up -- the "Connection closed by UNKNOWN port 65535" error
gh-repo: weiguangcui/weiguangcui.github.io
gh-badge: [star, fork, follow]
tags: [rsync, Linux]
comments: false
comments_id: 6
---

I would like to back up my laptop home directory to a server every night at 12. As such, even I did something stupid like the other day, `rm -rf * ` with a `for` loop includeing `cd ..`. 

The task is very easy, just create a back.sh script and include the rsync command in (see this [post](https://weiguangcui.github.io/2024-03-05-rsync/) for details). Then, you use `crontab -e` to add one additional line at the bottom, e.g. `0 0 * * *  /home/yourname/back.sh`

However, you need to make sure your script is running totally fine. Do Not naively believe that `./home/yourname/back.sh` in your terminal is fine, your `crontab` task will be running OK. `crontab` includes different environments... So, you have to make sure your script as specific as possible, e.g. you may want to avoid any alias in your .bashrc file. But most import of all, test and verify it by replace the line in `crontab` to

```
* * * * *  /home/yourname/back.sh >> /tmp/log 2>&1
```
This will run this job every minute, and out put the running log and err into the file `/tmp/log`. Give a check on that file to see if you have any errors or the output is as expected. 

In my case, it is not surprising this runs to an error:
```
Connection closed by UNKNOWN port 65535
rsync: connection unexpectedly closed (0 bytes received so far) [sender]
rsync error: unexplained error (code 255) at io.c(231) [sender=3.2.7]
```

If you want to know more about this error, add `vvv` to your `rsync` input parameters in the `/home/yourname/back.sh` file. 
<**SOLUTION**> My problem is solved by adding this line to `./home/yourname/back.sh` file, note NOT adding it to the `crontab` tasks:
```
export SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
```
You can see more discussions in this [weblink](https://ubuntuforums.org/showthread.php?t=2281818), I copied the explanation here for backup:
```
>> export SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
>> That seemed to solve the problem - (will mark as solved? - unless there is something wrong / bad about this). It would be good to know why / how this works though, if someone want to elaborate?

You have the loaded the key into the agent and are using it that way, I would guess. The variable SSH_AUTH_SOCK is needed because it points programs to the socket they can use to communicate with the agent. The agent used is ssh-agent, at least for 14.04. You can see if it was started for your user automatically when you logged in.

    ps axjf | less
 
If that is not it, then you can see with lsof what is using that socket.

Whichever account(s) can read and write to the socket can use the keys in that particular agent. Usually there is one agent per user, but root could use the socket too.
```

I don't understand the explanation above clearly. To my opinion, the `ssh` environment in `crontab` is different to my local user environment. A key missing one is the authorization socket (not knowing why), by exporting that in the script, it makes sure that is properly configured in the `crontab` environment.  
