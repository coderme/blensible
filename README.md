# 3D Rendering Farm

## Whats 3d Rendering Farm?
* An "Ansible" playbook to distribute 3D movies frames rendering fairly between all servers in your "rendering_farm" group.

## Features
* Fair distribution of frames rendering on all servers in rendering_farm.
* Add as many servers as you want to speed up rendering.
* Support Debian (and its derivatives), OpenBSD and FreeBSD as rendering servers.

## Limitation
* Number of servers must be less or equal the number of frames in your 3D movie.
* Rendering of any single frame at any time handled ONLY by one server.

