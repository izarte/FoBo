# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build

# Include any dependencies generated for this target.
include OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/depend.make

# Include the progress variables for this target.
include OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/progress.make

# Include the compile flags for this target's objects.
include OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/flags.make

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/flags.make
OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o: ../OpenNI2-FreenectDriver/src/DeviceDriver.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o -c /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/DeviceDriver.cpp

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.i"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/DeviceDriver.cpp > CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.i

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.s"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/DeviceDriver.cpp -o CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.s

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o.requires:

.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o.requires

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o.provides: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o.requires
	$(MAKE) -f OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/build.make OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o.provides.build
.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o.provides

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o.provides.build: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o


OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/flags.make
OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o: ../OpenNI2-FreenectDriver/src/DepthStream.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o -c /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/DepthStream.cpp

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.i"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/DepthStream.cpp > CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.i

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.s"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/DepthStream.cpp -o CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.s

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o.requires:

.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o.requires

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o.provides: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o.requires
	$(MAKE) -f OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/build.make OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o.provides.build
.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o.provides

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o.provides.build: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o


OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/flags.make
OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o: ../OpenNI2-FreenectDriver/src/ColorStream.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o -c /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/ColorStream.cpp

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.i"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/ColorStream.cpp > CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.i

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.s"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver/src/ColorStream.cpp -o CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.s

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o.requires:

.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o.requires

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o.provides: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o.requires
	$(MAKE) -f OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/build.make OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o.provides.build
.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o.provides

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o.provides.build: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o


# Object files for target FreenectDriver
FreenectDriver_OBJECTS = \
"CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o" \
"CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o" \
"CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o"

# External object files for target FreenectDriver
FreenectDriver_EXTERNAL_OBJECTS =

lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o
lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o
lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o
lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/build.make
lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0: lib/libfreenect.a
lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0: /usr/lib/aarch64-linux-gnu/libusb-1.0.so
lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared library ../lib/OpenNI2-FreenectDriver/libFreenectDriver.so"
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/FreenectDriver.dir/link.txt --verbose=$(VERBOSE)
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && $(CMAKE_COMMAND) -E cmake_symlink_library ../lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0 ../lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6 ../lib/OpenNI2-FreenectDriver/libFreenectDriver.so

lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6: lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0
	@$(CMAKE_COMMAND) -E touch_nocreate lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6

lib/OpenNI2-FreenectDriver/libFreenectDriver.so: lib/OpenNI2-FreenectDriver/libFreenectDriver.so.0.6.0
	@$(CMAKE_COMMAND) -E touch_nocreate lib/OpenNI2-FreenectDriver/libFreenectDriver.so

# Rule to build all files generated by this target.
OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/build: lib/OpenNI2-FreenectDriver/libFreenectDriver.so

.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/build

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/requires: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DeviceDriver.cpp.o.requires
OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/requires: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/DepthStream.cpp.o.requires
OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/requires: OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/src/ColorStream.cpp.o.requires

.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/requires

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/clean:
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver && $(CMAKE_COMMAND) -P CMakeFiles/FreenectDriver.dir/cmake_clean.cmake
.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/clean

OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/depend:
	cd /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/OpenNI2-FreenectDriver /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver /media/nvidia/AI-SD/OpenNI2/OpenNI2/libfreenect/build/OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : OpenNI2-FreenectDriver/CMakeFiles/FreenectDriver.dir/depend

