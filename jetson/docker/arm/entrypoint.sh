#!/bin/bash
set -e

# setup ros environment
source "/opt/ros/foxy/local_setup.bash" --
exec "$@"