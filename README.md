# Blensible
* An "Ansible" playbook to distribute Blender 3D movies frames rendering fairly between all servers in your "rendering_farm" group.

## Features
* Fair distribution of frames rendering on all servers in rendering_farm.
* Add as many servers as you want to speed up rendering.
* Support Debian (and its derivatives), OpenBSD and FreeBSD as rendering servers.

## Usage
* Setup connections settings under `[rendering_farm]` group in the inventory file named `hosts`
* Setup preferred settings in `group_vars/rendering_farm` supported variables as follow:
  * `blended_file` : Local path to the .blend file, that is the file to be rendered.
  * `frames_count` : Total frames count
  * `threads`  : Number of cpu cores used for rendering.
  * `output_format` : Output format, default to PNG.
  * `render_directory` : Working directory to store rendered frames.
  * `dest_directory` : Local directory to get gather all rendered frames
* Finally run `ansible-playbook -i host run.yaml`
  

## Limitation
* Number of servers should be less or equal the number of frames in your 3D movie.
* Rendering of any single frame at any time handled ONLY by one server.

