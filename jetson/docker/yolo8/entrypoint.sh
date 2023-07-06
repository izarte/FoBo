#!/bin/bash
set -e

# setup ros environment
source "/opt/ros/dashing/local_setup.bash" --
exec "$@"