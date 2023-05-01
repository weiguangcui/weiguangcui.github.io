---
layout: post
title: How to set up Jupyter-lab in the server to use it locally
gh-repo: weiguangcui/weiguangcui.github.io
gh-badge: [star, fork, follow]
tags: [Jupyterlab]
comments: true
---

`ssh` to your server, for example, `ssh yourusername@server.com`

In your server terminal:

`jupyter-lab --no-browser --port 9989`

You will see something like this:
```

To access the server, open this file in a browser:
    file:///users/home2/weiguang/.local/share/jupyter/runtime/jpserver-3207528-open.html
Or copy and paste one of these URLs:
    http://localhost:9989/lab?token=fa2313c28d672b833947512d4be274a4679387f445bb1c0d
 or http://127.0.0.1:9989/lab?token=fa2313c28d672b833947512d4be274a4679387f445bb1c0d
```

You can run the command in `screen` if you want your Jupyterlab runs continually. Leave the running in your server terminal if you don't use `screen`.

Now go back to your local machine. In the local terminal, you need this line to forward the port locally to use Jupyterlab in your browser.

`ssh -N -f -L 127.0.0.1:9989:127.0.0.1:9989 yourusername@server.com`

Afte this, open your browswer and paste the line showup in your server to the address of your browser:

like this: `http://127.0.0.1:9989/lab?token=fa2313c28d672b833947512d4be274a4679387f445bb1c0d`

Then, you should be able to have the Jupyterlab running. Happy coding!
